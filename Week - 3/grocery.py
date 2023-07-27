grocery = {}
while True:
    try:
        item = input().upper().strip()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] = grocery[item] + 1
    except EOFError:
        sorted_dict = dict(sorted(list(grocery.items())))
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ")
        break
    except KeyError:
        pass