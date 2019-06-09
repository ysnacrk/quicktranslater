#!/bin/bash

echo "Gereksinimler yükleniyor..."

if which pip3 1>/dev/null
then 
    echo "pip paket yönetisi zaten yüklü"

else 
    sudo apt-get install python3-pip
fi

if pip3 list| egrep "googletrans" 1>/dev/null
then 
    echo "googletrans modülü zaten yüklü"
else
    pip3 install googletrans
fi