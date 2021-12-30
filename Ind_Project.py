"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program checks if the user is wearing a facemask properly. There are two
    functions that can be used: Image or Video. In image, the user uploads an image
    and the program determines if the person in the image is wearing their facemask 
    properly. In the video function, the same process is followed except the 
    input is taken from the live video feed of the user from their webcam. 

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

from Ind_Project_v4 import image
from Ind_Project_v4 import video

def main():
    
    while True:
        x = input("Enter 'Image' or 'Video': ");  #Give User Choices for Image or Video
        if (x == 'Image'):
            image()  #Call Image Function 
            break;
        elif (x == 'Video'):
            video()  #Call Video Function
            break;
        else: 
            print("\nPlease enter valid choice")

if __name__ == '__main__':
    main()