"""

Requirement :
1. CRUD   Create,Retrieve,Update,Delete
2. Datatype
3. State, Behavior

"""



# State  --> Variables
student_info = {12345: ['RINKY', '10th', 90, 'ATP'],
                43232: ['SHYAMA', '10th', 85, 'CHR'],
                42422: ['RAMA', '10th', 34, 'KRN']
                }
print("-----------------------")
# Behavior --> Functions
for sid, sinfo in student_info.items():
    marks = sinfo[2]
    if marks >= 70 and marks <= 100:
        print(sid, " grade is : ", " A")
    elif marks >= 60 and marks < 70:
        print(sid, " grade is : ", " B")
    elif marks >= 50 and marks < 60:
        print(sid, " grade is : ", " C")
    elif marks >= 35 and marks < 50:
        print(sid, " grade is : ", " D")
    else:
        print(sid, " grade is : ", " Fail")
