from PIL import Image

bits_per_char = 8
def getLSBsFromPixels(binary_pixels):
    totalZeros = 0
    binList = []
    for binaryPixel in binary_pixels:
        for bin_pix in binaryPixel:
            if bin_pix[-1] == '0':
                totalZeros = totalZeros + 1
            else:
                totalZeros = 0
            binList.append(bin_pix[-1])
            if totalZeros == bits_per_char:
                return  binList

def decodeLSB(imageFilename):
    img = Image.open(imageFilename)
    pixels = list(img.getdata())
    binary_pixels = [list(bin(p)[2:].rjust(bits_per_char,'0') for p in pixel) for pixel in pixels]
    binList = getLSBsFromPixels(binary_pixels)
    message = "".join([chr(int("".join(binList[i:i+bits_per_char]),2)) for i in range(0,len(binList)-bits_per_char,bits_per_char)])
    return message