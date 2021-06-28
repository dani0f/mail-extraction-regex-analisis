# mail-extraction-regex-analisis
Se recopilan datos de los headers de correos y luego se generan los regex de cada uno en busca de patrones.

Se implemento un algoritmo propio para encontrar el regex de un set de datos, este se baso en el siguiente repositorio \url{https://github.com/benstreb/regex-generator}, el código original de este repositorio entrega la expresión regular en donde junta todos los caracteres que hay en las columnas del dataset y los concatena con corchetes cuadrados.

Este se modifico debido a que el resultado del algoritmo encontrado era muy extenso y restringido, buscando asi reducir su tamaño y la precisión en el rendimiento. La solución planteada consiste principalmente en tomar la expresión regular larga y agruparla, esto se hace definiendo rangos de caracteres y luego conmutarlos según cierta diferencia entre ellos. 
