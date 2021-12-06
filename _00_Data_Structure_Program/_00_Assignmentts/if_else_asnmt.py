def func1(n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input("enter the name of "+ str(i) + " subject  : ")
        marks = int(input("enter the marks of " + subject + " "+"subject :"))
        marks_dict.update({subject: marks})
        marks_list.append(marks)

    avg = (sum(marks_list)) / n

    count = 0

    for i in marks_list:
        if i >= 75.0:
            count = count + 1

    if avg >= 90.0:
        print('distinction')

    elif avg >= 75.0 and avg <= 90.0:
        print('average')

    elif avg < 75.0:
        if count <= 3:
            print('pass')
        else:
            print('failed')

    for i, j in marks_dict.items():
        print(i, ' : ', j)


def func2(n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input("enter the name of "+ str(i) + " subject  : ")
        marks = int(input("enter the marks of " + subject + " " + "subject :"))
        marks_dict.update({subject: marks})
        marks_list.append(marks)
        print(marks_list)
    avg = (sum(marks_list) / n)

    count = 0
    for i in marks_list:
        if i < 65.0:
         count = count + 1
    print("count " , count)
    if avg >= 90.0:
        print('distinction')

    elif avg >= 75.0 and avg <= 90.0:
        print('average')

    elif 65.0 <= avg <= 75.0:
            print('passed')

    elif count >= 5:
        print('debarred')

    else:
        print('failed')



    for i, j in marks_dict.items():
        print(i, ' : ', j)


number = int(input('enter the number of subjects: '))

if 3 <= number <= 7:
    func1(number)

elif number > 7:
    func2(number)

elif number < 3:
    print('enter minimum subject 3')