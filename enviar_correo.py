import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, mensaje, remitente, contraseña):
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587

    # Crear el objeto mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Añadir el cuerpo del mensaje
    msg.attach(MIMEText(mensaje, 'plain'))

    # Conectar al servidor SMTP
    try:
        server = smtplib.SMTP(servidor_smtp, puerto_smtp)
        server.starttls()
        # Iniciar sesión en el servidor SMTP
        server.login(remitente, contraseña)
        # Enviar el correo electrónico
        server.send_message(msg)
        print("Correo enviado correctamente")
    except Exception as e:
        print("Error al enviar el correo:", str(e))
    finally:
        # Cerrar la conexión con el servidor SMTP
        server.quit()
