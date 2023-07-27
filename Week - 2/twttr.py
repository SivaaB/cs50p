def main():
    input_string = input("Input: ")
    input_string = input_string.strip()
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    print ("Output: ", end = '')
    for i in input_string:
        if i in vowels:
            print("", end = '')
            continue
        else:
            print(i, end = '')

main()