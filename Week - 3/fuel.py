def main():
    while True:
        try:
            frac = input("Fraction: ")

            frac = frac.split("/")
            x = int(frac[0])
            y = int(frac[1])

            if (x <= y):
                percent = round((x / y) * 100)
                if (1 < percent < 99):
                    print (percent, end = "")
                    print ("%")
                    break
                elif (percent <= 1):
                    print ("E")
                    break
                elif (percent >= 99):
                    print ("F")
                    break
            else:
                pass

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()