# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 02:01:39 2020

@author: JabaNay
"""

import os




def converting_video_ffmpeg(framerate,file_path,file_path_out):
    os.system('yes | ffmpeg -r {0} -f image2 -s 1920x1080 -i "{1}%d.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p "{2}.mp4"'.format(framerate,file_path,file_path_out))
    return ('ffmpeg -r {0} -f image2 -s 1920x1080 -i "{1}%d.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p "{2}.mp4"'.format(framerate,file_path,file_path_out))


