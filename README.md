# shellcode_generator
shellcode generator for x86

```


   _____ _          _ _               _
  / ____| |        | | |             | |
 | (___ | |__   ___| | | ___ ___   __| | ___
  \___ \| '_ \ / _ \ | |/ __/ _ \ / _` |/ _ \
  ____) | | | |  __/ | | (_| (_) | (_| |  __/
 |_____/|_| |_|\___|_|_|\___\___/ \__,_|\___|
  / ____|                         | |
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|


usage: shellcode_generator.py [-h] [-a ARCH] [-f FORMAT] [-v] IFILE

positional arguments:
  IFILE                 input file

options:
  -h, --help            show this help message and exit
  -a ARCH, --arch ARCH  shell code architecture: elf32 (default), elf64, macho32, macho64, win32, win64
  -f FORMAT, --format FORMAT
                        output format. for example '\x' -> '\xde\xad\xbe\xef', '' -> deadbeef
                        print as hexadecimal as default
  -v, --verbose         verbose mode
```

### # Installation (linux or mac)
      curl https://raw.githubusercontent.com/AmitNiz/shellcode_generator/main/install.sh | sh

### # Troubleshooting
make sure that you have `nasm` and `objdump` installed and accessible from shell.
