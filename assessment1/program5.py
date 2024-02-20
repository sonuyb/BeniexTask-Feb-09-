stack = []

def push(item):
    stack.append(item)

def pop():
    if not is_empty():
        return stack.pop()
    else:
        print("Stack is empty")
        return None

def is_empty():
    return len(stack) == 0

def peek():
    if not is_empty():
        return stack[-1]
    else:
        print("Stack is empty")
        return None

def size():
    return len(stack)

if __name__ == "__main__":
    n = int(input("Enter the number of elements to push onto the stack: "))
    print("Enter the elements to push onto the stack:")
    for _ in range(n):
        item = input()
        push(item)

    print("Stack:", stack)

    print("Peek the top element:", peek())

    print("Pop:", pop())

    print("Stack after pop:", stack)

    print("Is stack empty?", is_empty())

    print("Size of stack:", size())
