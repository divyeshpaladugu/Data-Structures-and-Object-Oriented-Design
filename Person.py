"""Example demonstrating inheritance. Class diagrams:
                +----------+
                | Person   | <--- class name
                +----------+
                | name     | <--- instance variables
                | age      |
                | courses  |
                +----------+
                | __init__ | <--- instance methods
                | __str__  |
                +----------+
         +---------+  +--------+
         |                     |
         v                     v 
+------------------+    +---------------+
| Student          |    | Professor     |
+------------------+    +---------------+
| graduating_class |    | starting_year |
+------------------|    | title         |
| __init__         |    +---------------+ 
+------------------+    | __init__      |
                        +---------------+

Student and Professor both inherit __str__ directly.

Because they overload init to add class-specific variables,
they have to explicitly call super().__init__ to get the basic
variables (name, age, courses) attached.
"""

class Person:
    """Parent class for different types of People in the University
    system"""

    def __init__(self, name, age, course_list=None):
        """Constructor method - called when new Person objects are
        created."""
        self.name = name
        self.age = age
        self.courses = course_list if course_list is not None else []

        # Ternary if statement equivalent:
        # if course_list is not None:
        #     self.courses = course_list
        # else:
        #     self.courses = []

    def __str__(self):
        """Returns a string representation of this object designed to be read
        by humans."""
        return f"{self.__class__.__name__}: {self.name}"

class Student(Person):
    """Factory for generating student objects"""

    def __init__(self, name, age, graduating_class, course_list=None):
        """Constructor method - called when a new Student object is created
        and attaches instance variables to it"""
        super().__init__(name, age, course_list) # call parent class' init
        self.graduating_class = graduating_class

    
class Professor(Person):
    """Factory for generating professor objects"""

    def __init__(self, name, age, starting_year, title, course_list=None):
        """Constructor method - called when a new Professor object is created
        and attaches instance variables to it"""
        super().__init__(name, age, course_list) # call parent class' init
        self.starting_year = starting_year
        self.title = title

s1 = Student("Jake", 33, 2012)
p1 = Professor("Jake", 33, 2019, "Assistant Professor in Residence")
print(s1)
print(p1)

# Understanding check - is s1 a Student? a Professor? A Person?
print(isinstance(s1, Student))
print(isinstance(s1, Professor))
print(isinstance(s1, Person))

# Understanding check - is p1 a Student? a Professor? A Person?
print(isinstance(p1, Student))
print(isinstance(p1, Professor))
print(isinstance(p1, Person))