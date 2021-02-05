# Image Editor
Create a new image by editing the one you choose


```
Option         Long option             Meaning
-h             --help                  Show this help text and exit
-g             --grey                  Make the image black and white
-i             --inverse               Invert the colors
-m             --mirror                Mirror the image
-r90           --rotate90              Rotate the image by 90° to the right
-r180          --rotate180             Rotate the image by 180° to the right
-r270          --rotate270             Rotate the image by 270° to the right
```
Note: Please, make sure you have installed python3!


### How to use it

Open the terminal and type following commands:

- `apt update`
- `apt install git`
- `git clone https://github.com/morebaconstrips/image_editor.git`
- `cd image_editor`


`Usage: python3 editor.py [OPTION] <IMAGE_NAME> <NEW_NAME>`

Example: `python3 editor.py -g tiger.png grey_tiger.png`
