# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:21:23 2020

@author: JabaNay
"""

import os

framerate = 60
file_path_out = r"C:\Users\JabaNay\Desktop\CV and Certificates\Proof\test"
file_path = r"C:\Users\JabaNay\Documents\GitHub\JabaNay-Frame-Interpolation\Data_out\Images2\frame"


os.system('yes | cmd /K ffmpeg -r {0} -f image2 -s 1920x1080 -i "{1}%d.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p "{2}.mp4"'.format(framerate,file_path,file_path_out))