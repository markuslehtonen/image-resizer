import os
from PIL import Image

def get_files(curd):
    for f in os.listdir(curd):
        if os.path.isfile(curd + os.sep + f):
            yield f

def get_input():
    size = raw_input("Type destination image resolution separated by a space (eg. 1920 1200): ")
    return tuple(int(i) for i in size.split(" "))

def main():    
    try:
        os.mkdir("thumbnails")
        print "Putting thumbnails in a subdirectory called \"thumbnails\"."
    except OSError:
        print "A thumbnail subdirectory already exists. Putting thumbnails there."
    
    size = get_input()    
    for f in get_files(os.getcwd()):
        try:
            with Image.open(f) as im:
                im = Image.open(f)
                im.thumbnail(size)
                im.save("thumbnails/" + os.sep + f, "JPEG")
        # Handle other than image file formats
        except IOError:
            pass
    print "done"
    
if __name__ == "__main__":
    main()
