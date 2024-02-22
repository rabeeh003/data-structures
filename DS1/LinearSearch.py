def position_search(values):
    val = input("Typing... : ")
    t = False
    for i in range(len(values)):
        if values[i] == val:
            print("the value find in ",i,' th position. \n')
            t = True
    if t == False:    
        print('Value not fount in list. \n')

def search(values):
    ser = input('Typing... : ')
    for i in range(len(values)):
        if values[i] == ser:
            print(ser,' is on this list. \n')
            break
    else:
        print('Invalid search.\n')

def string_search():
    print("----- The letter search in a paragraph -----")
    sent = input("Enter a paragraph :")
    print("----- 1. for search,  2. for exit -----")
    while True:
        task = int(input('take task : '))
        if task == 1:    
            letter = input("Search letter : ")
            pos = []
            for i in range(len(sent)):
                if letter == sent[i]:
                    pos.append(i+1)
        
            if pos:
                print("Positions : ",pos,'\n')
            else: 
                print("sorry not font \n")
        elif task == 2:
            break
        else:
            print("Invalid task ! \n")




print("--------- Linear Search --------")
x = int(input("Enter your list width : "))
values = []
for i in range(x):
    val = input(f"Enter value {i + 1}: ")
    values.append(val)
print("----------------------")
print("----search started----")
print("1. Search,   2. Position search,  3. Letter search in string,   4. Exit")
while True:
    sel = int(input("select program : "))
    if sel == 1:
        search(values)
    elif sel == 2:
        position_search(values)
    elif sel == 4:
        break
    elif sel == 3:
        string_search()
    else:
        print("invalid command ! \n")