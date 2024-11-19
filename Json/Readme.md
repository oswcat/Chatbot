En este apartado podrás encontrar el funcionamiento del archivo JSON y el por qué se eligió la tecnología de backend para el proyecto.
### funcionamiento del archivo JSON
El archivo JSON se utiliza en este proyecto para almacenar toda la información que necesita el bot para encontrar las preguntas que se vayan a hacer y cómo tiene que responder.
##### ¿Comó funciona el archivo JSON?
Funciona de una manera muy sencilla y facil de utilizar en un futuro. La *flexibilidad* que nos da el manejar este archivo nos permite tener un **tiempo de vida** mas largo en el proyecto, esto debido a que podemos agregar o eliminar información de manera rápida y fácil. 
#### ¿Qué es una intención?
Una intención es una categoría que representa el propósito detrás de un mensaje del usuario. Permite que el bot entienda qué quiere lograr el usuario y responda de manera precisa.

Cada intención tiene:

1.**Un nombre**: Identifica de manera única la intención.
2.**Patrones**: Son ejemplos de lo que el usuario podría    escribir para activar esa intención.
3.**Respuestas**: Son las respuestas que el bot puede dar cuando identifica esta intención.
##### Intenciones y patrones.
En el modelo de entrenamiento supervisado se emplea un archivo JSON que contienen las preguntas y respuestas que se van a utilizar para entrenar el model. Por lo tanto se tienen que identificar las intenciones con las que el usuario se vaya a comunicar con el bot. Por ejemplo, si el usuario pregunta *"info"*, el bot tiene que buscar en su directorio la pregunta info o alguna similar. En nuestro archivo JSON tenemos info en *"oferta educativa"* entonces el bot le va a responder con un mensaje dandole todas las opciones de la oferta educativa.
>Es muy importante aclarar comó funciona el BOT y el por que se escogio esta forma de funcionamiento, para saber identificar las intenciones del usuario y responder de manera adecuada.
##### Ejemplo de intenciones.
```python
{
  "name": "Administracion_de_empresas",
  "patterns": ["Administración de empresas", "Administración", "Empresas"],
  "responses": ["[la respuesta sobre Administración de Empresas va aquí]"]
}
1.*name* (Nombre):
El identificador único de esta intención. En este caso, es "Administracion_de_empresas".
Esto ayuda a organizar y manejar las intenciones de manera clara.

2.*patterns* (Patrones):
Son las palabras o frases que el bot usará para identificar esta intención. Ejemplo:

"Administración de empresas"
"Administración"
"Empresas"
3.*responses* (Respuestas):
Contiene las respuestas que el bot dará cuando esta intención sea detectada. En este caso, hemos usado un marcador **([la respuesta sobre Administración de Empresas va aquí])** para personalizarlo después

