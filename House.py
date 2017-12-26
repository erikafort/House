'''Erika Fortune
September 26,2017
Purpose: This program is used to provide a customer with the correct total square feet of their house and the amount of gallons of paint they should buy depending on the dimensions they plug in.
'''

#Dimensions
print("Printing footgae Calculator, please enter values to compute. Enter width:")
num1=int(input())
print("enter length:")
num2=int(input())
print("enter height:")
num3=int(input())
print("enter gable height:")
num4=int(input())
num5=2*(num1*num3)+2*(num2*num3)+2*(.5*(num4*num1))
num6=int((num5)/400)
str1="Total square feet of the house:"
str4="Total amount of gallons needed:"
str2=str(num5)
str5=str(num6+1)
print(str1 + str2)
str3=(str4+str5)
print(str3)

