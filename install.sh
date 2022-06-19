#!/usr/bin/env sh

DIR_PATH=/usr/local/opt/shellcode_generator
LINK_PATH=/usr/local/bin
LINK_NAME=shcg

echo "[+] Installing shellcode generator..\n"
git clone https://github.com/AmitNiz/shellcode_generator $DIR_PATH && \
ln -s $PATH/shellcode_generator.py $LINK_PATH/$LINK_NAME
echo "\n[+] Done. Shellcode Generator is accessible as:\033[1m shcg \033[0m"
