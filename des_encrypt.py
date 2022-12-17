from PIL import Image 
from Crypto.Cipher import DES
from Crypto import Random
import hashlib 
 
#key = hashlib.sha256(key.encode()).digest()[:8]

def pad(data): 
    return data + b"\x00"*(8-len(data)%8)  
 
# Maps the RGB  
def convert_to_RGB(data): 
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2])) 
    pixels = tuple(zip(r,g,b)) 
    return pixels 
     
def process_des(filename, filename_out, key):
    key = hashlib.sha256(key.encode()).digest()[:8]
    # Opens image and converts it to RGB format for PIL 
    im = Image.open(filename) 
    data = im.convert("RGB").tobytes()  
 
    original = len(data)   
    new = convert_to_RGB(des_encrypt(key, pad(data))[:original])  
     
    # Create a new PIL Image object and save the old image data into the new image. 
    im2 = Image.new(im.mode, im.size) 
    im2.putdata(new) 
     
    #Save image 
    format = "png"
    im2.save(filename_out+"."+format, format) 

def des_encrypt(key, data, mode = DES.MODE_CBC): 
    des = DES.new(key, mode) 
    new_data = des.encrypt(data) 
    return new_data 
 