# Reto 3. Tercer capitulo de RabbitMQ

Created: April 6, 2024 9:14 AM

- Ejercicio 2
    
    [Ejercicio_practico.pdf](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/Ejercicio_practico.pdf)
    
    1. Levantar cluster de rabbitmq con docker-compose.
    
    ```bash
    sudo docker-compose -f rabbitmq.yml up
    ```
    
    ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1.png)
    
    1. Levantar el servicio api en python
        
        ```bash
        uvicorn main:app --reload
        ```
        
        ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%201.png)
        
    2. Crear una cola directa llamada **tienda** donde se enviará la compra del carrito
    a. Si el producto que seleccionaste su stock es mayor que cero agregarlo a la venta
    final
        
        ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%202.png)
        
    
    3. Crear una cola directa llamada compra donde se envíe la venta generada
    
    ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%203.png)
    
    1. Levantamos celery escuchando en las dos colas:
        
        ```bash
        #Cola que escucha cuando el cliente está realizando la compra
        celery -A tasks worker --loglevel=info -Q tienda
        
        #Cola que escucha cuando la compra se realiza si el stock es mayor a 0
        celery -A tasks worker --loglevel=info -Q compra
        ```
        
        1. Se consume el endpoint con postman
            
            ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%204.png)
            
        2. Cola tienda
            
            ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%205.png)
            
        3. Cola compra
            
            ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%206.png)
            
    2. Crear una cola directa para notificar la compra al usuario y en la task de celery realizar
    cualquiera de las opciones:
    a. Notificar enviando un email
    b. Guardar los datos de la compra en redis.
        
        ![5.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/5.png)
        
        ![1.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/1%207.png)
        
        ![2.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/2.png)
        
        ![3.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/3.png)
        
        ![4.png](Reto%203%20Tercer%20capitulo%20de%20RabbitMQ%20b80c9ffae83b40ffbe3804d9c818dcdc/4.png)