def main():
    input_string = str(input("Greeting: "))
    output = str(value(input_string))
    print("$" + output)


def value(greeting):
    output = 0
    greeting = greeting.upper().strip()
    if (greeting == "HELLO") or greeting.startswith("HELLO"):
        output = 0
        return output
    elif (greeting[0] == "H"):
        output = 20
        return output
    else:
        output = 100
        return output

if __name__ == "__main__":
    main()