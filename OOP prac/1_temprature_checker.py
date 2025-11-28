class TempratureChecker:
    def __init__ (self, temp):
        self.temp = temp
    def is_freezing(self):
        return self.temp <= 32
    def is_boiling(self):
        return self.temp >= 212


def main():
    while True:
        try:
            temp = int(input("Enter the temprature as a whole number (Farenheit): "))
            break
        except:
            print("Invalid input. Try again.")
        

    temp = TempratureChecker(temp)

    if temp.is_freezing():
        print("It's freezing!")
    elif temp.is_boiling():
        print("It's boiling!")
    else:
        print("Temprature is normal.")

if __name__ == "__main__":
    main()