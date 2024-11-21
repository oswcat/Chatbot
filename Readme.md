# Objetivo.

La intención de este repositorio es la creación de un BOT de Messenger que pueda responder de manera automática a los mensajes que se le envíen y pueda interactuar con el usuario de manera efectiva, proporcionando la información que se le solicite.

## 19/11/24

Se empezaron a subir todos los archivos creados con anterioridad, incluyendo el **Reporte de prácticas,** que se está modificando diariamente con todos los avances del día.
A sí mismos los **diagramas de flujo** donde se muestran dos de los problemas que se encontraron en el planteamiento del proyecto. Fueron el *"Bucle por directorio no encontrado"* y *"contactar a un asesor"*, en estos dos casos se encontraron soluciones y se han implementado en el proyecto. Con soluciones "sencillas" pero efectivas. Por ejemplo, en el caso del "Bucle por directorio no encontrado" se utilizó un menú en el que el usuario puede seleccionar la opción que satisfaga sus necesidades. En el caso del "contactar a un asesor" se utilizó una intervención de un asesor que se encuentra moderando el chat. Por lo tanto, se puede decir que se han encontrado soluciones efectivas a los problemas encontrados.

##### También se puede encontrar el flujo de trabajo del BOT.
![Estructura](./img/Estructura.png)
>Diagrama de flujo de como tiene que funcionar el BOT.
##### ¿Cómo funciona el BOT?:
1. El usuario ingresa al chat y el BOT le da la bienvenida.
2. El usuario hace una pregunta o solicita información.
3. El BOT le da la información solicitada o le hace una pregunta para obtener más información.
4. El usuario responde a la pregunta del BOT.
5. En el caso de que la pregunta no esté guardada en las intenciones, el bot muestra el menú de opciones.
6. El usuario selecciona una opción del menú.
7. Si la opción seleccionada sigue sin estar en el conocimiento del BOT, el asesor se encarga de ayudar al usuario.
8. Si el usuario deja de responder, el BOT manda un mensaje de seguimiento después de X tiempo.
[^1]: El tiempo X puede ser configurado por el administrador del BOT. 
[^2]: Ya se encuentran implementadas las soluciones de los casos de uso.

## Configuración del entorno donde se ejecutará el BOT.
##### Configuración de la máquina.
1. Instalar Debian en el servidor.
>Una vez instalado, se tienen que actualizar todos los paquetes.
```bash
sudo apt update && sudo apt upgrade -y
```
2. Configuración de la IP.
>Se tiene que configurar la ip del servidor.
```bash
sudo nano /etc/network/interfaces
 ```
 >Se tiene que modificar la dirección, máscara y gateway dependiendo de la IP que se tenga.
```bash
auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 8.8.4.4
```
```bash
sudo systemctl restart networking
```
3. Instalar Python.
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-dev
```
4. Instalar el framework de Flask.
```bash
pip install flask
```
5. Instalar pip.
```bash
sudo apt update
sudo apt install -y python3-pip
```
6. Instalar ngrok.
```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin
```
>Autentica ngrok (cambia <YOUR_AUTH_TOKEN> por tu token de autenticación):
```bash
ngrok authtoken <YOUR_AUTH_TOKEN>
```
7. Instalar supervisord o systemd.
```bash
sudo apt update
sudo apt install -y supervisor
```
8. Configurar el firewall (ufw para flask).
> Es muy importante instalar de manera correcta el entorno de ejecución del BOT.
##### Librerías necesarias.
1. Spacy.
2. JSON.
3. Datetime.
4. Difflib.
6. Flask.
7. Ngrok.
8. Supervisord o systemd.
> Se agregaran mas si es el caso.

