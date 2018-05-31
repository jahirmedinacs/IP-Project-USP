# Image Processing Project

Full Title:

<center>
<span style="font-size:large; font-weight:bold">
  Comparison of Image Enhancement Techniques applied to Sound Data Retrive( from Images )
</span>
</center>

Brief Description:

When an electromagnetic wave-type signal is capture or register, in his raw state, can be representated in multiple ways; but in the case it is a sound, despite the fact is a merly electrical field pertubation, can be also representated as an image; an image who contain the same informatin as the sound but in other information domains. (could have less informatio tho)

* * *

# Project Information

## Student Data

* **Name**: Jahir Gilberth Medina Lopez
* **USP Number**: 1659682

## Description and Project Structure

### Project Area(s)

#### Main Area
  * Super-Resolution

#### Secondariy Area(S)
  * Feature Extraction
  * In-painting
  * Noise Reduction [\*]

[\*] As an auxiliary topic.

### Project Context

#### Project Idea and Data Sources

<span style="font-size:large; font-weight:bold">
  University of Twente
</span>

[Wide-band WebSDR - Web Page](http://websdr.ewi.utwente.nl:8901)

The University of Twente posses a short-wave receiver located at the amateur radio club ETGD offices, who is offered free as an online radio.

![]( ./md-media/site-capture.png "Site Capture")

They allow the possibility of multiple tune-it radio frequency, generating a wide spectrum of available frequencies [0 Mhz - ~30 Mhz]


![]( ./md-media/general-data.png "24 Hours Frequencies Register")

Like it is looks, the image resulting of a complete day of registering frequencies posses a relative "pattern" behavior, in spite of it contents a lot of voice signals [ 0Mhz - 15 Mhz ].

<span style="font-size:large; font-weight:bold">
  The ARSS Project
</span>

[The ARSS Project - Web Page](http://arss.sourceforge.net)

The ARSS Project could be considerer as the main inspiration for this project, it works the idea of sound reconstruccion from images, however, the project was first develop for Sound-to-Image conversion.

The way it is works is converting images as if it were a frecuency domain data, this method of Sound-from-Image Data Retrive method is generic enough to convert any image to sound, being usefull in this project.

[The ARSS Project - Examples](http://arss.sourceforge.net/examples.shtml)

<center>
  <img src="http://arss.sourceforge.net/examples/lena/lena_small.png" border="0">
  <audio controls="controls">
    <source type="audio/mp3" src="http://arss.sourceforge.net/examples/lena/lena.mp3"></source>
  <p>Your browser does not support this audio format.</p>
  </audio>
  <img src="http://arss.sourceforge.net/examples/lena/lena_result_small.png" border="0">
</center>


### Project Objective(s)
  * Find a correlation between "General Data" ( 24h Images), "Detailed Data" (1min Images) and "Specific Data" (Sound) in the process of pattern recognicion.

  ![]( ./md-media/detailed-data.png "Detailed Data 1")

  ![]( ./md-media/sound-plt.png "Detailed Data 2")

[Specific Data (Sound File Sample)](./md-media/audio_player.html)

<audio controls="controls">
  <source type="audio/mp3" src="./md-media/websdr_recording_start_2018-05-17T00_10_41Z_7076.8kHz.mp3"></source>
  <source type="audio/ogg" src="./md-media/websdr_recording_start_2018-05-17T00_10_41Z_7076.8kHz.ogg"></source>
  <p>Your browser does not support this audio format.</p>
</audio>

  * Improve the image quality (register along 1 day) , focusing in the "pattern behaviored" areas (for example at the 27550 MHz Frequency), making more easy the feature extraction process.

  * The Feature Extraction process it gona be performed in a more detailed image (1 min images), and usit as a correctness proof.

### Possible Solutions Steps
  * Retrive all the possible "General Data" [Picture Above] (400 ~ 500 samples)
  
  ![]( ./md-media/samples-url.png "Sample Urls")

  ![]( ./md-media/retrive-samples-script.png "Script for Sample Retrive")

  * Split the data in "Detailed Data" Sizes
  * Find Match between all of them (same pattern) an proceed to increase de resolution
  * Re-Generates a "General Data" image.
  
  > Speculative Steps
  
  * Applys an CNN
  * Applys an SVM
  
  > Fix Steps
  
  * Compare the behavior of the same data at diferent levels (General, Detailed, Specific) and contrast his Features or the information available in every one of them.

# Project Development

# Project Results