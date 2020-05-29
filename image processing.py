from PIL import Image, ImageFilter
img = Image.open('../images/PicsArt_03-02-09.22.54.jpg')

print(img)
print(img.mode)

red = img.filter(ImageFilter.SMOOTH)
red.save("kishore.png" , 'png' )   #saves a new file

red_1 = img.convert('L')           #returns some format in RGB - here L gives black and white
red_1.save("kp.png" , 'png')

#red.show()   #-- just shows image
resize = red_1.resize((300,300))
resize.save("size.png",'png')

box = (100,100,100,100)
region = red.crop(box)
red.save("croped.png",'png')