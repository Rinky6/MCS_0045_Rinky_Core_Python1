x = [1, 2, 3, 4]
for i in range(0, 3):
    try:
        if i == 0:
            print(y)
        elif i == 1:
            5 / 0
        else:
            x[4]

    # Multiple except blocks to handle Exceptions
    except NameError as e:
        print("Seems variable not defined")

    except IndexError as e:
        print("Index out of bound")

    except ZeroDivisionError as e:
        print("Answer is infinity")

    except:
        print("Unknown Error Caught")