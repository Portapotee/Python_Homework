# A class defines specific things, but a function does specific things (the function is the code while the class defines what the function is doing)

# lastname = str
# firstname = str 
# grade = int
# courses = list

# __init__(book:dict)
# __repr__()

class student:
    
    def __init__(self, lastname, firstname, grade, courses, book):
        self.lastname = lastname
        self.firstname = firstname
        self.grade = grade
        self.book = book
        self.courses = courses

    
    def __repr__(self):
        return(self.lastname + ',' + self.firstname + ':' + '\t grade:' + str(self.grade) + '\t courses:' + str(self.courses) + '\t books:' + str(self.book))

    # def addCourse(self, Course):
    #     self.list.append(Course)

    def printAll(self):
        print(self)



student1courses = ["science", "math", "ELA"]
student2courses = ["ELA", "art", "band"]

student1books = {'ELA': '6th grade ELA', 'math': 'math basics', 'science': 'middle school science'}
student2books = {'art textbook': 'the basics of art'}
  
student1 = student("wang", "bryan", 6, student1courses, student1books)
student2 = student("lastname", "firstname", 7, student2courses, student2books)



student1.printAll()