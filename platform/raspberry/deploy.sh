# /bin/bash

# old version, used for local tftp server
TFTP_FOLDER=/srv/tftp
cp "$1" "$TFTP_FOLDER/test.img"
echo "COPIED $1 TO $TFTP_FOLDER/test.img\n"



# New version, place file on lab-pc00's tftp server and changes config.txt
REMOTE_TFTP_FOLDER=/proj/tftp/research/rpi4
# cut the name of the selected benchmark from the full path
NAME=$(echo "$1" |rev | cut -d '/' -f 1 | cut -d '.' -f 2 | rev)

# make sure lab-pc00 is configured in your ssh config!
scp "$1" "lab-pc00:$REMOTE_TFTP_FOLDER/$NAME.img"
# change the kernel line to the new image name
ssh lab-pc00 "sed -i -E 's/^kernel=.*/kernel=$NAME.img/' $REMOTE_TFTP_FOLDER/config.txt"

echo "Offering $NAME.img via tftp on lab-pc00!"
