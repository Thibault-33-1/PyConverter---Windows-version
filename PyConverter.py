#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

import os
import sys
import subprocess

from tkFileDialog import *
from PIL import Image

avi_state = False
avi_button_state = False

mp4_state = False
mp4_button_state = False

mpeg_state = False
mpeg_button_state = False

flv_state = False
flv_button_state = False

mp3_state = False
mp3_button_state = False

wav_state = False
wav_button_state = False

ogg_state = False
ogg_button_state = False

aif_state = False
aif_button_state = False

bmp_state = False
bmp_button_state = False

jpeg_state = False
jpeg_button_state = False

png_state = False
png_button_state = False

tga_state = False
tga_button_state = False

main_window = ""
filename = ""
filename_no_extensions = ""
path = ""

def create_window():
    global main_window
    main_window = Tk()
    main_window.title('PyConverter v1.0')
    main_window.resizable(width=False, height=False)

    global filename
    global filename_no_extensions

    global avi_button_state
    global mp4_button_state
    global mpeg_state_button_state
    global flv_state_button_state

    global mp3_state_button_state
    global wav_state_button_state
    global ogg_state_button_state
    global aif_state_button_state

    global bmp_state_button_state
    global jpeg_state_button_state
    global tga_state_button_state

    # Video formats
    global avi_state
    avi_state = IntVar()
    global mp4_state
    mp4_state = IntVar()
    global mpeg_state
    mpeg_state = IntVar()
    global flv_state
    flv_state = IntVar()

    # Music formats
    global mp3_state
    mp3_state = IntVar()
    global wav_state
    wav_state = IntVar()
    global ogg_state
    ogg_state = IntVar()
    global aif_state
    aif_state = IntVar()

    # Images formats
    global bmp_state
    bmp_state = IntVar()
    global jpeg_state
    jpeg_state = IntVar()
    global png_state
    png_state = IntVar()
    global tga_state
    tga_state = IntVar()

    #Create video converter LabelFrame
    label_video = LabelFrame(main_window, bd=2, text='Video converter')
    label_video.pack(fill="both", side="left")
    Label(label_video).pack()

    #Create audio converter LabelFrame
    label_audio = LabelFrame(main_window, bd=2, text='Audio converter')
    label_audio.pack(fill="both", side="left")
    Label(label_audio).pack()

    #Create images converter LabelFrame
    label_img = LabelFrame(main_window, bd=2, text='Images converter')
    label_img.pack(fill="both", expand=False)
    Label(label_img).pack()

    # Check butttons for video convertion
    avi_button = Checkbutton(label_video, text="To .avi", variable=avi_state)
    avi_button.pack(anchor=W)

    mp4_button = Checkbutton(label_video, text="To .mp4", variable=mp4_state)
    mp4_button.pack(anchor=W)

    mpeg_button = Checkbutton(label_video, text="To .mpeg", variable=mpeg_state)
    mpeg_button.pack(anchor=W)

    flv_button = Checkbutton(label_video, text="To .flv", variable=flv_state)
    flv_button.pack(anchor=W)

    # Check butttons for images convertion
    jpeg_button = Checkbutton(label_img, text="To .jpeg", variable=jpeg_state)
    jpeg_button.pack(anchor=W)

    bmp_button = Checkbutton(label_img, text="To .bmp", variable=bmp_state)
    bmp_button.pack(anchor=W)

    png_button = Checkbutton(label_img, text="To .png", variable=png_state)
    png_button.pack(anchor=W)

    tga_button = Checkbutton(label_img, text="To .tga", variable=tga_state)
    tga_button.pack(anchor=W)

    # Check butttons for Audio convertion
    mp3_button = Checkbutton(label_audio, text="To .mp3", variable=mp3_state)
    mp3_button.pack(anchor=W)

    wav_button = Checkbutton(label_audio, text="To .wav", variable=wav_state)
    wav_button.pack(anchor=W)

    ogg_button = Checkbutton(label_audio, text="To .ogg", variable =ogg_state)
    ogg_button.pack(anchor=W)

    aif_button = Checkbutton(label_audio, text="To .aif", variable=aif_state)
    aif_button.pack(anchor=W)

    # Convert Button
    convert_button = Button(main_window, text="Convert", width=13, command=get_checkbutton_state)
    convert_button.pack(anchor=E)

    main_window.mainloop()

def get_checkbutton_state() :
    filename_no_extensions = get_file_path()

