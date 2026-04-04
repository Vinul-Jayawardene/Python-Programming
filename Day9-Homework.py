x=open(r"C:\Users\HP\Desktop\my_pynote.txt", "w")
x.write("Python is easy\n")
x.write("Python is powerful\n")
x.write("Python is popular\n")
x.close()

x=open(r"C:\Users\HP\Desktop\my_pynote.txt", "r")
print(x.read())
x.close()

x=open(r"C:\Users\HP\Desktop\my_pynote.txt", "r")
for line in x:
    if line.startswith("Python"):
        print(line)
x.close()

x=open(r"C:\Users\HP\Desktop\my_pynote.txt", "a")
x.write("Python is fun to learn")
x.close()

x=open(r"C:\Users\HP\Desktop\my_pynote.txt", "r")
print(x.read())
print(x.mode)
x.close()
