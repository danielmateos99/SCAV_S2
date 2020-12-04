import os

exit = True
while exit == True:

    print("Selecciona un ejercicio: ")
    print("[1]: Cut 10 seconds of the BBB video")
    print("[2]: Extract the YUV histogram from the cut video and plays a new video with both images at the same time")
    print("[3]: Resize the video into 4 differentsvideo outputs")
    print("[4]: Change the audio into mono output and in a different audio codec")
    print("[5]: Exit")

    a = input()
    x = int (a)


    if x == 1:
        os.system("ffmpeg -i BBB.avi -ss 00:00:20 -t 00:00:10 -async 1 cut.avi")
    elif x == 2:
        os.system('ffplay cut.avi -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"')
    elif x == 3:
        print("Selecciona a que calidad quieres cambiar el vídeo: ")
        print("[1]: 720p")
        print("[2]: 480p")
        print("[3]: 360x240")
        print("[4]: 160x120")
        b = input()
        y = int (b)
        if y == 1:
            os.system("ffmpeg -i cut.avi -vf scale=1280:720,setsar=1:1 cut1280x720.avi")
        elif y == 2:
            os.system("ffmpeg -i cut.avi -vf scale=720:480,setsar=1:1 cut720x480.avi")
        elif y == 3:
            os.system("ffmpeg -i cut.avi -vf scale=360:240,setsar=1:1 cut360x240.avi")
        elif y == 4:
            os.system("ffmpeg -i cut.avi -vf scale=160:120,setsar=1:1 cut160x120.avi")
        else:
            print('Error: Introduce alguno de los valores mencionados.')

    elif x == 4:
        os.system('ffmpeg -i cut.avi -map_channel 0.1.0 -c:v copy mono.avi')
        os.system('ffmpeg -i mono.avi -acodec mp3 -vcodec copy mono_code2.avi')
    elif x == 5:
        exit = False
    elif x == 69:
        print("Easter egg")
        os.system('firefox https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    elif x == 420:
        print("Nice")
    else:
        print('Error: Introduce alguno de los valores mencionados.')
