#finding grade for different values of marks between 0.0 and 1.0
number = float(input("Enter a number: "))
if number >=0.9 and number <=1:
    print("grade A")
elif number >=0.8 and number <0.9:
    print("grade B")
elif number >=0.7 and number <0.8:
    print("grade c")
elif number >=0.6 and number <0.7:
    print("grade D")
elif number <0.6 and  number >= 0.0:
    print("grade F")   
else:
    print("Bad result")
    