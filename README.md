# elige
Un analizador de libros de "Elige tu propia eventura"

La parte tediosa es crear el archivo con los datos del libro: un json donde se definen las paginas y cuales son las posibles siguientes de cada una. (ver archivo `la_taza_de_la_muerte.json`)

Si la proxima página es una o mas páginas, se define una lista, por ejemplo:

    [4, [5]],       -- de la pagina 4 saltar a la 5 (sin opciones)
    [5, [7, 12]],   -- de la pagina 5 se puede elegir saltar a la 7 o a la 12.


Los finales tienen `null` como proxima pagina.

    [12, null],     -- la página 12 es un Fin.


Luego se ejecuta el script pasandole el nombre de archivo:

    ./elige.py --file some_file.json


