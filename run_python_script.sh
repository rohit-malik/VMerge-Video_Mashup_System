#!/bin/sh
echo "hi"
echo "/opt/lampp/htdocs/AndroidUploadImage/$1/"
python2 /home/vmash/VMERGE/Audio_Smoothing/dum.py "/opt/lampp/htdocs/AndroidUploadImage/$1/"
echo " really done!"
