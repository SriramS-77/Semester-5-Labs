from tkinter import *
from random import randint
import huffman 
import collections

top = Tk()

lbl = Label(top, width=100, height=5)
lbl.config(text="Huffman encoder-decoder")
lbl.pack(pady=2)

entry = Entry(top, width=35)
entry.pack(pady=3)

def encode():
    # Example text to encode
    text = entry.get()

    huff = huffman.codebook(collections.Counter(text).items())
    print(huff)

    huffman_encode = str.maketrans(huff)

    encoded_text = text.translate(huffman_encode)

    lbl.config(text=f"Encoded: {encoded_text} | Decoded: {text}")
    
    return

encode_btn = Button(top, cnf={"text": "Encode", "command": encode})
encode_btn.pack()

top.mainloop()