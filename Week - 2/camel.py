def main():
    word = input ("Camel-Case: ")

    print ("Snake-Case: ", end= '')
    for c in word:
        if c.islower():
            print (c , end='')
        else:
            print ('_' + c.lower(), end= '')
    print('')
main()