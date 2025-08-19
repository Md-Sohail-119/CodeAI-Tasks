with open("students.txt", "w") as file:
    file.write("Alice,85 \n")
    file.write("Bob,90 \n")
    file.write("Sohail,75 \n")
    file.write("David,88 \n")
    file.write("Poornam,70 \n")

with open("students.txt") as file:
    for line in file:
        name, marks = line.split(",")
        if int(marks) > 80:
            print(name)
