import LSB_Encode
import LSB_Decode

message = "My hidden text =)"
imageFilename = "input.png"
newImageFilename = "output.png"

newImg = LSB_Encode.encodeLSB(message, imageFilename, newImageFilename)
print("Encoded text into image by LSB and stego image created successfully!")

message = LSB_Decode.decodeLSB("output.png")
print("Your image decoded successfully! \nmessage in image: ", message)
