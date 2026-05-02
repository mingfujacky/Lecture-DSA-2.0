class SimpleHash:
    def __init__(self, size):
        self._size = size
        # A single list to store only the keys
        self._slots = [None] * self._size

    def insert(self, key):
        # 1. Find the starting position
        index = key % self._size

        # 2. Loop until we find an empty slot (None)
        while self._slots[index] is not None:
            print(
                f"Index {index} is occupied by {self._slots[index]}. Moving to next..."
            )

            # Move to the next index, wrapping back to 0 if we hit the end
            index = (index + 1) % self._size

        # 3. Place the key in the empty slot
        self._slots[index] = key
        print(f"Key {key} placed at index {index}\n")

    def display(self):
        print("Current Table:", self._slots)


# --- Classroom Example ---
# Table size of 5
my_hash = SimpleHash(5)

# Insert keys that will collide
my_hash.insert(10)  # 10 % 5 = 0
my_hash.insert(20)  # 20 % 5 = 0 -> Collision, moves to 1
my_hash.insert(7)  # 7 % 5 = 2
my_hash.insert(12)  # 12 % 5 = 2 -> Collision, moves to 3

my_hash.display()
