# converts image to pixel format

from PIL import Image
import glob, copy

images = []
image_names = []

for f in glob.glob('pngs/*'):
    image_names.append(f.split('\\')[-1])
    images.append(Image.open(f))
    print('getting images ...')

for img in images:
    pos = copy.copy(images.index(img))
    img = img.resize((20, 16))
    print('resizing all images...')
    img.save('pngs' + '\\' + image_names[pos])
    print('saving...')




