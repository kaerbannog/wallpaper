from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
# import commands
import os.path
from sys import argv
import urllib
import socket
import shutil
import subprocess
import datetime
# print("Total: %d GiB" % (total // (2**30)))
# print("Used: %d GiB" % (used // (2**30)))
# print("Free: %d GiB" % (free // (2**30)))
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blanc = (255, 255, 255)
taillePolice = 40
tailleInterligne = 10
incLine = tailleInterligne+taillePolice
txtX = 1200
txtY = 50


def set_gnome_wallpaper(file_path):

    command = "gsettings set org.gnome.desktop.background  picture-uri '" + file_path + "'"
    print(command)
    os.system(command)


def printinfo(txt, color):
    global draw, helvetica, txtX, txtY, incLine
    draw.text((txtX, txtY), txt, color, font=helvetica)
    txtY += incLine


if __name__ == '__main__':
    if len(argv) <= 1:
        print("usage: %s img_path" % argv[0])
    else:
        img_path = os.path.abspath(argv[1])
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        print(os.getcwd() + "/LemonMilk.otf")
        helvetica = ImageFont.truetype(
            "/home/grut/Bureau/wallpaper/LemonMilk.otf", size=taillePolice)

        hostname = socket.gethostname()
        IPAddr = subprocess.check_output(
            "hostname -I", shell=True).decode('utf-8').split(" ")[0]
        total, used, free = shutil.disk_usage("/")
        p = (int)((free*100)/total)
        # totalr, usedr, freer = shutil.disk_usage("/media/raid")
        info = hostname + " : "+IPAddr + " \n"
        printinfo(info, blanc)

        info = ("Free Space: " + str(p) + "%")+"\n"
        if (p <= 10):
            color = red
        elif (p <= 50):
            color = yellow
        else:
            color = green
        printinfo(info, color)
        now = datetime.datetime.now()
        printinfo(str(now.hour) + ":" + str(now.minute), blanc)
        img.save("/home/grut/Bureau/wallpaper/sample-out.jpg", quality=100)

        if not set_gnome_wallpaper("/home/grut/Bureau/wallpaper/sample-out.jpg"):
            print("Wallpaper changed with success.")
        else:
            print("An error ocurred while setting a new wallpaper.")
# */1 * * * * root python3 /home/grut/Bureau/wallpaper/wp.py /home/grut/Bureau/wallpaper/wall.jpg
