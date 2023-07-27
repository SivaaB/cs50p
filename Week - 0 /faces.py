def main():
    str1 = input("Enter String: ")
    str1 = convert (str1)
    print (str1)

def convert (str):
    str = str.replace (":)", "🙂")
    str = str.replace (":(", "🙁")
    return str

main()