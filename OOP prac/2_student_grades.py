class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, score):
        self.grades.append(score)
    def is_passing(self):
        return sum(self.grades)/len(self.grades) >= 70
    

def main():
    while True:
        try:
            name = str(input("Enter student's name: "))
            break
        except:
            print("Please enter a valid name.")

    student = Student(name)
        
    get_scores(student)
    
    if student.is_passing():
        print(f"{student.name} is passing")

    else:
        print(f"{student.name} is not passing.")
        

def get_scores(student):
    while True:
        score = input("Enter student's score (Type 'done' to stop):\n")
        if score == "done":
            break
        try:
            score = int(score)
            
            if score in range(0,101):
                student.add_grade(score)
            else:
                print("Invalid. Score must be 0-100.")
                continue
        except:
            print("Must be a valid number 0 through 100.")



if __name__ == "__main__":
    main()


