from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
        try:
            dob = input ("Date of Birth: ")
            difference = operator.sub(date.today(), date.fromisoformat(dob))
            print(convert(difference.days))
        except ValueError:
             print ("Invalid Date")
             sys.exit()

def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()