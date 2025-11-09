# INFO081-simulaci-n-de-trenes
En el presente archivo se podrán ejecutar los inicios de un simulador general de estaciones para la Empresa de Ferrocarriles del Estado (EFE), donde se busca el monitoreo, recopilación y ajuste de datos sobre las personas, trenes, estaciones y rutas tomadas.

integrantes
Matias villanueva /matias2005-20
Raúl Risco /drkanhub
Benjamín Molina
Cristóbal Pairo
Brian Vallejos

Se utilizarán indicadores como el generador de trenes, que tiene como objetivo crear trenes en función de los datos establecidos, y el generador de pasajeros, encargado de producir personas pasajeras para dichos trenes según la hora y otros datos de importancia.

En este proyecto se planea guardar los datos mediante archivos .txt, ya que es el medio de almacenamiento más fácil de utilizar y de interactuar con ellos.

Dentro de la carpeta “proyecto_trenes” se encuentra el archivo “simulacion 1.5.py”, el cual actúa como el archivo principal del programa. En la misma carpeta se ubica la subcarpeta “ui”, que contiene el archivo “menu.py”, considerado el segundo archivo núcleo del programa, ya que en él se ejecuta gran parte de la funcionalidad principal.
El archivo simulacion 1.5.py contiene el bloque if __name__ == "__main__": y actúa como punto de inicio del simulador.
Posteriormente, el programa carga ui/menu.py, que gestiona la interfaz gráfica y la ejecución de los módulos secundarios.

El archivo se debe iniciar en “simulacion 1.5.py”, donde, al presionar el botón “Iniciar”, se abrirá el menú principal. En este menú se podrán crear y mostrar datos de los distintos momentos de simulación mediante la opción “Crear”.