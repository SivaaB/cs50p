def main():
    input_string = input("Input: ")
    output = str(shorten(input_string))
    print ("Output : ", + output)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    shortened_text = []
    for i in input_string:
        if i not in vowels:
            shortened.append(i)
    output = str("".join(shortened_text))
    return output

if __name__ == "__main__":
    main()