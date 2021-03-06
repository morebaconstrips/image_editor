# Image Editor
Create a new image by editing the one you choose


```
Option         Long option             Meaning
-h             --help                  Show this help text and exit
-g             --grey                  Make the image black and white
-i             --inverse               Invert the colors
-m             --mirror                Mirror the image
-r             --right                 Rotate the image by 90° to the right
-u             --upside                Rotate the image upside-down
-l             --left                  Rotate the image by 90° to the left
```

## How to use it

Open the terminal and type following commands:

- `sudo apt update`
- `sudo apt install python3.8`
- `sudo apt install git`
- `git clone https://github.com/morebaconstrips/image_editor.git`
- `cd image_editor`


`Usage: python3 editor.py [OPTION] <IMAGE_NAME> <NEW_NAME>`

Example: `python3 editor.py -g tiger.png grey_tiger.png`


![alt text](tiger.png  "tiger.png")
![alt text](grey_tiger.png  "grey_tiger.png")


## Contribute!
All contributions are welcome!

