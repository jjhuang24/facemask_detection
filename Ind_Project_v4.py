"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program contains all the user defined functions for Ind_Project

Assignment Information
    Assignment:     Individual Project 
    Author:         Joseph Huang, jjhuang@purdue.edu
    Team ID:        LC5 - 18

Contributor:    None, none@purdue 
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import cv2
import numpy as np
import os
    
def grayscale(row, col, img):  #Convert Image to Grayscale
    redarray = np.zeros((row, col), np.dtype(np.uint8))  #CREATE ARRAYS FOR RED GREEN AND BLUE
    greenarray = np.zeros((row, col), np.dtype(np.uint8))
    bluearray = np.zeros((row, col), np.dtype(np.uint8))
   
    for i in range(row):
        for j in range(col):        
            redarray[i][j] = img[i][j][0]   #DEFINE THE VALUES OF THE RED GREEN AND BLUE ARRAYS
            greenarray[i][j] = img[i][j][1]
            bluearray[i][j] = img[i][j][2] 
    
    grey = np.zeros((row, col,3), np.uint8)
    grey = 0.333 * redarray + 0.333 * greenarray + 0.333 * bluearray  #CONVERT IMAGE TO GRAYSCALE
    arr = np.uint8(grey)
    return(arr)

def facesFind(gray):  #Loacte Faces in Image
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )
    return(faces)

def nosesFind(gray): #Locate Noses in Image
    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    noses = nose_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            maxSize=(60, 60),
            minSize=(40,40)
        )
    return(noses)

def draw(faces, noses, frame):  #Draw Rectangles around faces and noses
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    for (x, y, w, h) in noses:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return(0)

def putText(faces, noses, frame):  #Put Text that shows if user is wearing mask or not on image
    cv2.putText(frame, '', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    if (len(faces) == 1):
        if (len(noses) == 0):
            cv2.putText(frame, 'Wearing Facemask Properly', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 200, 0), 1, cv2.LINE_AA)
        elif (len(noses) > 1):
            cv2.putText(frame, 'Detected Too Many Noses', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'Please Wear Your Mask Properly', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 1, cv2.LINE_AA)
    return(0)    

def image():
    
    while True: 
        IMAGE_PATH = input("Enter your image path: ")  #Get image from user
        file_exists = os.path.exists(IMAGE_PATH)
        if not (file_exists):
            print('\nError: File does not exist')
        if (file_exists):
            break;
            
    # Read the input image
    img = cv2.imread(IMAGE_PATH)
    
    row = len(img)
    col = len(img[1])

    grey = grayscale(row, col, img)  #Convert to Grayscale
    
    # Detect faces
    faces = facesFind(grey)  #Find Faces
    
    noses = nosesFind(grey)  #Find Noses
   
    draw(faces, noses, img)  #Draw rectangles around noses and faces
    
    # Display the output
    putText(faces, noses, img)  #Put text on image 
    cv2.imshow('USER IMAGE', img) #Show the image
    cv2.waitKey(0)
    
    return(0);

def video():
    
    video_capture = cv2.VideoCapture(0) #Use video camera instead of image
    
    while True: 
        ret, frame = video_capture.read() # Capture frame-by-frame
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convert to grayscale using cv2 function instead of my function to reduce lag
    
        faces = facesFind(gray) #Find Faces
        
        noses = nosesFind(gray) #Find Noses
    
        draw(faces, noses, frame) #Draw rectangles around noses and faceson video frame
        
        putText(faces, noses, frame)  #Place text on video frame
    
        cv2.imshow('Video', frame) # Display the resulting frame
        
        key = cv2.waitKey(10)
        if key in [27, 1048603]: # Press esc key to close window
            cv2.destroyAllWindows()
            break    