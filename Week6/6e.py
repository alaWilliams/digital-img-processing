from collections import Counter

class Node:
    def __init__(self, byte_value, freq, left=None, right=None):
        self.byte_value = byte_value
        self.freq = freq
        self.left = left
        self.right = right


def count_byte_frequencies(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return Counter(data), len(data)


def build_huffman_tree(freq_counter):
    nodes = []
    for byte_value, freq in freq_counter.items():
        nodes.append(Node(byte_value, freq))
    while len(nodes) > 1:
        nodes.sort(key=lambda n: n.freq)  
        smallest = nodes.pop(0)
        second_smallest = nodes.pop(0)
        merged = Node(None, smallest.freq + second_smallest.freq, smallest, second_smallest)
        nodes.append(merged)

    return nodes[0]  # the root


def build_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    if node.left is None and node.right is None:
        codes[node.byte_value] = code if code else "0"
        return codes
    build_codes(node.left, code + "0", codes)
    build_codes(node.right, code + "1", codes)
    return codes


def main(filename):
    freq_counter, total_bytes = count_byte_frequencies(filename)
    root = build_huffman_tree(freq_counter)
    codes = build_codes(root)

    print("Byte (hex)\tOccurrences\tCode")
    for byte_value, freq in sorted(freq_counter.items(), key=lambda x: -x[1]):
        print(f"0x{byte_value:02X}\t{freq}\t{codes[byte_value]}")


main("alice_in_wonderland.txt")

