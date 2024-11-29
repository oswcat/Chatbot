### Diagramas de flujo.
En este espacio se encontrarán los diagramas de flujo de los diferentes procesos que tiene que realizar el BOT y cómo se relacionan entre sí.
Es importante conocer la colorimetría de los diagramas de flujo para entenderles mejor.

![Casos](../img/colorimetria.png)

#### Diagrama de flujo en casos prácticos. 
En el diagrama se presentan distintos casos que el BOT tiene que enfrentar en una interacción "normal" con el usuario.

#### Caso 1: El usuario hace una pregunta que no se encuentra en nuestras opciones.

![Casos](../img/Caso%201%20.png)

En este caso, el BOT no tiene una respuesta predefinida, por lo que sale un mensaje de que no se encuentra la respuesta a la pregunta y le pide al usuario que vuelva a realizar la pregunta.
Esto nos hace entrar en un bucle infinito hasta que el usuario se rinda o haga una pregunta válida. Es un caso muy común en los chatbots. Se han hecho pruebas en las distintas redes sociales a los chatbots que manejan las redes sociales de las empresas y se ha visto que en la mayoría de los casos el usuario se rinde y el bot entra en un bucle infinito.
En el desarrollo del BOT se ha implementado un sistema de límites para evitar que el usuario se rinda y no haga tediosa la tarea de obtener información.

#### Caso 1: Solución.

![Casos](../img/Solucion%20Caso%201.png)

La solución a este problema que se encontró más viable fue implementar un menú de opciones, donde el usuario tenga que elegir una de las opciones que se le presentan. De esta manera se evita el bucle infinito y que el usuario tenga una experiencia más agradable con el BOT.


#### Caso 2: Asesor moderador.

![Casos](../img/Caso%202.png)

El problema que se presentó en este caso es cuando tenemos a un asesor moderando la conversación, y el usuario le hace una pregunta que no se encuentra en las opciones del BOT. El asesor responde, pero el BOT no tiene un sistema de apagado, entonces se crea un conflicto entre el asesor y el BOT. No es un conflicto grave, pero sí puede ser un problema en la comunicación entre el asesor y el BOT, creando una confusión al usuario.
>Cuando se refiere a un asesor no nos referimos al asesor educativo, si no al asesor que esta llevando la red social "Messenger".

#### Caso 2: Soluciones.

##### Caso 2: Solución 1.
![Casos](../img/Propuesta%201.png)

La primera propuesta que se planteó fue que en el menú se integrara una opción para que el usuario pudiera contactar a un asesor (dentro del mismo chat). Se descartó esta opción porque pasaría lo mismo que en el caso 1 (un bucle donde solo sale esta opción) y no tendría sentido el bot porque, a la primera pregunta incorrecta, el usuario escogería contactar a un asesor y el bot no tendría ninguna utilidad.

La segunda propuesta que se planteó es que el BOT tenga un límite de preguntas incorrectas, y que cuando el usuario supere ese límite, el BOT contacte directamente a un asesor. Así se evita el conflicto entre el asesor y el BOT, por lo tanto, también se evitan los bucles infinitos y se mejora la experiencia del usuario.
##### Caso 2: Solución 2.
![Estructura](../img/Estructura.png)
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

##### Caso 3: múltiples preguntas.

![Casos](../img/Caso%203.png)

En múltiples ocasiones se ha visto que el usuario hace múltiples preguntas al BOT. Esto es algo completamente normal, porque el usuario quiere saber toda la información posible en un periodo de tiempo corto, por lo tanto, esto nos puede llegar a crear un problema. Por temas de bucles y si alguna pregunta no está, se identifica su *intención*, el menú se desplegaría. Por lo tanto, una pregunta sí se contesta, pero la otra no, porque no fue identificada.

##### Caso 4: Situaciones Especiales.

![Casos](../img/Caso%204.png)

En ocasiones se ha detectado que el usuario tiene una intención completamente diferente a lo que estamos manejando con el bot. Por lo tanto, la llamamos *"situación especial"*. En este caso, tenemos que implementar un filtro que detecte el número de palabras enviadas y que el BOT contacte a un asesor de manera inmediata. Es parecido al sistema que se propuso cuando se tienen más de dos preguntas incorrectas.

##### Propuesta de flujo de chat.

En esta propuesta se manejan los casos anteriormente encontrados.

1. El usuario le manda un mensaje al BOT.
2. El BOT verifica si el mensaje es mayor a 20 palabras.
3. Si el mensaje **es mayor** a 20 palabras, el BOT contacta a un *asesor*.
4. Si el mensaje **no es mayor** a 20 palabras, el BOT le da la bienvenida.
5. El usuario le hace una pregunta o solicita información.
6. El BOT verifica si la pregunta está en las *intenciones*.
7. Si la pregunta está en las intenciones, el BOT le da la información solicitada.
8. Si la pregunta no está en las intenciones, el BOT tiene que verificar si el conteo de preguntas incorrectas es **mayor o igual a 2**.
9. Si el conteo de preguntas incorrectas es mayor a 2, el BOT contacta a un *asesor*.
10. Si el conteo de preguntas incorrectas no es mayor a 2, el BOT **despliega el menú**.
11. Al finalizar, el BOT hace una verificación de si el usuario ha respondido.
12. Si el usuario ha respondido, el BOT vuelve a empezar el *ciclo*.
13. Si el usuario no respondió, el BOT manda un mensaje de *seguimiento después de X tiempo*.
[^1]: El tiempo *X* puede ser configurado por el administrador del BOT.

![Estructura](../img/Flujosdechat.png)


