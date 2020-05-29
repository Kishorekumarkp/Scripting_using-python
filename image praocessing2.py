# compreesing a large image to small size
from PIL import Image , ImageFilter

image = Image.open("../images/ironman.jpg")
#new_img = image.resize((400,400))
#new_img.save("thumbnail.jpg")


#thumbnail method
image.thumbnail((400,400))
image.save('newthumb.jpg')

print(image.size) #decides best size