import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        list_of_numbers = (ip.split("."))
        for number in list_of_numbers:
            if (0 > int(number)) or (int(number)> 255):
                return False
        else:
                return True
    else:
        return False

if __name__ == "__main__":
    main()