i = 0
while i < 10:
    i += 1
    f = open("tutorial.txt", "a")
    f.write(str(i))
    f.write("\n")
    f.close()
