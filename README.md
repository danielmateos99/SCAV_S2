### SCAV Seminario 2
Daniel Mateos Manjón
NIA: 205514

## Introducción
Para este seminario 2 de la asignatura de SCAV se nos pide aplicar ciertas modificaciones a el vídeo de Big Buck Bunny (BBB.avi).
En el archivo "capturas_S2.pdf" se pueden observar los comandos de ffmpeg para la terminal que realizan lo pedido en los ejercicios.
En la última parte se nos pide implementar los ejercicios anteriores a python, para ello debemos correr con python desde la terminal el archivo "S2_205514.py" y que el vídeo mencionado se encuentre en la misma localización con el nombre indicado anteriormente.

## Ejercicio 1
Recortamos 10 segundos del vídeo original "BBB.avi" utilizando la línea "ffmpeg -i BBB.avi -ss 00:00:20 -t 00:00:10 -async 1 cut.avi" y creamos un nuevo vídeo llamado "cut.avi".
Los primeros 20 segundos indican a partir de que segundo empezamos a recortar y los siguientes 10 la cantidad de tiempo que extraemos.
Link: https://stackoverflow.com/questions/18444194/cutting-the-videos-based-on-start-and-end-time-using-ffmpeg

## Ejercicio 2
Con la línea " ffplay cut.avi -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" " reproducimos el fragmento "cut.avi" mostrando los histogramas de YUV.
Link: https://trac.ffmpeg.org/wiki/Histogram

## Ejercicio 3
En este ejercicio se nos pide cambiar la calidad del vídeo a las siguentes: 720p, 480p, 360x240 y 160x120.
Para ello utilizamos la siguente línea en terminal: ffmpeg -i cut.avi -vf scale=X:Y,setsar=1:1 cutXxY.avi
"X" y "Y" representan los valores de tamaño que queremos aplicar al vídeo "cut.avi" y guardar el resultado como "cutXxY.avi", donde de nuevo "X" y "Y" representan los valores deseados.

## Ejercicio 4
En esta parte primero utilizamos " ffmpeg -i cut.avi -map_channel 0.1.0 -c:v copy mono.avi " para cambiar el audio del vídeo "cut.avi" a mono y guardarlo como "mono.avi".
Y finalmente cambiamos el codec del audio con " ffmpeg -i mono.avi -acodec mp3 -vcodec copy mono_code2.avi ", el vídeo resultante se guardará como "mono_code2.avi".
Link: https://superuser.com/questions/215430/would-like-to-change-audio-codec-but-keep-video-settings-with-ffmpeg

## Ejercicio 5
Implementamos todos los ejercicios anteriores a python para que al correr el archivo "S2_205514.py". Si lo corremos con "python S2_205514.py" o "python3 S2_205514.py" se nos muestra un menú donde podemos seleccionar cada ejercicio o salir.
Es necesario hacer primero el ejercicio 1, de recortar 10 segundos del vídeo original, ya que el resto de ejercicios se basan en modificar el vídeo resultante de este: "cut.avi".
