class Add:
    def __call__(self, num_list):
        return sum(num_list)

add = Add()
numbers = [1, 2, 3, 4, 5, 6]
total = add(numbers)
print(f"Total sum: {total}")
