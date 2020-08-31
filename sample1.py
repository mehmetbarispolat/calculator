class Calculator():
    def __init__(self,firstNumber,secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
    def addition(self):
        return self.firstNumber + self.secondNumber
    def multiplication(self):
        return self.firstNumber * self.secondNumber
    def division(self):
        return self.firstNumber / self.secondNumber
    def subtraction(self):
        return self.firstNumber - self.secondNumber

def inputChooseScreen():
    chosenInput = int(input("Please choose a operation \n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n"))  
    return chosenInput

def chosenOperation(chosenInput,numInput1,numInput2):
    student = Calculator(numInput1,numInput2)
    if chosenInput == 1:
        return student.addition()
    elif chosenInput == 2:
        return student.subtraction()
    elif chosenInput == 3:
        return student.multiplication()
    elif chosenInput == 4:
        return student.division()
    else:
        return "Please enter a valid number"
    
    
if __name__ == '__main__':
    numInput1 = float(input("Please enter a number to calculate\n"))
    numInput2 = float(input("Please enter a number to calculate\n"))
    chosenInput = inputChooseScreen()
    result = chosenOperation(chosenInput,numInput1,numInput2)
    print("Sonuç: {}".format(result))