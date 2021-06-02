from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)

filtered_image = img.convert('L')

# filtered_image.save('grey.png', 'png')

box = (100,100,400,400)
region = filtered_image.crop(box)

# resize = filtered_image.resize((300, 300))

# region.save('grey.png', 'png')

astro = Image.open('./astro.jpg')
new_astro = astro.resize((400,400))
# astro.thumbnail((400,200))
new_astro.save('thumbnail.jpg')