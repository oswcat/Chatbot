# Objetivo.

La intención de este repositorio es la creación de un BOT de Messenger que pueda responder de manera automática a los mensajes que se le envíen y pueda interactuar con el usuario de manera efectiva, proporcionando la información que se le solicite.

## 19/11/24

Se empezaron a subir todos los archivos creados con anterioridad , incluyendo el **Reporte de practicas** que se esta modificando diariamente con todos los avances del dia.
A si mismo los **diagramas de flujo** donde se muestran dos de los problemas que se encontraron en el planteamiento del proyecto. Fueron el *"Bucle por directorio no encontrado"* y *"contactar a un asesor"*, en estos dos casos se encontraron soluciones y se han implementado en el proyecto. Con soluciones "sencillas" pero efectivas. Por ejemplo, en el caso del "Bucle por directorio no encontrado" se utilizo un menu en el que el usuario puede seleccionar la opción que satisfaga sus necesecidades . En el caso del "contactar a un asesor" se utilizo una intervención de un asesor que se encuentra moderando el chat. Por lo tanto, se puede decir que se han encontrado soluciones efectivas a los problemas encontrados.

Tambien se puede encontrar el flujo de trabajo del BOT.
![estructura](./img/Estructura.png)
>Diagrama de flujo de como tiene que funcionar el BOT.
###### Comó funciona el BOT:
1. El usuario ingresa al chat y el BOT le da la bienvenida.
2. El usuario haces una pregunta o solicita información.
3. El BOT le da la información solicitada o le hace una pregunta para obtener más información.
4. El usuario responde a la pregunta del BOT.
5. En el caso que la pregunta no este guardada en las intenciones, el bot muestra el menu de opciones.
6. El usuario selecciona una opción del menu.
7. Si la opción seleccionada sigue sin estar en el conocimiento del BOT, el asesor se encarga de ayudar al usuario.
8. Si el usuario deja de responder, el BOT manda un mensaje de seguimiento despues de X tiempo.
[^1]: El tiempo X puede ser configurado por el administrador del BOT. 
[^2]: Ya se encuentran implementadas las soluciones de los casos de uso.