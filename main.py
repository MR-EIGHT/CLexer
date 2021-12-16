code = open("hello.c", mode='r')

for line_no, line in enumerate(code.readlines()):
    if line.strip() != "":
        print(str(line_no) + " " + line)
