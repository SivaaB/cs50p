def main():
    answer = input ("The Answer to the Great Question of Life, the Universe and Everything? ")
    answer = answer.upper().strip()
    if ((answer == "42") or (answer == "FORTY-TWO") or (answer == "FORTY TWO")):
        print ("Yes")
    else:
        print ("No")
main()