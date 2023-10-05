# Writing to a text file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')

# Reading from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
        
        
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    
# Write a new line to text file "a" is append

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    
    
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    
    
with open('Example2.txt', 'a+') as testwritefile: #The open() function is used to open a file named Example2.txt in append plus read mode (a+). If Example2.txt does not exist, it will be created. The file is referenced by testwritefile within the block.
    print("Initial Location: {}".format(testwritefile.tell()))#tell() returns the current file cursor position. Initially, since the file is opened in append mode, the cursor is at the end of the file.
    
    data = testwritefile.read() #Attempts to read the file, but since the cursor is at the end, nothing is read. Thus, 'Read nothing' is printed.
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # seek() moves the file cursor to a specified position. Here, it's moved to the beginning of the file (0 bytes from the beginning).
    
    print("\nNew Location : {}".format(testwritefile.tell())) #Prints the new cursor position which is now at the beginning of the file.
    data = testwritefile.read()#Attempts to read the file again. This time, since the cursor is at the beginning, it reads the file contents and prints them.
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )#Prints the cursor position after reading. It will be at the end of whatever data was read.
    #This script demonstrates how the file cursor's position affects reading from a file, and how you can use seek() to move the cursor to different positions within the file, and tell() to know the current position of the cursor in the file.



with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate() #To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
    testwritefile.seek(0,0)
    print(testwritefile.read())

# 

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
                
                
# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())