# Convert Video
    avi_button_state = avi_state.get()
    if avi_button_state == True :
        get_only_filename()
        convert_to_avi()

    mp4_button_state = mp4_state.get()
    if mp4_button_state == True :
        get_only_filename()
        convert_to_mp4()

    mpeg_button_state = mpeg_state.get()
    if mpeg_button_state == True :
        get_only_filename()
        convert_to_mpeg()

    flv_button_state = flv_state.get()
    if flv_button_state == True :
        get_only_filename()
        convert_to_flv()

# Convert Audio
    mp3_button_state = mp3_state.get()
    if mp3_button_state == True :
        get_only_filename()
        convert_to_mp3()

    wav_button_state = wav_state.get()
    if wav_button_state == True :
        get_only_filename()
        convert_to_wav()

    ogg_button_state = ogg_state.get()
    if ogg_button_state == True :
        get_only_filename()
        convert_to_ogg()

    aif_button_state = aif_state.get()
    if aif_button_state == True :
        get_only_filename()
        convert_to_aif()

# Convert Images
    bmp_button_state = bmp_state.get()
    if bmp_button_state == True :
        get_only_filename()
        convert_to_bmp()

    jpeg_button_state = jpeg_state.get()
    if jpeg_button_state == True :
        get_only_filename()
        convert_to_jpeg()

    png_button_state = png_state.get()
    if png_button_state == True :
        get_only_filename()
        convert_to_png()

    tga_button_state = tga_state.get()
    if tga_button_state == True :
        get_only_filename()
        convert_to_tga()

def get_file_path() :
    global path
    path = open_file()

    get_filename()

def open_file() :
    file_path = askopenfilename(initialdir=sys.argv[0], title='Select File', filetypes = (('all files', '*.*'), ('avi files', '*.avi'), ('mp4 files', '*.mp4'),\
    ('jpeg files', '*.jpg'), ('bmp files', '*.bmp'), ('png files', '*.png'), ('mp3 files', '*.mp3'), ('wav files', '*.wav'), ('ogg files', '*.ogg'), \
    ('aif files', '*.aif')))

    return file_path

def get_filename() :
    inverted_path = ''
    inverted_filename = ''

    i = len(path)
    j = 0

    global filename
    filename = ""
    global filename_no_extensions
    filename_no_extensions = ""

    # Invert the path
    for letter in reversed(path) :
        inverted_path += letter

    # we split the inverted path for get only the file name inverted
    i = 0
    while i < len(inverted_path):
        if inverted_path[i] == '/':
            break
        else :
            inverted_filename += inverted_path[i]
            i += 1

    # we put back the right side of the filename
    for letter in reversed(inverted_filename) :
        filename += letter

    i = 0
    for elt in filename :
        if elt == ' ' :
            os.rename(filename, filename.replace(" ", "_"))
            sys.exit('The file have been renamed please re call convert operation.\nExiting ...\n')


def get_only_filename() :
    global filename
    global filename_no_extensions
    i = 0

    while i < len(filename):
        if filename[i] == '.':
            break
        else :
            filename_no_extensions += filename[i]
            i += 1

# Convert video
def convert_to_avi() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.avi'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_mp4() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.mp4'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_mpeg() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.mpeg'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_flv() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.flv'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

# Convert audio
def convert_to_mp3() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.mp3'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_wav() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.wav'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_ogg() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.ogg'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_aif() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.aif'
    cmd = 'ffmpeg -i ' + filename + ' ' + '-qscale 0' + ' ' + filename_no_extensions
    ret = subprocess.call(cmd, shell=True)
    print('\nDone.')

    if ret == 0 :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

# Convert images
def convert_to_bmp() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.bmp'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_jpeg() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.jpeg'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_png() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.png'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

def convert_to_tga() :
    global filename
    global filename_no_extensions
    global main_window
    global path
    ret = -1

    filename_no_extensions += '.tga'
    image = Image.open(filename)
    ret = image.save(filename_no_extensions)
    print('\nDone.')

    if ret == None :
        path_frame = LabelFrame(main_window, bd=2, text='Converted')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='gold', width=len(path), pady =5)
        file_opening.pack()
    else :
        path_frame = LabelFrame(main_window, bd=2, text='Error')
        path_frame.pack(fill="both", expand=False)
        Label(path_frame).pack()
        file_opening = Label(main_window, text=path, anchor=W, bg='red', width=len(path), pady =5)
        file_opening.pack()

create_window()
