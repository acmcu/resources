#!/usr/bin/python

import subprocess

def main():
    try:
        while True:
            fullname = raw_input("Full Name: ")
            email = raw_input("email: ")

            fd = open("register.txt", "a")
            fd.write(email + '\t|\t' + fullname + '\n')
            fd.close()

            subprocess.call(["figlet", fullname])
            subprocess.call(["fortune"])
            print
    except KeyboardInterrupt:
        print

if __name__ == "__main__":
    main()
