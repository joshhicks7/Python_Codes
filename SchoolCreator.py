
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + "," + str(self.age);
    
class Student(Person):
    def __init__(self, name, age = 10, grade = 3):
        super().__init__(name, age)
        self.grade = grade
    def __str__(self):
        return 'Student) ' + super().__str__() + "," + str(self.grade)

class Teacher(Person):
    def __init__(self, name, age = 30, experience = 10):
        super().__init__(name, age)
        self.experience = experience
    def __str__(self):
        return 'Teacher) ' + super().__str__() + "," + str(self.experience)

class ClassRoom:
    students = []
    def __init__(self):
        self.students = []
    def addStudent(self,student):
        self.students.append(student)
    def setTeacher(self, teacher):
        self.teacher = teacher
    def __str__(self):
        lis = '\n'
        lis = lis + str(self.teacher)
        for s in self.students:
            lis = lis + '\n' + str(s)
        return lis
    
class School:
    classRooms = []
    def __init__(self):
        pass
    def addClass(self, classroom):
        self.classRooms.append(classroom) 
    def __str__(self):
        lis = ' School'
        i = 1
        for s in self.classRooms:
            lis = lis + '\n\n Class ' + str(i) + '\n' + str(s)
            i = i+1
        return lis
        
classRoom = ClassRoom()     
        
names = ['Josh', 'John', 'Susan', 'Lerome', 'Sam', 'Kennedy']

for i in names:
    classRoom.addStudent(Student(i))
    
classRoom.setTeacher(Teacher("Mr.Simon"))    

school = School()

for i in range(0,10):    
    school.addClass(classRoom)

print(school)
