
try:
    file1= open('sample.txt','r')
    read_file = file1.readline()
    read_file1 = file1.readline()
    print('Reading the file content :')
    print('Line 1: ', read_file)
    print('Line 2: ', read_file1)
    file1.close()

except FileNotFoundError:
    print("Error : the file 'sample.text' was not found")





