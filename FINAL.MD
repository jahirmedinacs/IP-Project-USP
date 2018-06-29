<script src="https://tex.s2cms.ru/latex.js"></script>

# Visualizacion de Sonidos usando Curvas de Hilberth

## Introduccion

Durante el desarrollo del proyecto (transcurso de las etapas) , se econtro ciertas dificultades para solventar el problema inicial:

* ***Analizar el ruido dentro de un sonido usando la imagen generada por el***

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

