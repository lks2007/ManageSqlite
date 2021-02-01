#!/bin/bash

FILE=`pwd`"/.env"
i="0"

if [ ! -f "$FILE" ]; then
    echo `pwd` >> $FILE
    echo "$( tput setaf 1 )[*] $(tput setaf 5)$(tput bold)$(tput smul)The file ".env"$(tput rmul) was created with succeed $(tput setaf 7)$(tput sgr0)
    ";
else
    echo "$( tput setaf 1 )[*]" $(tput setaf 5)$(tput bold)$(tput smul)$FILE$(tput rmul) "is arlready created $(tput setaf 7)$(tput sgr0)
    ";
fi

if [ ! -f `pwd`"/conf.ini" ]; then
    echo "How many field do you have in the table of your database ?"
    boolean=true
    while ${boolean}; do
        read -p "> " number
        if [[ "$number" =~ ^[0-9]+$ ]];
            then
            boolean=false
        fi
    done

    CONF="[DEFAULT]"

    while [ $i -lt $number ]; do
        i=$[$i+1]
        read -p "Value> " val
        CONF="$CONF\n$val"
    done
    echo -e $CONF >> `pwd`"/conf.ini"
    echo "$( tput setaf 1 )[*] $(tput setaf 5)$(tput bold)$(tput smul)`pwd`/onfig.ini$(tput rmul) was created with succeed $(tput setaf 7)$(tput sgr0)
    ";
else
    echo "$( tput setaf 1 )[*] $(tput setaf 5)$(tput bold)$(tput smul)`pwd`/config.ini$(tput rmul) is arlready created $(tput setaf 7)$(tput sgr0)
    ";
fi