# A program from B3nam
# Please Run this code on Python version 3 .x
from tkinter import filedialog

xorTo = 0x39
def isEncrypted(first_ten_bytes):
        b = [195, 162, 226, 128, 162, 197, 147, 69, 104, 115]

        if first_ten_bytes == b:
                return True
        else:
                return False
def getExtension(secon_ten_bytes):
        nl = []
        for b in secon_ten_bytes:
                if b != 0:
                        nl.append(b^xorTo)
        return bytes(nl)
def encrypt_extension(ext):
        extb = list(bytes(ext,'utf-8'))
        while len(extb) < 10:
                extb.append(0)
        cext = []
        for b in extb:
                cext.append(b^xorTo)
        return cext
def xor(rest_bytes):
        result = []
        for b in rest_bytes:
                result.append(b^xorTo)
        return result
def add_flags(ext):
        b = [195, 162, 226, 128, 162, 197, 147, 69, 104, 115]
        b = b + encrypt_extension(ext)
        return b

tf = filedialog.askopenfilename(
        title="Open Text file", 
        filetypes=(("Encrypted Files", "*"),)
        )

fr = open(tf, "rb")
content = fr.read()
code = bytes.fromhex(content.hex())
cbytes= list(code)[:10]
if isEncrypted(cbytes):
        extbytes = list(code)[10:20]
        ext = getExtension(extbytes)
        pcontent = xor(code[20:])
        fw = filedialog.asksaveasfile(
        mode='wb',
        title="Save to", 
        filetypes=(("Decrypted File", "*."+ext.decode('utf-8')),),
        initialfile = "output."+ext.decode('utf-8')
        )
        fw.write(bytes(pcontent))
        fw.close()
else:
        ext = tf.split('.')[-1]
        flag = add_flags(ext)
        ccontent = flag+xor(code)
        fw = filedialog.asksaveasfile(
        mode='wb',
        title="Save to", 
        filetypes=(("Decrypted File", "*.*"),),
        initialfile = "output"
        )
        fw.write(bytes(ccontent))
        fw.close()

