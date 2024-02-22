# check its palindrome
def palindrome():
    value = str(input("Ender word to check palindrome : "))
    r_value = value[::-1]
    if value.lower() == r_value.lower():
        print("its a palindrome.\n")
    else:
        print("its not palindrome.\n")

def word_revise():
    value = str(input("Enter a sentence for revise : "))
    separated = value.split(' ')
    separated = separated[::-1]
    re_value = ''
    for i in separated:
        re_value += i
        re_value += ' '
    print(re_value)


print("------------ String ------------")
print("""
    1. Palindrome,       2. Revise,         3. Word revise,        4. Exit
""")
print('--------------------------------')

while True:
    choice = int(input("command $ "))
    if choice == 1:
        palindrome()
    elif choice == 2:
        value = str(input("Ender word for revise : "))
        print(value[::-1],'\n')
    elif choice == 3:
        word_revise()
    elif choice == 4:
        break
    else:
        print("command not fount !\n")