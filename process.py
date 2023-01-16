from PIL import Image
import os


def processor(channel):
    return list(channel.getdata())
    # other write option
    # pixels = list(channel.getdata())
    # width, height = channel.size
    # return [pixels[i * width:(i + 1) * width] for i in range(height)]


def run_file(full_file, file_dir, name):
    # full array of bytes
    grb_array = []

    im = Image.open(full_file)

    # resize images per GRB spec
    # green - full rez
    im = im.resize((320, 240), Image.Resampling.BICUBIC)
    # red - 50% rez
    red = im.resize((160, 120), Image.Resampling.BICUBIC)
    # blue - 25% rez
    blue = im.resize((80, 60), Image.Resampling.BICUBIC)

    # green
    green_array = processor(im.split()[1])
    grb_array.extend(green_array)

    # red
    red_array = processor(red.split()[0])
    grb_array.extend(red_array)

    # blue
    blue_array = processor(blue.split()[2])
    grb_array.extend(blue_array)

    grb_bytes = bytes(grb_array)

    path = os.path.join(file_dir, 'grb', '{}.grb'.format(os.path.splitext(name)[0]))
    binary_file = open(path, 'wb')

    for byte in grb_bytes:
        binary_file.write(byte.to_bytes(1, byteorder='big'))

    # other write option
    # with open('../Pictures/test.grb', 'wb') as binary_file:
    #     # Write bytes to file
    #     binary_file.write(grb_bytes)


# assign directory
directory = '../Videos/frames'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        run_file(f, directory, filename)
