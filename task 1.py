x = input("enter 1 for adision\n 2 for substraction\n 3 for multiplication \n 4 for division\n 5 for camparison\n 6 to find %\n 7 for squer")

if x == str(7):
     f = input("enter your squaring number")
     s = 0
else:
    f = input("enter your first number")
    s = input("enter your first number")




class Calculate:
    def __init__(self, num1, num2, task):
        self.num1 = num1
        self.num2 = num2
        self.task = task

    def addition(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def greater(self):
        if self.num1 > self.num2:
            return f"{self.num1} is greater"
        elif self.num1 <self.num2:
            return f"{self.num1} is lesser"
        elif self.num1 == self.num2:
            return f"both the numbers are equel"

    def persentage(self):
        return self.num1 % self.num2

    def squar(self):
        return self.num1 **2

    def __str__(self):
        if self.task == str(1):
            ans = self.addition()
        elif self.task == str(2):
            ans = self.sub()
        elif self.task == str(3):
            ans = self.multi()
        elif self.task == str(4):
            ans = self.div()
        elif self.task ==str(5):
            ans = self.greater()
        elif self.task ==str(6):
            ans = self.persentage()
        elif self.task ==str(7):
            ans = self.squar()
        else:
            return f"please enter a valid number"
        return f" result = {ans}"


a = int(f)
b = int(s)

r = Calculate(num1=a, num2=b, task=x)
print(r)
