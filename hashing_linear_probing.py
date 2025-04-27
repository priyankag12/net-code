def linear_probing_hashing(keys, size):
    table = [None] * size
    for key in keys:
        idx = key % size
        while table[idx] is not None:
            idx = (idx + 1) % size
        table[idx] = key
    return table

keys = list(map(int, input("Enter keys (space-separated): ").split()))
size = int(input("Enter hash table size: "))
table = linear_probing_hashing(keys, size)
print("Hash Table:", table)
