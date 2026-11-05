
database = [
    {
    "name": "Bogdan",
    "password": "221221",
    "grades": [2,3,1,2,4,5,9,1]
    },
    {
        "name": "Nazar",
        "password": "332233",
        "grades": [3,2,12,7,11,9,8,7]
    },
    {
        "name": "Yura",
        "password": "442134",
        "grades": [4,2,3,9,11,12,1]
    },
    {
        "name": "Denis",
        "password": "123456",
        "grades": [9,12,2,7,5,11,3]
    }
]

login_name = input("Enter your name: ")
login_password = input("Enter your password: ")

found = False

for user in database:
    if user["name"] == login_name and user["password"] == login_password:
        found = True
        print("You logged in successfully!")
        print("Your grades:")
        good_grades = 0
        bad_grades = 0
        for grade in user["grades"]:
            print(grade)
            if 5 <= grade <= 12:
                good_grades += 1
            elif 1 <= grade <= 4:
                bad_grades += 1
        print("Good grades:" , good_grades)
        print("Bad grades:" , bad_grades)
        break

if found == False:
    print("Uncorrect login or password!")

