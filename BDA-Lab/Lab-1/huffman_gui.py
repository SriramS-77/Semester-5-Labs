from tkinter import *
from random import randint
import huffman 

top = Tk()

lbl = Label(top, width=40, height=5)
lbl.config(text="Huffman encoder-decoder")
lbl.pack(pady=2)

entry = Entry(top, width=25)
entry.pack(pady=3)

def encode():
    # Example text to encode
    text = entry.get()

    # Generate Huffman encoding tree
    tree = huffman.huffman_tree(text)

    # Generate Huffman encoding dictionary
    encoding_dict = huffman.encoding_dict(tree)

    # Encode text
    encoded_text = huffman.encode(encoding_dict, text)

    # Decode text
    decoded_text = huffman.decode(tree, encoded_text)

    lbl.config(text=f"Encoded: {encoded_text} | Decoded: {decoded_text}")
    
    return

encode_btn = Button(top, cnf={"text": "Encode", "command": encode})
encode_btn.pack()

top.mainloop()