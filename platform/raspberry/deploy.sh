# /bin/bash

TFTP_FOLDER=/srv/tftp

cp "$1" "$TFTP_FOLDER/test.img"

echo "COPIED $1 TO $TFTP_FOLDER/test.img"