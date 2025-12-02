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


# Cuando se abre la selección de tren, ruta o estación, puede aparecer una opción marcada por defecto. Para actualizar la lista y dejar todo sin seleccionar, solo presione cualquier opción nuevamente, El boton mostras info solo sale despues de apretar crear no es nesesario crear. 

Funcionamiento interno 
el programa se maneja mediante diccionarios y listas en memoria, por que son mas fexcibles lo que los vuelve mas faciles de manipular.
Para almacenar se utilizo ".json" ya que permite el guardado mediante lista o diccionarios

# Trenes
los trenes se crean con una ruta asaignada, una estacion y una via que este disponible
estos contienen una lista de vagonesy cada uno con una lista de pasajeros generados de manera aleatoria, su cantidad esta delimitada por porcentajes de minimos y maximos 

# estacion y vias
Las estaciones contienen su numero de vias donde pueden esta ocupadas o no, una vez creado el tren a este se leasigna una via y esta pasa a estar ocupada

# Ruta
las rutas guarda un nombre meramente 

# interfaz grafica
se utilizo tkinder por su facilidad y integracion con python, la interfaz permite la creacion de rutas estaciones vias y trenes, todo esto dividido en ventanas especificas


# atributos
Tren
Cada tren se guarda con los atributos:
nombre: Nombre del tren.
ruta: Ruta asignada.
estacion: Estación donde se encuentra al crearse.
via: Vía ocupada dentro de la estación.
pasajeros: Lista de listas; cada sublista representa un vagón y contiene los pasajeros creados.

Estación
Cada estación contiene:
nombre: Nombre de la estación.
vias: Número total de vías disponibles.
vias_ocupadas: Lista de vías que ya tienen un tren asignado.

Ruta
Actualmente posee:
nombre: Nombre de la ruta.

# eventos importantes

creacion de estacion
donde se define su nombre, y su total de vias que se va actualizando
seleccion de estacion y vias al crear un tren
cuando se elige una estacion, y se revisa cual vias estan libres permitiendo solo usar las no ocupadas
generacion de pasajeros al crear un nuevo tren se le generan un numero aleatoria de pasajeros
asignacion de un tren a una via 

# Línea de tiempo
Módulo del reloj
El proyecto utiliza un módulo llamado Reloj (importado desde reloj/reloj.py), que controla el tiempo interno.
Se decidió que este reloj pueda modificarse para simular el paso del tiempo actual.

# caso especial
el caso especial solo manda un mensaje de precaucion 