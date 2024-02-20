queue = []

def enqueue(item):
    queue.append(item)

def dequeue():
    if not is_empty():
        return queue.pop(0)
    else:
        print("Queue is empty")
        return None

def is_empty():
    return len(queue) == 0

def peek():
    if not is_empty():
        return queue[0]
    else:
        print("Queue is empty")
        return None

def size():
    return len(queue)

if __name__ == "__main__":
    n = int(input("Enter the number of elements to enqueue onto the queue: "))
    print("Enter the elements to enqueue onto the queue:")
    for _ in range(n):
        item = input()
        enqueue(item)

    print("Queue:", queue)

    print("Peek the front element:", peek())

    print("Dequeue:", dequeue())

    print("Queue after dequeue:", queue)

    print("Is queue empty?", is_empty())

    print("Size of queue:", size())
