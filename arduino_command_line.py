#===================================================================================================
# Developped by: David Li
# Email: davidli2881@gmail.com
# Date: 1/14/2020
#
# This is a lightweight arduino command line interface, created with the purpose of
# selecting LED strip patterns more easily (as each pattern uses a different .ino file)
# Goal of this project is to eventually develop a GUI that allows a user to select a
# folder containing all of the LED patterns they wish to cycle through, adjust upload
# parameters, and run any sketch without needing to open the IDE. A naive saving method
# will be implemented by creating a save.txt file containing information about previous
# upload preferences and previously loaded folders. The save.txt will be compiled using json
#objects and updated everytime a new folder is uploaded/deleted or preferences change.

# Important setup:
#     Arduino program folder must be set to environment PATH
#     Com port number needs to be predetermined (automatic detection in the future)
#     
#===================================================================================================
import subprocess
import os



def open_ide(): #opens the arduino IDE
    os.system("arduino")

def open_ino(*filepaths): #open input files in arduino IDE
    for file in filepaths:
        command_name = "arduino " + file
        os.system(command_name)

def upload_ino(board, chip, port, filepath): #compiles and uploads sketch according to user parameters
    board_command = parse_board_flag(board, chip)
    port_command = parse_port_flag(port)
    upload_command = parse_upload_flag(filepath)

    command_name = "arduino" + board_command + port_command + upload_command
    os.system(command_name);

def parse_board_flag(board, chip): #generates board selection command
    command = " --board arduino:avr:" + board + ":cpu=" + "chip"
    return command

def parse_port_flag(port): #generates port selection command
    command = " --port " + port
    return command

def parse_upload_flag(filepath): #generates upload selection command
    commmand = " --upload " + filepath
    return command

if __name__ == "__main__":
    os.system("arduino  --version")
