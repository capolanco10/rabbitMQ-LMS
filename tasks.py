from typing import Dict, List
from celery import Celery
from models.Producto import Producto
from models.Carrito import Carrito
from models.Venta import Venta
from enviar_correo import enviar_correo
import redis
import json
celery = Celery('tasks', broker='amqp://admin:admin@localhost:5672/',backend='rpc://')

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#Metedo que recibe el producto y lo itera para validar el stock
#si tiene stock, lo envia a la cola de compra
@celery.task
def send_carrito(data:Dict):

    carrito = Carrito(numero=data['numero'], productos=data['productos'])

    products_seleccionados = []
    subtotal = 0.0
    productos = carrito.productos

    for producto in productos:

        product = Producto(name=producto.name, stock=producto.stock, price=producto.price)

        if product.stock > 0:
            products_seleccionados.append(product)
            subtotal += product.stock
        else:
            print("El producto %s no tiene stock para hacer la venta " % (product.name))


    venta = Venta(numero = carrito.numero ,productos = products_seleccionados, subtotal=subtotal, iva=0.15, total=( subtotal * 0.15) + subtotal )

    result = celery.send_task("tasks.send_ventas", args=[venta.dict()], queue="compra")

    print("El id del resultado de envio a la cola de ventas es => %s"%(result.id))


@celery.task
def send_ventas(data:Dict):

    venta = Venta(numero = data['numero'] ,productos = data['productos'], subtotal=data['subtotal'], iva=data['iva'], total=data['total'] )
    json_data = json.dumps(data)

    redis_client.set(data['numero'], json_data)

    print(f"La venta {venta.numero} se ha generado correctamente y se guardo en redis:)")
    
    result = celery.send_task("tasks.send_reporte", args=["Su venta se genero correctamente."], queue="reportes")

@celery.task
def send_reporte(mensaje:str):

    # Ejemplo de uso
    destinatario = 'carlos.polanco010@gmail.com'
    asunto = 'Notificacion de compra'
    remitente = 'carlos.polanco010@gmail.com'
    contraseña = 'syzw ucvw mtff aweo' #contraseña de aplicacion para gmail
    
    enviar_correo(destinatario, asunto, mensaje, remitente, contraseña)
    
    print(mensaje)
    
#----------------------------------------------------------
@celery.task
def operacion(x, y):
    print(f"La multiplicacion de {x} x {y} = {x*y}")

@celery.task
def send_producto(data: Dict):
    producto = Producto(**data)
    if product.stock > 0:
        print("Aplica para la venta")
    else :
        print("No aplica para la venta")
        
@celery.task
def add_products(data: Dict):
    carrito = Carrito(**data)
    print(f"Aplica para el carrito {carrito.numero}")
    