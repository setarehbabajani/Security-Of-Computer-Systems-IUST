from PIL import Image

bits_per_char = 8
bits_per_pixel = 3
max_bit_stuffing = 2

def check_size_encode(message, image):
    width, height = image.size
    image_capacity = width * height * bits_per_pixel
    message_capacity = (len(message) * bits_per_char) - (bits_per_char + max_bit_stuffing)
    return image_capacity >= message_capacity

def create_binary_triple_pairls(message):
    binaries = list("".join([bin(ord(i))[2:].rjust(bits_per_char,'0') for i in message]) + "".join(['0'] * bits_per_char))
    binaries = binaries + ['0'] * (len(binaries) % bits_per_pixel)
    binaries = [binaries[i*bits_per_pixel:i*bits_per_pixel+bits_per_pixel] for i in range(0,int(len(binaries) / bits_per_pixel))]
    return binaries

def embed_bits_to_pixels(bin_triple_pairs, pixels):
    binary_pixels = [list(bin(p)[2:].rjust(bits_per_char,'0') for p in pixel) for pixel in pixels]
    for i in range(len(bin_triple_pairs)):
        for j in range(len(bin_triple_pairs[i])):
            binary_pixels[i][j] = list(binary_pixels[i][j])
            binary_pixels[i][j][-1] = bin_triple_pairs[i][j]
            binary_pixels[i][j] = "".join(binary_pixels[i][j])
    newPixels = [tuple(int(p,2) for p in pixel) for pixel in binary_pixels]
    return newPixels

def encodeLSB(message, imageFilename, newImageFilename):
    img = Image.open(imageFilename)
    size = img.size
    if not check_size_encode(message, img):
        return None
    bin_triple_pairs = create_binary_triple_pairls(message)
    pixels = list(img.getdata())
    newPixels = embed_bits_to_pixels(bin_triple_pairs, pixels)
    newImg = Image.new("RGB", size)
    newImg.putdata(newPixels)
    newImg.save(newImageFilename)
    return newImg

