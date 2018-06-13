Relatório parcial

O relatório parcial deve incluir a proposta denitiva que a dupla ou estudante está
perseguindo. Deve ser um repositório no github, cujo README deve conter as seguintes
informações:
1. nome e número USP;
2. tema do projeto, título do projeto e descrição breve;
3. exemplos de imagens, incluindo a fonte das imagens (onde foram obtidas);

4. descrição breve dos métodos a serem utilizados para resolver o problema (ex.
suavização, detecção de bordas, morfologia, segmentação, analise de texturas, análise
de cores, análise de planos de bits, transformada de imagem, detecção de pontoschave,
etc.),

Adicionalmente, deve ter um arquivo em PDF, Markdown ou Jupyter Notebook contendo:
1. descrição dos primeiros métodos testados, e apresentação de resultados preliminares;
2. próximos passos a serem realizados (métodos)
Enviar por email o link para o repositório com o assunto [SCC0251-2018] Parcial
Prazo para submissão do relatório parcial em um repositório: 11/06

## Full Title:

<center>
<span style="font-size:large; font-weight:bold">
  Comparison of Image Enhancement Techniques applied to Sound Data Retrieve( from Images )
</span> 
</center>

## Brief Description:

When an electromagnetic wave-type signal is capture or register, in his raw state, can be represented in multiple ways; but in the case it is a sound, despite the fact is a merely electrical field perturbation, can be also represented as an image; an image who contain the same information as the sound but in other information domains. (could have less information too)

* * *

## Student Information

* **Name**: Jahir Gilberth Medina Lopez
* **USP Number**: 1659682

## Project Area(s)

### Main Area
  * Super-Resolution

### Secondary Area(S)
  * Feature Extraction
  * In-painting
  * Noise Reduction [\*]
  * Image Restoration
  * Sound Processing [\*]

[\*] As an auxiliary topic.

# This Project as it is, are gonna be abandoned

, and I gonna switch for other, but the current state of this projects are gonna be described briefly:

* Because all the data retrieved from real noise source have a lot of background noise (removable via spectrum analysis) was omitted and shifted to use studio quality sound. 
(see Data Sources)

* the methods used to convert the data from sound to image was:

  * Generate the frequency spectrum of a sample
  * use this frequency spectrum per sample to create an image (spatial domain)
  * the image have width and height, the width are define by the *frames* in the sample (frames are defined by bitrate * time ) , and the height by number of octaves per pixels, so for example (and like was used) have a range from 27 Hz to 22 kHz and 120 pixels per octave the image approximately are gonna have 2.4e3 pixels.

* sounds samples are made using python  (cutting, and adding noise).
* the inducted noise was random noise, using the random pack from python.

[Scripts Links](partial_links.md)

# Examples :

Sub-Sampling Data from '01 - Tank!" (only left chanel) (Sound) (and his generated images)

### Pure:

