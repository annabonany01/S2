import os

#definim aquesta funció per cridar la cmd
def runBash(command):
    os.system(command)

#EX 1
def crop(start, time, input_file, output):
    # -ss es posicio d'inici del video
    # -t el temps que es vol tallar el video
    command = "ffmpeg -i " + input_file + " -ss " + start + " -t " + time + " -c copy " + output
    runBash(command)

#EX 2
def yuv_hist(input_file, output):
    command = "ffmpeg -i " + input_file + " -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay " + output
    # "ffmpeg -i " + input_file + " -c:v rawvideo -pixel_format yuv420p " + output
    runBash(command)

#EX 3
def resize(size, input, output):
    # si la size es 720p o 480p haurem d'escriure -1:720 o -1:480
    # si es 360x240 o 160x120
    command = "ffmpeg -i " + input + " -vf scale=" + size + " " + output
    runBash(command)

#EX 4
def stereo_to_mono(input_file, output):
    #de stereo a mono es ac = 1
    command = "ffmpeg -i " + input_file + " -c:v copy -ac 1 " + output
    runBash(command)


def mono_to_stereo(input_file, output):
    #de mono a stereo es ac = 2
    command = "ffmpeg -i " + input_file + " -c:v copy -ac 2 " + output
    runBash(command)


if __name__ == '__main__':
    crop("00:00:00", "00:00:11", "big_buck_bunny_1080p_stereo.ogg", "BBB_cut_video.ogg")
    yuv_hist("BBB_cut_video.ogg", "BBB_yuv_hist.ogg")
    resize("360:240", "big_buck_bunny_1080p_stereo.ogg", "BBB_resize.ogg")
    stereo_to_mono("BBB_cut_video.ogg", "BBB_stereo_to_mono.ogg")
    mono_to_stereo("BBB_stereo_to_mono.ogg", "BBB_mono_to_stereo.ogg")
