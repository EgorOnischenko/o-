line_count2 = 0
line_count1 = 0
with open("2.txt", 'r', encoding="utf8") as file2:
    for line2 in file2:
        if line2 != "\n":
            line_count2 += 1

    with open("1.txt", 'r', encoding="utf8") as file1:
        for line1 in file1:
            if line1 != "\n":
                line_count1 += 1
        lines = file1.readlines()
        for line_1 in lines:
            print(line_1)


    with open("3.txt", 'w', encoding="utf8") as file:
        file.write(file2.name)
        file.write("\n")
        file.write(str(line_count2))
        file.write("\n")
        file.write(line2)
        file.write("\n")
        file.write(file1.name)
        file.write("\n")
        file.write(str(line_count1))
        file.write("\n")
        file.write(line_1)


