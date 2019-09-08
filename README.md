# Proyecto Final IronHack 
## BeerTective

BeerTective es un programa que, mediante el procesamiento de imágenes por webcam, es capaz de reconocer distintos modelos de cervezas para posteriormente mostrarte información adicional sobre estas. 

## PROCESO
La base de datos desde la que se basa el programa tuvo que se creada a partir de imágenes grabadas desde la propia webcam.
Mediante la grabación de video y la posterior divisón por frames se pudo crear una base de datos suficiente para poder trabajar en el modelo de clasificación de imágenes. Cada modelo tiene alrededor de unas 600 imágenes.

Una vez creada la base de datos, se lleva entrena un modelo de red neuronal convolucional[1] capaz de detectar y clasificar de forma eficaz los distintos modelos de cerveza de la base de datos.

Los modelos de cerveza utilizados para este primer programa son:
- Budweiser
- Coronita
- Heineken
- Mahou
- Pilsner Urquell
- San Miguel
- (Nothing): Esta ultima categoría era un fondo en blanco para que cuando no hubiese ningun modelo de cerveza en la cámara, el programa no detectase ninguna marca.

Cuando el programa detecta durante ms de 5 segundos, y con un alto porcentaje de confianza (+95%) un modelo de cerceza, el programa abre la página web de la wikipedia para mostrar información adicional del producto que se está mostrnado por la webcam.

## Archivos

- BeerTective.py: El programa de detección de modelos de cerveza. Abrirá la webcam para que muestres algunos de los modelos de cerveza con los que ha sido entrenado.
- Creating DataBase (Video&Split).ipynb: Jupyter Notebook mediante el cual se ha conseguido grabar y splitear los videos para crear la base de datos.
- Modelo_Final.ipynb: Archivo de Jupyter Notebook donde se se encuentra el modelo de CNN que se ha utilizado como modelo.

## Próximas implementaciones:

- [ ] Crear una extensa base de datos de cervezas artesanales.
- [ ] Añadir más opciones para mostrar información sobre las distintas cervezas artesnales a través de web scraping de distintas páginas o APIs donde muestren valoraciones y opiniones de usuarios sobre el producto.
- [ ] Detectar mediante geolocalización el punto de venta más cercano del producto en cuestión.

## NOTAS:

El modelo al estar guardado en local, el programa no se puede ejecutar desde remoto.

---------------------------------------------------------


[1]"La CNN es un tipo de Red Neuronal Artificial con aprendizaje supervisado que procesa sus capas imitando al cortex visual del ojo humano para identificar distintas características en las entradas que en definitiva hacen que pueda identificar objetos y «ver». Para ello, la CNN contiene varias capas ocultas especializadas y con una jerarquía: esto quiere decir que las primeras capas pueden detectar lineas, curvas y se van especializando hasta llegar a capas más profundas que reconocen formas complejas como un rostro o la silueta de un animal." Fuente: (https://www.aprendemachinelearning.com/como-funcionan-las-convolutional-neural-networks-vision-por-ordenador/)
