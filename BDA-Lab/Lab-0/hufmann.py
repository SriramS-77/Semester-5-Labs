import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    priority_queue = []
    for char, freq in freq_dict.items():
        heapq.heappush(priority_queue, HuffmanNode(char, freq))

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(freq=left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]  # Return the root of the Huffman tree

def build_freq_dict(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1
    return freq_dict

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def encode(data):
    freq_dict = build_freq_dict(data)
    huffman_tree = build_huffman_tree(freq_dict)

    huffman_codes = {}
    build_huffman_codes(huffman_tree, '', huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

def decode(encoded_data, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}

    current_code = ''
    decoded_data = ''
    for bit in encoded_data:
        current_code += bit
        if current_code in reversed_codes:
            decoded_data += reversed_codes[current_code]
            current_code = ''

    return decoded_data

if __name__ == '__main__':
    # Take user input for the data to be encoded
    data_to_encode = input("Enter the data to encode: ")
    
    # Encode the input data
    encoded_data, huffman_codes = encode(data_to_encode)
    print(f"Encoded data: {encoded_data}")
    
    # Take user input for the encoded data to decode
    encoded_data_input = input("Enter the encoded data to decode: ")
    
    # Decode the input encoded data
    decoded_data = decode(encoded_data_input, huffman_codes)
    print(f"Decoded data: {decoded_data}")