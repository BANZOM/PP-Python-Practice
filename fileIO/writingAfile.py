'''

Writing into a file

'''

F = open("sample.txt" , "wb")
print(F.mode) #finding a mode of file
print(F.name) #getting file name

#write "Hello there"
F.write( bytearray ("Hello there", "UTF-8"))
F.close()