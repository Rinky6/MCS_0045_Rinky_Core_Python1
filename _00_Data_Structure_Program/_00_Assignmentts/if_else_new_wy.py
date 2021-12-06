num=int(input("Enter no of subjects : "))
sub_lst=[]
marks_lst=[]
if 3 <= num <= 7:
     for i in range(1, num + 1):
       subject = input("enter the name of " + str(i) + " subject  : ")
       marks = int(input("enter the marks of " + subject + " " + "subject :"))
       if  marks >100:
        print("Please enter valid marks between 0 to 100")
       else:
        sub_lst.append(subject)
        marks_lst.append(marks)
     print(sub_lst)
     print(marks_lst)
     avg = (sum(marks_lst) / num)
     count = 0

     for i in marks_lst:
        if i >= 75.0:
         count = count + 1
     if avg >= 90:
       print("Distinction")
     elif 75<=avg<=90:
       print("Average")
     elif avg<75:
       if count > 3:
         print("Pass")
       else:
        print("Fail")


if num > 7:
    for i in range(1, num + 1):
        subject = input("Enter the name of " + str(i) + " subject  : ")
        marks = int(input("Enter the marks of " + subject + " " + "subject :"))
        if marks >= 100:
            print("Please enter valid marks between 0 to 100")
        else:
         sub_lst.append(subject)
         marks_lst.append(marks)
    print(sub_lst)
    print(marks_lst)

    avg = (sum(marks_lst) / num)
    count = 0
    avg1 = 0
    add=0
    for i in marks_lst:
        if i <= 65:
         add+=i
         count = count + 1
    avg1 = add/count
    if avg < 75:
     if 65 <= avg1 <= 75:
        print('passed')
     elif count >= 5:
         print('debarred')
     else:
        print('failed')

    elif avg >= 90:
        print("Distinction")

    elif 75 <= avg <= 90:
        print("Average")



if num < 3:
 print("Enter more than three subject")