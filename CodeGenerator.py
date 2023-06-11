
import Field
import sys

class CodeGenerator(): # In Constructor: File Path, Bot Starting X, Y, and Rotation

    isDriverRoute = False

    x = 0
    y = 0

    botWidth = 0
    botLength = 0

    botStartingRotation = 0

    code = ""     # If Auton, write 0 at the start, if Driver write 1 at the start

    
    ##########   Format   ##########

    # { X, Y, Theta, Action Code } #

    ################################


    #######   Action Codes   #######

    # Inputted by the end user with 
    # function pointers. 6 possible.
    
    # 1 = 1st Opt: Scored Gamepiece
    # 2 = 2nd Opt: Descored Gamepiece
    # 3 = 3rd Opt: Action
    # 4 = 4th Opt: Action
    # 5 = 5th Opt: Action
    # 6 = 6th Opt: Action

    ################################


    def score():
        
        # Call to field and say that the bot scored, generate code for scoring mechanism.

        print("filler")

    def moveTo(xarg, yarg):

        x = xarg
        y = yarg

        theta = 0
        radius = 0

        # Move to X Position and Y position. Including turn to angle. Find theta by doing trig. Angle between the current mouse pos 
            # and the robot default angle. Radius by how far the mouse is from the robot center. Radius is just for visual purposes.
            # Add an arrow as well pointing away from the bot towards the mouse. Append code to CODE variable. Add way to reverse drive

    def saveToProject():

        # Save the CODE variable to the User's C++ Project. Tie to a button. Use sys for this.

        print("Saved!")

    


















