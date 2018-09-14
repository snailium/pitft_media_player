#!/bin/bash

MEDIA_ROOT=~/Media
MEDIA_DIR=.

WALLPAPER=/home/pi/grumpy-cat.png

MENU_DEFAULT=

SELECTION=menu.sh.$$

function list_media {

  DIR_WORKING=${MEDIA_ROOT}/${MEDIA_DIR}
  DIR_LIST=$(ls -1 ${DIR_WORKING} | perl -p -e 's/^(.*)\n$/$1 $1 /g')
  DIR_UP=

  if [ -z ${MEDIA_DIR} ]; then
    DIR_UP='.. "Parent directory" '
  fi

  if [ -e ${SELECTION} ]; then
    rm -rf ${SELECTION}
  fi

#  sudo killall fbi
#  sudo fbi -a --noverbose -T 2 ${WALLPAPER} &

  DEFAULT_ITEM=
  if [ ! -z ${MENU_DEFAULT} ]; then
    DEFAULT_ITEM="--default-item ${MENU_DEFAULT}"
  fi

  dialog --clear \
  --backtitle "Ultra Super Media Management" \
  --cancel-label "Exit" \
  --no-tags --no-shadow \
  ${DEFAULT_ITEM} \
  --title "[ VIDEO PLAYER ]" \
  --menu "${MEDIA_DIR}" 25 40 20 \
  ${DIR_LIST} 2>"${SELECTION}"



#  echo dialog --clear --backtitle "Ultra Super Media Management" \
#  --title "[ ${MEDIA_DIR} ]" \
#  --menu "${DIR_WORKING} \n\
#  Choose the item" 15 50 4 \
#  ${DIR_LIST}  2>"${SELECTION}"

  RETURN=$?
  RESULT=$(<"${SELECTION}")

  case $RETURN in
    0)
      # Valid selection
      ITEM=${DIR_WORKING}/${RESULT}
      echo ${ITEM}
      if [ -f "${ITEM}" ]; then
        omxplayer -o hdmi ${ITEM}
        MENU_DEFAULT=${RESULT}
        list_media
      fi
      if [ -d "${ITEM}" ]; then
        MEDIA_DIR=${MEDIA_DIR}/${RESULT}
        MENU_DEFAULT=
        list_media
      fi
      ;;

    1)
      # Pressed "Cancel"
      gracefully_exit
      if [ ${MEDIA_DIR} != ${MEDIA_ROOT} ]; then
        MEDIA_DIR=$(dirname ${MEDIA_DIR})
      fi
      MENU_DEFAULT=
      list_media
      ;;

    255)
      # Pressed "ESC"
      if [ ${MEDIA_DIR} != ${MEDIA_ROOT} ]; then
        MENU_DEFAULT=$(basename "${MEDIA_DIR}")
        MEDIA_DIR=$(dirname "${MEDIA_DIR}")
      fi
      list_media
      ;;

  esac
}

function gracefully_exit {
  if [ -e ${SELECTION} ]; then
    rm -rf ${SELECTION}
  fi
  exit
}

list_media


