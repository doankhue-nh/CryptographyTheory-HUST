from PIL import Image 
from Crypto.Cipher import ARC4
import hashlib

#key = hashlib.sha256(key.encode()).digest()[:5]

def convert_to_RGB(data): 
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2])) 
    pixels = tuple(zip(r,g,b)) 
    return pixels 

def process_rc4(filename, filename_out, key): 
    #encode key to byte -> hash algorithm
    key = hashlib.sha256(key.encode()).digest()[:5] 
    
    # Opens image and converts it to RGB format for PIL
    im = Image.open(filename) 
    data = im.convert("RGB").tobytes()  
 
    original = len(data)  
    new = convert_to_RGB(rc4_encrypt(key, data)[:original])  
     
    # Create a new PIL Image object and save the old image data into the new image. 
    im2 = Image.new(im.mode, im.size) 
    im2.putdata(new) 
     
    #Save image
    format = "png"
    im2.save(filename_out+"."+format, format) 

def rc4_encrypt(key, data): 
    rc4 = ARC4.new(key) 
    new_data = rc4.encrypt(data) 
    return new_data 

