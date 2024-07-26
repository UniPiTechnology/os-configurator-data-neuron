#!/bin/sh

[ -f /etc/bootcmd.d/Makefile ] && exit 0

if [ -r /boot/firmware/config.txt ]; then
    CONFIG_TXT=$(readlink -f /boot/firmware/config.txt)
else
    CONFIG_TXT=$(readlink -f /boot/config.txt)
fi

CONFIG_INC=$(dirname "$CONFIG_TXT")/config_unipi.inc

#OVERLAYS="unipi-rtc unipi-neuron"

# create include config file
{
cat <<EOF
dtparam=i2c_arm=on
dtoverlay=unipi_id
dtoverlay=unipi_rtc
EOF

if [ -n "$USE_DS2482" ]; then
    echo "dtoverlay=ds2482"
fi

for overlay in ${DT}; do
    echo "dtoverlay=$overlay"
done
} >"${CONFIG_INC}"
