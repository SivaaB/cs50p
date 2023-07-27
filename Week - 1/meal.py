def main():
    time = input ("Enter Time: ")
    time = convert(time)

    if (7.0 <= time <= 8.0):
        print("breakfast time")
    elif (12.0 <= time <= 13.0):
        print ("lunch time")
    elif (18.0 <= time <= 19.0):
        print ("dinner time")
    else:
        print ("")

def convert(time):
    time = time.split(":")
    time[1] = int(time[1])/60
    time = time[1] + int(time[0])
    return time


if __name__ == "__main__":
    main()