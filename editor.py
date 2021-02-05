import png
import sys

def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            list = []
            for i in range(0, len(line), 3):
                list += [(line[i], line[i + 1], line[i + 2])]
            img += [list]
        return img


def save(img, filename):
    pngimg = png.from_array(img, 'RGB')
    pngimg.save(filename)


#######################################################
#######################################################


def grayscale(img):
    gray = []
    for line in img:
        row = []
        for pixel in line:
            mid = sum(pixel) // 3
            row.append((mid, mid, mid))
        gray.append(row)
    return gray


#######################################################


def inverse(img):
    return [
        [(255 - r, 255 - g, 255 - b) for r, g, b in row]
        for row in img
    ]


#######################################################


def mirror(img):
    return [
        list(reversed(row))
        for row in img
    ]


#######################################################


def rotate_90(img):
    h, w = len(img), len(img[0])
    return [[img[h - x - 1][y] for x in range(h)] for y in range(w)]


#######################################################


def rotate_180(img):
    h, w = len(img), len(img[0])
    ret = [[(0, 0, 0)] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            ret[y][x] = img[h - 1 - y][x]
    return ret


#######################################################

def rotate_270(img):
    h, w = len(img), len(img[0])
    return [[img[x][y] for x in range(h)] for y in range(w)]


def help():
    print("Usage: python3 editor.py [OPTION] <IMAGE_NAME> <NEW_NAME>\n"
          "Create a new image by editing the one you choose\n\n"
          "Option         Long option             Meaning\n"
          "-h             --help                  Show this help text and exit\n"
          "-g             --grey                  Make the image black and white\n"
          "-i             --inverse               Invert the colors\n"
          "-m             --mirror                Mirror the image\n"
          "-r90           --rotate90              Rotate the image by 90° to the right\n"
          "-r180          --rotate180             Rotate the image by 180° to the right\n"
          "-r270          --rotate270             Rotate the image by 270° to the right\n")


def usage():
    print("Usage: python3 editor.py [OPTION] <IMAGE_NAME> <NEW_NAME>\n"
          "Try 'python3 editor.py --help' for more information.")


if __name__ == '__main__':
    try:
        option = sys.argv[1]
        if option == "-h" or option == "--help":
            help()
            exit()

        img = load(sys.argv[2])
        if option == "-g" or option == "--grey":
            new = grayscale(img)
        elif option == "-i" or option == "--inverse":
            new = inverse(img)
        elif option == "-m" or option == "--mirror":
            new = mirror(img)
        elif option == "-r90" or option == "--rotate90":
            new = rotate_90(img)
        elif option == "-r180" or option == "--rotate180":
            new = rotate_180(img)
        elif option == "-r270" or option == "--rotate270":
            new = rotate_270(img)

        save(new, sys.argv[3])

    except NameError:
        print(f"{option} option is not valid.\n"
              "Try 'python3 editor.py --help' for more information.")
    except png.FormatError:
        print("PNG file has invalid signature.")
    except FileNotFoundError:
        print(f"No such file or directory: {sys.argv[2]}")
    except IndexError:
        usage()
