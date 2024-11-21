### Diagramas de flujo.
En este espacio se encontraran los diagramas de flujo de los diferentes procesos que tiene que realizar el BOT y como se relacionan entre si.
#### Diagrama de flujo en casos prácticos. 
En el diagrama de presentan distintos casos que el BOT tiene que enfrentar en una interaccion "normal" con el usuario.
##### Caso 1: El usuario hace una pregunta que no se encuentra en nuestras opciones.

![Casos](../img/Caso%201%20.png)

En este caso el BOT no tiene una respuesta predefinida, por lo que sale un mensaje de que no se encuentra la respuesta a la pregunta y le pide al usuario que vuelva a realizar la pregunta.
Esto nos hace entrar en un bucle infinito hasta que el usuario se rinda o haga una pregunta valida. Es un caso muy comun en los chatbots, se han hecho pruebas en las distintas redes sociales a los chatbots que manejan las redes sociales de las empresas y se ha visto que en la mayoria de los casos el usuario se rinde y el bot entra en un bucle infinito.
En el desarrollo del BOT se ha implementado un sistema de limites para evitar que el usuario se rinda y no haga tediosa la tarea de obtener informarcion.

##### Caso 1: Solución.

![Casos](../img/Solucion%20Caso%201.png)
