import zlib
import cbor2
from cose.messages import CoseMessage
import base45 as base45
from pyzbar.pyzbar import decode
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def decoder():
    Tk().withdraw()
    f_types = [('Photos', '.png .jpg, .jpeg')]
    qrcode = askopenfilename(filetypes=f_types)

    data = decode(Image.open(qrcode))
    data = data[0].data.decode('ascii')
    b45data = base45.b45decode(data[4:])
    decompressed = zlib.decompress(b45data)
    cose = CoseMessage.decode(decompressed)
    decoded = cbor2.loads(cose.payload)
    print(decoded)

if __name__ == '__main__':
    decoder()