![](./project_data/images/tank_sample_pure_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_pure_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>

### 10% noice:

![](./project_data/images/tank_sample_random_10_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_10_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


### 20% noice:

![](./project_data/images/tank_sample_random_20_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_20_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


### 30% noice:

![](./project_data/images/tank_sample_random_30_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_30_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


50% noice:

![](./project_data/images/tank_sample_random_35_1_L.bmp)

<center>
  <audio controls="controls">
    <source type="audio/wav" src="./project_data/tank_sample_random_35_1_L.wav"></source>
    <p>Your browser does not support this audio format (WAV).</p>
  </audio>
</center>


## Project Context

### Project Idea

The main idea of the project is to retrieve damage images of sound data and return enhance sound data, the images are generated from sound signals.
The sound signals itself can be converted to images, but, during the sound data reception its possible to get analog images (as frequency "pictures" of sound, like an analog TV). This redundant data could help in the enhancement sound process, not only improving the sound quality filtering the sound data, also filter the image data associated with the sound 

### Data Sources

#### University of Twente

[Wide-band WebSDR - Web Page](http://websdr.ewi.utwente.nl:8901)

The University of Twente posses a short-wave receiver located at the amateur radio club ETGD offices, who are offered free as an online radio.

![]( ./md-media/site-capture.png "Site Capture")

They allow the possibility of multiple tune-it radio frequency, generating a wide spectrum of available frequencies [0 Mhz - ~30 Mhz]


![]( ./md-media/general-data.png "24 Hours Frequencies Register")

Like it is looks, the image resulting of a complete day of registering frequencies posses a relative "pattern" behavior, in spite of its contents a lot of voice signals [ 0Mhz - 15 Mhz ].
#### Musical Discs ***"downloads.Khinsider"***
For the part where the need is to perform a sound quality test by humans, was necessary have sound data in excellent quality.
The website Downloads. Khinsider provides some animes/video games soundtracks albums, for this project was used the album [** Tank, The Best**](https://downloads.khinsider.com/game-soundtracks/album/cowboy-bebop-tank-the-best) from the anime Cowboy Bebop (besides the copyright issues this could be considered a "fair use").

### Inspirations

#### The ARSS Project

[The ARSS Project - Web Page](http://arss.sourceforge.net)

The ARSS Project could be considered as the main inspiration for this project, it works the idea of sound reconstruction from images, however, the project was first to develop  Sound-to-Image conversion.

The way it works is converting images as if it were a frequency domain data, this method of Sound-from-Image Data Retrieve method is generic enough to convert any image to sound, being used in this project.

[The ARSS Project - Examples](http://arss.sourceforge.net/examples.shtml)

<center>
  <img src="http://arss.sourceforge.net/examples/lena/lena_small.png" alt="Lena" style="width:120px;height:120px;">
  <img src="./md-media/bidirectional.png" style="width:40px;height:40px;">
  <audio controls="controls">
    <source type="audio/mp3" src="http://arss.sourceforge.net/examples/lena/lena.mp3"></source>
    <p>Your browser does not support this audio format (MP3).</p>
  </audio>
</center>


## Project Objective(s)

### Principal Objective

<center>
<span style="font-size:large; font-weight:bold">
  Find what method performs statistically better in the process of image enhance.
</span>
</center>

### Secondary Objectives
  * Test the efficiency in developing time and execution time

  * Compare the "human-perceived" quality, having a 99% of accuracy not always mean have a nice sound

## Solution Steps
  * Get all the possible "General Data" that it gonna be use [Picture Above] ( 50~100 samples)
    * [2016-02-01 Full Day Image](http://websdr.ewi.utwente.nl:8901/fullday/day16832.png)
    * It also gonna be used some *music samples for the "human" quality test*

  * Get the subsamples relatives to the identified patterns in the general data
  * Find Match between all of them (same pattern) and proceed to increase the number of samples
  * Start the tests
  * Compare
  * Get Results

### Test Types
  
**The Project performs 3 different test:**

1. Using data to test every chosen method, getting the best and the worst methods (quality of results)
2. Using the methods obtained, applying the same methods and comparing the accuracy of the "quality prediction"
3. Testing the methods in data who were not used in any of the steps before

**Types of Data**
  
  1. General Image:
    This kind of image represents the original data (sound) with compression in the time domain; representing, for example, 1 hour in a *2min length* image.
    ![]( ./md-media/general-data.png "General Image - 24 Hours")
  2. Detailed Image:
    This kind of image represents the original data (sound) without compression in the time domain
    ![]( ./md-media/detailed-data.png "Detailed Data 1 - Same bitrate")
    ![]( ./md-media/sound-plt.png "Detailed Data 2 - Same bitrate")
  3. Specific Data:
    Is just the sound data, it is considered as an original because his purpose is being the quality references in any of the tests.

[Specific Data (Sound File Sample)](./md-media/audio_player.html)
<center>
  <audio controls="controls">
    <source type="audio/mp3" src="./md-media/websdr_recording_start_2018-05-17T00_10_41Z_7076.8kHz.mp3"></source>
    <source type="audio/ogg" src="./md-media/websdr_recording_start_2018-05-17T00_10_41Z_7076.8kHz.ogg"></source>
    <p>Your browser does not support this audio format (MP3 / OGG).</p>
  </audio>
</center>

The specific methods that are gonna be used, for now, are just tentative, to avoid unnecessary changes in this section. they are just gonna be adding when they are developed (all of them with his respective background)

