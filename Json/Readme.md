En este apartado podrás encontrar el funcionamiento del archivo JSON y el porqué se eligió la tecnología de back-end para el proyecto.
### funcionamiento del archivo JSON
El archivo JSON se utiliza en este proyecto para almacenar toda la información que necesita el bot para encontrar las preguntas que se vayan a hacer y cómo tiene que responder.
##### ¿Cómo funciona el archivo JSON?
Funciona de una manera muy sencilla y fácil de utilizar en un futuro. La *flexibilidad* que nos da el manejar este archivo nos permite tener un **tiempo de vida** más largo en el proyecto, esto debido a que podemos agregar o eliminar información de manera rápida y fácil. 
#### ¿Qué es una intención?
Una intención es una categoría que representa el propósito detrás de un mensaje del usuario. Permite que el bot entienda qué quiere lograr el usuario y responda de manera precisa.

Cada intención tiene:

1.**Un nombre**: Identifica de manera única la intención.

2.**Patrones**: Son ejemplos de lo que el usuario podría    escribir para activar esa intención.

3.**Respuestas**: Son las respuestas que el bot puede dar cuando identifica esta intención.
##### Intenciones y patrones.
En el modelo de entrenamiento supervisado se emplea un archivo JSON que contiene las preguntas y respuestas que se van a utilizar para entrenar el modelo. Por lo tanto, se tienen que identificar las intenciones con las que el usuario se vaya a comunicar con el bot. Por ejemplo, si el usuario pregunta *"info"*, el bot tiene que buscar en su directorio la pregunta "info" o alguna similar. En nuestro archivo JSON tenemos info en *"oferta educativa"* entonces el bot le va a responder con un mensaje dándole todas las opciones de la oferta educativa.
>Es muy importante aclarar comó funciona el BOT y el por que se escogio esta forma de funcionamiento, para saber identificar las intenciones del usuario y responder de manera adecuada.
##### Ejemplo de intenciones.
```python
{
  "name": "Administracion_de_empresas",
  "patterns": ["Administración de empresas", "Administración", "Empresas"],
  "responses": ["[la respuesta sobre Administración de Empresas va aquí]"]
}
```
##### ¿Cómo funcionan las intenciones?
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
###### Intenciones que se han identificado.
*Bienvenida. 

*Cursos. 

*Preguntas frecuentes. 

*Oferta educativa (General). 

*Bachillerato general. 

*Prepa UNAM. 

*Asesor. 

*Asesores ocupados. 

*Ubicación de la institución. 

*Despedida *Opcional. 

*Pregunta de seguimiento. 

*Información de contacto. 

*Extensiones. 

*Redes sociales. 

*Costos *opcional. 

*Datos de contacto. 

*Vacantes laborales. 

*Extensiones.

*Redes Sociales.

*Diferencias entre bachillerato y prepa UNAM.

*Servicios Escolares.

*Cajas.

**Intenciones de Licenciaturas**

*Administración de Empresas.

*Administración de Empresas Turísticas.

*Arquitectura.

*Ciencias de la Comunicación.

*Comercio Internacional.

*Contaduría.

*Derecho.

*Diseño Gráfico.

*Fisioterapia.

*Gastronomía.

*Ingeniería en Sistemas Computacionales.

*Mercadotecnia.

*Nutrición.

*Psicología.

*Pedagogía.

**Licenciaturas Empresariales**

**Licenciaturas Sabatinas**

*Derecho. 

*Administración de empresas. 

**Licenciaturas en Línea**

*Contaduría. 

*Pedagogía. 
> Nota: Se tienen conflictos con estas carreras porque existen igual en modelo presencial, por lo tanto, el Bot tiene que preguntar que modalidad y de ahí dar la respuesta.

 **Intenciones de Maestrías**

 *Administración y gestión estratégica de talento humano. 

 *Derecho fiscal y administrativo. 

 *Derecho procesal penal acusatorio y adversarial. 

 *Educación. 

 *Seguridad de sistemas y tecnologías de la información. 


**Diplomados**

*Neuromarketing

*Sabor y salud

*Habilidades gerenciales.

##### Manejo de imagenes para responder.

En el transcurso del desarrollo del BOT, se han identificado las distintas maneras de responder a un mensaje de un usuario y como se puede evitar el mandar mensajes extremadamente largos y buscar la manera de hacer la información más digerible para el usuario.
Por lo que se ha propuesto el manejo de imagenes en las respuestas del BOT, para que el usuario pueda visualizar la información de manera más clara y rápida.
Por eso mismo se tiene que modificar la estructura del archivo *.JSON* para que pueda incluir las imagenes en sus respuestas.
##### Estructura modificada del archivo *.JSON*

```python
    {
      "name": "location",
      "patterns": [
        "ubicación",
        "dirección",
        "donde están",
        "como llegar"
      ],
      "responses": [
        {
          "text": "Nos encontramos en [dirección de la institución].",
          "image": "https://ejemplo.com/images/ubicacion.jpg"
        }
      ]
    }
```
Si no se tiene una imagen para enviar, la estructura tiene que cambiar, no se borra el campo *"image"* se tiene que poner un *NULL* en vez de una *URL*.

```python
    {
      "name": "location",
      "patterns": [
        "ubicación",
        "dirección",
        "donde están",
        "como llegar"
      ],
      "responses": [
        {
          "text": "Nos encontramos en [dirección de la institución].",
          "image": null
        }
      ]
    }
```

##### Explicación.

En esta nueva estructura la respuesta se categoriza en dos partes: texto e imagen. Messenger no permite el envío de imagenes localmente, por lo tanto, la imagen solo se puede guardar mediante una *URL* y se tiene que asegurar que la imagen esté disponible en el servidor para que el usuario pueda visualizarla.

El problema encontrado en este punto es que la imagen se tiene que cargar a un servidor y si solo contamos con la máquina que está alojando al bot tiene que crear otro servidor para alojar las imagenes, lo que puede ser un problema de seguridad y de costo.

Se han planteado distintas opciones y la más factible es guardar las imagenes en la página institucional y utilizar la *URL* de la imagen para que el usuario pueda visualizarla.
Esto nos ahorraría el costo de crear otro servidor y nos permitiría tener un mejor control sobre la seguridad de las imagenes.