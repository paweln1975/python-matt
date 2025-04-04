class Person:
    """
    A Person class with an instance variable, and a constructor that takes an integer, as a parameter. The constructor
    must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as,
    the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write
     the following instance methods:

    yearPasses() should increase the  instance variable by 1
    amIOld() should perform the following conditional actions:
        If age < 13, print You are young..
        If age >= 13 and age < 18, print You are a teenager..
        Otherwise, print You are old..
    """
    
    def __init__(self, initial_age):

        if initial_age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initial_age

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")