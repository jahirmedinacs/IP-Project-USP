<script src="https://tex.s2cms.ru/latex.js"></script>

# Visualizacion de Sonidos usando Curvas de Hilberth

## Introduccion

Durante el desarrollo del proyecto (transcurso de las etapas) , se econtro ciertas dificultades para solventar el problema inicial:

* ***Analizar el ruido dentro de un sonido usando la imagen generada de el***

Este concepto fue la idea principal del proyecto durante las dos etapas anteriores, sin embargo, presentaba una dificultad: La visualizacion del reuido terminaba estando localizada (que es bueno) pero era indiferenciable del resto de los datos, como se puede ver a continuacion:

### Primer Intento de Visualizacion :

Sub Muestra de la cancion '01 - Tank!" (Canal Izquierdo)

#### Muestra Pura:

![](./project_data/images/tank_sample_pure_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_pure_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>

#### 10% Ruido:

![](./project_data/images/tank_sample_random_10_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_10_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


#### 20% Ruido:

![](./project_data/images/tank_sample_random_20_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_20_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


#### 30% Ruido:

![](./project_data/images/tank_sample_random_30_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_30_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


#### 50% Ruido:

![](./project_data/images/tank_sample_random_35_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_35_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>

* En este caso para convertir el sonido a imagen genera un espectrograma del dominio de frecuecias (Revisar : [Arss Documentation](http://arss.sourceforge.net/doc.shtml)) moviendolo al dominio del espacio usando el concepto de ***octavas***.

* El alto de la imagen esta definida por la cantidad de pixeles por octava y por la minima e maxima frecuencia esto significa que en un rango definido de frecuencias si se tiene 12 octavas se puede "dibujar" $$ 12 \times 8$$ notas entre el rango de frecuencias.

* El largo de la imagen es definido por el ***framerate*** del audio, el tiempo de la muestra y los pixeles por segudo, es decir a 44100 frames, 5 segudos de duracion y 20 pixeles por segundo se tendria $$ \frac{44100 \times 5}{20} $$ pixeles.

Sin embargo , el ruido inducido tiende a acumularse en las areas de **maxima frecuencia** , dada la cualidad de este ruido (Ruido Aleatorio) , siendo esto de poca utilidad; considerando la diferencia entre pixeles esta difuminada por un gradiente de grises , el ruido puede camuflarse si en su entorno el color no pesee mucha **variancia**.

En vista de estos problemas, se mudo el modo de visualizacion de hacia el metodo actual.

## Curva de Hilbert y Transformaciones  1-D -> 2-D 

La [curva de Hilbert](https://en.wikipedia.org/wiki/Hilbert_curve) es aquella curva fractal capas de cubrir completamente un espacio 2 dimensional usando solo una linea (de ahi la denominacion de curva),  una de las propiedades mas importantes de esta curva es que ***dados 2 puntos proximos en la una recta , al ser sometida a una tranformacion via la curva de hilbert, estos puntos se mantiene proximos*** , ademas, la ubacion final de un punto en la recta se mantiene casi constante en su represatacion 2 dimensional (matriz); en otras palabras : ***a mayor resolucion de la imagen (tamano de la matriz) un punto perteneciente a la recta transformada converge a una sola posicion unica y sin superposicion***.

![Curva de Hilberth, 8 Iteraciones recursiva del Fractal](./md-media/Hilbert_curve.gif)

## Archivos WAV y Espacios de Color

Los [archivos WAV](http://soundfile.sapp.org/doc/WaveFormat/) usan una configuracion de valores de tipo PCM , esto significa que por cada ruido registrado se genera un pico de ruido (en el caso de este proycto el rango de picos fue $$ (-2^{15}, 2^{15} - 1) $$.

De esta forma, se puede tener que por cada subframe se genera un pixel de con un color especifico , relativo a dicha intensidad.
Este proceso de conversion ***intensidad -  color*** se realizo usando la idea de que la luz representa un ***frecuencia, una logitud de onda y una amplitud***, [todos estos parametros genera una energia caracteriztica por onda](http://www.fourmilab.ch/documents/specrend/) pudiendose asi (dada una reconfiguracion del rango del sonido) asociar una intensidad de sonido a una intesidad de color y esta a un valor  **RGB**, para automatizar este proceso, se uso el siguiente [Codigo de conversion](http://www.noah.org/wiki/Wavelength_to_RGB_in_Python).

Ambas ideas combinadas con la idea de curva de Hilberth fractal ( automatizado mediante este [codigo](https://github.com/galtay/hilbert_curve) , con una modificacion propia para conseguir paralelizar en un numero arbitrario de kernels ) generan imagenes del siguiente tipo:

<center>
<img src="./data/01 - tank! (tv stretch)_L.png" alt="01 - Tank! (Canal Izquierdo)">
<img src="./data/01 - tank! (tv stretch)_R.png" alt="01 - Tank! (Canal Derecho)">
</center>

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./data/01 - tank! (tv stretch).wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>

## Scripts , Codigo y Resultados

> Dado la resolucion de las imagenes (4096 * 4096) solo se adjuta los resultados ya calculados.

En este experimento se uso el disco musical [Cowboy Bebop Tank! THE! BEST!](http://cowboybebop.wikia.com/wiki/Cowboy_Bebop_Tank!_THE!_BEST!) dada su variedad de sonidos (entre jazz y musica ambiental) permite visualizar el alcance de esta tecnica de representacion de sonido.

### Pasos Usados

###
