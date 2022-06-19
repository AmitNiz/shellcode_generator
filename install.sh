#!/usr/bin/env bash

if [[ $(uname -s) == "Linux" ]]
then
  DIR_PATH=/opt/shellcode_generator
else
  DIR_PATH=/usr/local/opt/shellcode_generator
fi

LINK_PATH=/usr/local/bin
LINK_NAME=shcg

echo -e "[+] Installing shellcode generator..\n"

(git clone https://github.com/AmitNiz/shellcode_generator $DIR_PATH 2>/dev/null || sudo git clone https://github.com/AmitNiz/shellcode_generator $DIR_PATH) && \
(ln -s $DIR_PATH/shellcode_generator.py $LINK_PATH/$LINK_NAME 2>/dev/null || sudo ln -s $DIR_PATH/shellcode_generator.py $LINK_PATH/$LINK_NAME) && \
echo -e "\n[+] Done. Shellcode Generator is accessible as:\033[1m shcg \033[0m" || \
echo -e "\n[!] Installation Failed."

