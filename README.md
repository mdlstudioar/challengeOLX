# challengeOLX
Challenge para OLX group

Repositorio creado para la resolución del challenge de OLX.

--Aclaraciones--

Ejercicio 1:

Tal como le expliqué a Débora, no pude cargar el json modificado en firestore. Vía manual imposible, pero vía código lo intenté de varias maneras sin suerte, creo que ese área debería formarme o capacitarme mejor porque me noté muy precaria.

Tiempo de creación: aproximadamente 1h30-2h, el resto del tiempo fue buscar cómo resolver lo de firestore. Usé herramientas y librerías que ya conocía, y con las que me sentía segura, aunque creo que convertir a df para poder transformar consume más memoria y tiempo de ejecución que trabajar directamente sobre el json, cosa que no pude hacer porque el archivo como tal requería de varias modificaciones y, además, al usar object_hook y cambiar el valor del parámetro debía crear funciones para las distintas transformaciones. 

Cambios: en el caso del df, lo que hice fue chequear si cuando fuera object era susceptible de ser modificado a tipo fecha, previamente rellenando aquellos valores nulos con formato símil fecha "00-00-00" elgí este formato para luego en el análisis poder contrastar los valores que se reemplazaron con los ya existentes, en cado de que se puediera lo convertí a fecha con to_datetime. Luego, para que se pueda hacer en otras url o archivos json y no sólo en éste, puse tmb que se chequeara cuando el tipo es float y fuera factible de convertir a int, aquí me encontré con muchos datos faltantes, como en este caso son counters los reemplacé por -1 por la misma razón de antes, para que ese valor me sirva para contrastar las modificaciones y los valores originales, en el caso de que no fueran counters y hubieran valores iguales a -1, chequeé con -1000 y finalmente si hubiese valores iguasles a -1000, el cambio sería por la media y la cantidad de flotantes igual a 0 para que se puedan convertir en int.

Una vez hecha la modificación volví a convertir el df a json para almacenarlo como tal pero ya con las modificaciones realizadas.

Se podrían hacer mejoras:
-como puse anteriormente, el tema del df consume bastante memoria, quizá iría con más tiempo por pickle y json para trabajar con archivos de tipo bytes y json y poder hacer modificaciones directamente, sin tener que transformar tanto y consumir memoria y tiempo de ejecución
-en el caso de los valores faltantes matchear entre varias alternativas para que eso no infiera luego y el proceso sea lo más limpio y certero posible
-obviamente la carga a la colección de firestore que no la pude hacer

Ejercicio 2:

Si bien respondí todo, la segunda pregunta no estoy del todo segura y confieso que indagué para ver qué sería lo más factible, sin embargo no llegué a ninguna conclusión más que la de la respuesta pero, repito, tengo mis dudas. Del tema modelado nunca he trabajado y, tal como le comenté a Lisandro, es algo que me gustaría aprender, las nociones que tengo son bastante básicas y requeriría práctica en la rama.

Enunciados: [Ejercicio_Data_Engineer_(1).docx](https://github.com/mdlstudioar/challengeOLX/files/7468120/Ejercicio_Data_Engineer_.1.docx)

Respuestas al Ejercicio 2: [Rtas challenge OLX.pdf](https://github.com/mdlstudioar/challengeOLX/files/7468131/Rtas.challenge.OLX.pdf)



