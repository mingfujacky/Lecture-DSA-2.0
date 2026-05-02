def hashing_chaining(table, key):
    """Hashing with chaining."""
    # Initializing a table with 10 empty lists (buckets)
    index = key % 10
    table[index].append(key)


if __name__ == "__main__":
    hash_table = [[] for _ in range(10)]
    keys_to_insert = [10, 24, 17, 3, 31, 13, 23, 33]
    for key in keys_to_insert:
        hashing_chaining(hash_table, key)

    for i in range(len(hash_table)):
        print(f"Bucket {i}: {hash_table[i]}")
