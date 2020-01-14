import subprocess
import os

#Arduino program folder must be set to environment PATH

def open_ino(*filepaths): #open input files in arduino IDE
    for file in filepaths:
        command_name = "arduino " + file
        os.system(command_name)


def upload_ino(board, make, chip, port, filepath): #compiles and uploads sketch
    board_command
    port_command
    upload_command
    command_name = "arduino" + board_command + port_command + upload_command
    os.system(command_name);

def parse_board_flag(board, make, chip):

def parse_port_flag(port):

def parse_upload_flag(filepath):
