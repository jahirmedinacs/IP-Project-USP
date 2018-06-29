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
