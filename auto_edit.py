import cv2
import numpy
import glob
import os
import python_yt_uploader
import sys
import argparse
import moviepy.editor as mp
from moviepy.editor import *




class Uploader:

        #pass
    def main (self):#grabs all mp4 in local directory

        path = 'N:\VIDEOS\VODS\clips'
        files = glob.glob(path +r'/'+'2022''*'+'.mp4')
        print(files)
        print('files are being prepared for upload' )
        for file in files:
            data = file
            self._resize(self,file, data=data)
            return file#sends each file to be resized
            
    def _resize(self, file, data):
        filename,fileextension = os.path.splitext(data)#splits filename and extension for further manipulation
        cap = cv2.VideoCapture(data)#sets the capture as the file
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        new_name = filename + '_resize' + fileextension
        out = cv2.VideoWriter(new_name, fourcc, 60, (1080, 1080))
        #clip =mp.VideoFileClip(file)
        audioclip = AudioFileClip(file)
        #clip_resized = clip.resize(.8)
        #clip_resized.write_videofile(new_name, bitrate="5000")
        while True:

            ret, frame = cap.read()
            if ret == True:
                b = cv2.resize(frame, (1080, 1080), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
                out.write(b)
            else:
                break
        cap.release()
        out.release()
        #new_file = b

        cv2.destroyAllWindows()

        videoclip = VideoFileClip(new_name)
        avclip = videoclip.set_audio(audioclip)
        avclip.write_videofile(new_name+"_sound"+'.mp4')
        clip2 = mp.VideoFileClip('FollowAlert.mp4')

        final_clip = concatenate_videoclips([clip2, avclip])
        final_clip.write_videofile(new_name + '_final.mp4')
        os.remove(file)
        os.remove(new_name)
        #self.add_intro_outro(self,clip=videoclip, avclip=audioclip,new_name=new_name, file=file)
      #  new_file =
        self._post(self)

    def add_intro_outro (self, clip, avclip,new_name,file):
        clip2 = mp.VideoFileClip('FollowAlert.mp4')
        av_clip = clip.set_audio(avclip)
        final_clip = concatenate_videoclips([clip2,av_clip])
        final_clip.write_videofile(new_name+'_final.mp4')
        os.remove(file)
        os.remove(new_name)
        self._post(self)

    def _post(self):
         #python_yt_uploader()
         os.system(f' start cmd.exe @cmd /k python python_yt_uploader.py')

    def __init__(self):
        self.file = glob.glob("*.mp4")
        self._resize(self)
        self._post(self)

if __name__ == '__main__':
    uploader = Uploader
    self = uploader
    uploader.main(self)
    #main()
 