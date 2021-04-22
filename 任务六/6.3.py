#e12.1DrawCharImage.py.py
from PIL import Image

ascii_char = list('"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxr\jft/\|()1{}[]?-/+@<>i!;:,\^`.')

def get_char(r, b, g, alpha=256):

    if alpha == 0:
        return''

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = 256 / len(ascii_char)

    return ascii_char[int(gray // unit)]

def main():
    
    im = Image.open('D:\\python代码\\任务六\\1.jpg')

    width = 100
    height = 60

    im = im.resize((width,height))

    txt=""

    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))

        txt+='\n'

    fo=open("D:\\python代码\\任务六\\pic_char.txt","w")

    fo.write(txt)

    fo.close()
    
main()
