import subprocess
from datetime import datetime
import argparse


def welcome():
    welcome_message = [
        " ___       __   _______   ___       ________  ________  _____ ______   _______              ___  ________  _____ ______   _______   ________          ",
        "|\\  \\     |\\  \\|\\  ___ \\ |\\  \\     |\\   ____\\|\\   __  \\|\\   _ \\  _   \\|\\  ___ \\            |\\  \\|\\   __  \\|\\   _ \\  _   \\|\\  ___ \\ |\\   ____\\         ",
        "\\ \\  \\    \\ \\  \\ \\   __/|\\ \\  \\    \\ \\  \\___|\\ \\  \\|\\  \\ \\  \\\\\\__\\ \\  \\ \\   __/|           \\ \\  \\ \\  \\|\\  \\ \\  \\\\\\__\\ \\  \\ \\   __/|\\ \\  \\___|_        ",
        " \\ \\  \\  __\\ \\  \\ \\  \\_|/_\\ \\  \\    \\ \\  \\    \\ \\  \\\\\\  \\ \\  \\\\|__| \\  \\ \\  \\_|/__       __ \\ \\  \\ \\   __  \\ \\  \\\\|__| \\  \\ \\  \\_|/_\\ \\_____  \\       ",
        "  \\ \\  \\|\\__\\_\\  \\ \\  \\_|\\ \\ \\  \\____\\ \\  \\____\\ \\  \\\\\\  \\ \\  \\    \\ \\  \\ \\  \\_|\\ \\     |\\  \\\\_\\  \\ \\  \\ \\  \\ \\  \\    \\ \\  \\ \\  \\_|\\ \\|____|\\  \\      ",
        "   \\ \\____________\\ \\_______\\ \\_______\\ \\_______\\ \\_______\\ \\__\\    \\ \\__\\ \\_______\\    \\ \\________\\ \\__\\ \\__\\ \\__\\    \\ \\__\\ \\_______\\____\\_\\  \\     ",
        "    \\|____________|\\|_______|\\|_______|\\|_______|\\|_______|\\|__|     \\|__|\\|_______|     \\|________|\\|__|\\|__|\\|__|     \\|__|\\|_______|\\_________\\    ",
        "                                                                                                                                      \\|_________|    ",
    ]
    for line in welcome_message:
        print(line)


def get_weather():
    result = subprocess.run(["sh", "sh_scripts/weather.sh"], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error running weather script:")
        print(result.stderr)


def time_of_day():
    now = datetime.now()
    if now.hour >= 12:
        print("Good afternoon sir\nHere is your weather: ")
    else:
        print("Good morning sir\nHere is your weather: ")


def wacky_scripts_installer():
    result = subprocess.run(["sh", "sh_scripts/installer.sh"], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error running installer script:")
        print(result.stderr)


def homebrew_script_installer():
    result = subprocess.run(["sh", "sh_scripts/Homebrew_installer.sh"], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error running installer script:")
        print(result.stderr)


def installer():
    def wacky_scripts():
        while True:
            user_input = input("Do you wish to continue? yes/no: ")
            if user_input == "yes":
                wacky_scripts_installer()
                break
            elif user_input == "no":
                break
            else:
                print("Invalid input")

    def homebrew_installer():
        while True:
            user_input = input("Do you wish to continue? yes/no: ")
            if user_input == "yes":
                homebrew_script_installer()
                break
            elif user_input == "no":
                break
            else:
                print("Invalid input")

    def quit():
        nonlocal exit_condition
        exit_condition = False

    def default():
        print(
            "-w to install Wacky scripts, which contain a function to delete files and directories with the revolutionary 'fuckthis' 'file or directory'\n"
            "-h to install Homebrew scripts, to speed up the inevitable reformatting of a MacBook xd\n"
            "-x is to quit")

    switch = {
        "-w": wacky_scripts,
        "-h": homebrew_installer,
        "-x": quit
    }

    exit_condition = True
    while exit_condition:
        command = input()
        switch.get(command, default)()



def main(initialize_input):
    welcome()
    time_of_day()
    get_weather()
    if initialize_input:
        installer()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script with an optional input initialization flag.")
    parser.add_argument("-i", "--initialize", action="store_true", help="Initialize the input section")
    args = parser.parse_args()

    main(args.initialize)
