student = {}

while True:
  print("\n ---------STUDENT MANAGER APP--------")
  print("1. Add Student")
  print("2. view Student")
  print("3. check result")
  print("4. exit ")

  choice = input("enter your choice: ")


  # add student
  if choice == "1":
    name = input("enter student name: ")
    marks = int(input("enter marks: "))
    student[name] = marks
    print(f"{name} successfully added!")


    # view students
  elif choice == "2":
    if not student:
      print("no student found!")

    else:
      for name, marks in student.items():
        print(name, ":", marks)

    # check result
  elif choice == "3":
    name = input("enter student name: ")

    if name in student:
      mark = student[name]

      if marks >= 40:
        print("PASS")

      else:
        print("FAIL")

    else:
      print("student not found")


  elif choice =="4":
    print("exiting....")
    break

  else:
    print("invalid input")



