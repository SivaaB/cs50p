def main():
    greeting = input ("Greeting: ")
    greeting = greeting.upper().strip()
    if (greeting == "HELLO") or greeting.startswith("HELLO"):
        print ("$0")
    elif (greeting[0] == "H"):
        print ("$20")
    else:
        print ("$100")
main()