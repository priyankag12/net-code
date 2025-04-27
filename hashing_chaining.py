def chaining_hashing(keys, size):
    table = [[] for _ in range(size)]  # Create list of empty lists
    for key in keys:
        idx = key % size
        table[idx].append(key)  # Simply add (chain) key at correct index
    return table

# --------- MAIN DRIVER CODE -------------

keys = list(map(int, input("Enter keys (space-separated): ").split()))
size = int(input("Enter hash table size: "))

table = chaining_hashing(keys, size)
print("Hash Table with Chaining:")
for i, chain in enumerate(table):
    print(f"Index {i}:", " -> ".join(map(str, chain)) if chain else "None")
