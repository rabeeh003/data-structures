queue = []

def enqueue():
    element = input('Enter the element : ')
    queue.append(element)
    print("element: ", element, "is added.")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        element = queue.pop(0)
        print("element: ", element, "is removed.")

def display():
    print("======= Queue =======")
    print(queue)
    print("======================")

print("----- Commands -----")
print("1. Enqueue, 2. Dequeue, 3. Display, 4. Exit")
print("--------------------")

while True:
    choice = int(input('command $ '))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")