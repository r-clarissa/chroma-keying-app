import os
import numpy as np
import cv2

INPUT_PREFIX = "./input/"

def main():
  files = os.listdir(INPUT_PREFIX)

  #Variables to merge
  backGround = cv2.VideoCapture("Background Video.mp4")         #variable that contains the background
  
  #READING ALL INPUT FILES
  inputs = {}

  #Variables for the output video
  SIZE = (1920, 1080)
  FPS = int(backGround.get(cv2.CAP_PROP_FPS))

  resultVideo = cv2.VideoWriter('result.avi', cv2.VideoWriter_fourcc(*"MJPG"), FPS, SIZE)     #variable that holds the output video
 
  while True:
    pass  # chroma keying techniques

main()