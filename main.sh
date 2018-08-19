#!/bin/bash

MEDIA_ROOT=~/Media
MEDIA_DIR=.

SELECTION=menu.sh.$$

function list_media {

  DIR_WORKING=${MEDIA_ROOT}/${MEDIA_DIR}
  DIR_LIST=$(ls -1 ${DIR_WORKING} | perl -p -e 's/^(.*)\n$/$1 "s" /g')
  DIR_UP=

  if [ -z ${MEDIA_DIR} ]; then
    DIR_UP='.. "Parent directory" '
  fi

  if [ -e ${SELECTION} ]; then
    rm -rf ${SELECTION}
  fi

  dialog --clear --backtitle "Ultra Super Media Management" \
  --title "[ ${MEDIA_DIR} ]" \
  --menu "${DIR_WORKING} \n\
  Choose the item" 15 50 10 \
  ${DIR_LIST}  2>"${SELECTION}"



#  echo dialog --clear --backtitle "Ultra Super Media Management" \
#  --title "[ ${MEDIA_DIR} ]" \
#  --menu "${DIR_WORKING} \n\
#  Choose the item" 15 50 4 \
#  ${DIR_LIST}  2>"${SELECTION}"

  RESULT=$(<"${SELECTION}")

  echo ${RESULT}
 # echo ${DIR_LIST}

  if [ -z ${RESULT} ]; then
    exit
  fi

  ITEM=${DIR_WORKING}/${RESULT}
  echo ${ITEM}
  if [ -f "${ITEM}" ]; then
    omxplayer -o hdmi ${ITEM}
    list_media
  fi
  if [ -d "${ITEM}" ]; then
    MEDIA_DIR=${MEDIA_DIR}/${RESULT}
    list_media
  fi
}

list_media


