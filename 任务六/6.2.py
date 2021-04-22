from PIL import Image

im = Image.open("D:\\python代码\\任务六\\1.jpg")

width = im.size[0]  
height = im.size[1]

im = im.resize((int(width * 0.3), int(height * 0.3)))

im.save('123.jpg')
