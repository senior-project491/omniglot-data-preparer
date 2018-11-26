from PIL import Image, ImageOps
import os

# where corresponding fonts images of Anglo-Saxon_Futhorc stored
DIGITAL_INPUT_DIR = './input/digital/'
# where actual omniglot dataset resides
HANDWR_INPUT_DIR = './input/handwriting/'
OUTPUT_DIR = './output/'
IMAGE_WIDTH = 105
IMAGE_HEIGHT = 105

# List of digital font images - ignores hidden files
digital_chars = [f for f in os.listdir(DIGITAL_INPUT_DIR) if not f.startswith('.')]
# List of directories which stores an alphabet of actual omniglot dataset.
handwr_char_dirs = sorted([f for f in os.listdir(HANDWR_INPUT_DIR) if not f.startswith('.')])

# loop over chars in an alphabet
for i in range(len(digital_chars)):

    same_char_dir = os.path.join(HANDWR_INPUT_DIR, handwr_char_dirs[i])
    # list of handwriting images of a specific character -relative path
    same_handwr_chars = os.listdir(same_char_dir)
    # Digital font image of given char goes to right on new image
    im_right = Image.open(os.path.join(DIGITAL_INPUT_DIR, str(i+1)+'.png'))
    # create output in the same format as input omniglot folders
    if not os.path.exists(os.path.join(OUTPUT_DIR, handwr_char_dirs[i])):
        os.makedirs(os.path.join(OUTPUT_DIR, handwr_char_dirs[i]))
    # loop over different handwriting of same char
    for k in same_handwr_chars:
        # handwritten image goes to left in new image
        im_left = Image.open(os.path.join(same_char_dir, k))
        new_im = Image.new('RGB', (IMAGE_WIDTH * 2, IMAGE_HEIGHT))
        new_im.paste(im_left)
        # Paste second image to right side
        new_im.paste(im_right, (IMAGE_WIDTH, 0))
        # Invert color since it will be very likely to be used with MNIST in this project
        new_im = ImageOps.invert(new_im)
        new_im.save(os.path.join(OUTPUT_DIR, handwr_char_dirs[i], 'digital_' + k))

