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

**¿Quienes somos?**
