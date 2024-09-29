import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # Frequency of the character(s)
        self.symbol = symbol  # Character(s) represented by the node
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.huff = ""  # Huffman code (0 or 1)
    
    def __lt__(self, other):
        return self.freq < other.freq  # Compare nodes based on frequency

def print_huffman_codes(node, val=""):
    newval = val + node.huff
    
    # Traverse the tree to print Huffman codes
    if node.left:
        print_huffman_codes(node.left, newval)
    if node.right:
        print_huffman_codes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

def main():
    # Take user input for characters and frequencies
    num_chars = int(input("Enter the number of characters: "))
    
    chars = []
    freqs = []
    
    for i in range(num_chars):
        char = input(f"Enter character {i + 1}: ")
        freq = int(input(f"Enter frequency of character '{char}': "))
        chars.append(char)
        freqs.append(freq)
    
    # Create a priority queue (min-heap) for the nodes
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freqs[i], chars[i]))

    # Build the Huffman Tree
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        
        # Assign binary codes
        left.huff = "0"
        right.huff = "1"
        
        # Merge the two nodes and push the new node back into the heap
        newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)

    # Print the Huffman codes by traversing the tree
    print_huffman_codes(nodes[0])

if __name__ == '__main__':
    main()
