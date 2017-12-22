import glob
import os

raw_dir = "/home/pi/rawdata/"
pro_dir = "/home/pi/prodata/"
upload_server = "192.168.0.30"

for file in glob.glob(raw_dir+"gps_log*"):
    os.system("gpsbabel -i nmea -f " + file + " -o kml -F " + pro_dir + "gps" + file.split('.',1)[0].split('/gps')[1] + ".kml")
    os.rename(file, file.split('/gps')[0] + "/old/gps" + file.split('/gps')[1])

#while True:
#    if os.system("ping -c 1 -W 2 " + upload_server) is 0:
#        break
#
#if glob.glob(pro_dir + "gps*"):
#
