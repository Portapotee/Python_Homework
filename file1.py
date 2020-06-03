def fileread(filename):
    file1 = open(filename)
    text = file1.read()
    file1.close()
    return text

def filewrite(filename,line):
    file1 = open(filename,'r+')
    file1.write(f"\nprint('{line}')")
    file1.close()

if(__name__ == '__main__'):
    print(fileread("random.txt"))
    filewrite("random.txt","hello there")