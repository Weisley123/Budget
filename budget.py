#Ask the user to input their hourly wage and monthly expenses.
wage=float(input("Please enter your hourly wage in dollars per hour."))
rent=float(input("Please enter your monthly rent."))
internet=float(input("Please enter your monthly internet service expense."))
grocery=float(input("Please enter your monthly grocery expense."))
leisure=float(input("Please enter your monthly leisure expense."))

#Calculate total monthly and weekly expenses. 
total_month=float(rent+internet+grocery+leisure)
total_week=total_month/4

#Calculate how many hours the user needs to work to cover their expenses/ save 100 a month.
import math
hours_even=math.ceil(total_week/wage)
hours_hundred=math.ceil((total_week+25)/wage)

#Display wage, monthly expenses, total monthly expenses, hours per week to break even, and hours per week to save 100 dollars a month.
print("Your hourly wage is "+str(wage)+" dollars per hour.")
print("Your monthly rent is "+str(rent)+" dollars.")
print("Your monthly internet service fee is "+str(internet)+" dollars.")
print("Your monthly grocery expense is "+str(grocery)+" dollars.")
print("Your monthly leisure expense is "+str(leisure)+" dollars.")
print("Your total monthly expenses are "+str(total_month)+" dollars.")
print("You will need to work "+str(hours_even)+" hours a week in order to cover all monthly expenses.")
print("You will need to work "+str(hours_hundred)+" hours a week in order to cover all monthly expenses and save an additional 100 dollars a month.")

#To test my code I used the values: wage=15.5, rent=700, internet service=100, groceries=250, and leisure=100
#I added all the expenses: 700 + 100 + 250 + 100 = 1,150 dollars, divided by four is 287.5 dollars per week
#Next, I divided 287.5 by 15.5 (wage) to get 19 (after rounding), lastly I added 25 to 287.5 and divided by 15.5 to represent an additional 100 dollars per month, which equals 21 hours
#My program gave the same result. This result makes sense because each step is a direct operation on the inputs which produces the real-world outputs of how many hours you need to work.
#While I was writing the code I was thinking the project was very easy and repetative; naming variables, printing text, making calculations was all easy to me.
#What was more difficult was correcting my code to get the program to produce the output I wanted. For example it took some time for me to learn how to round up when calculating the number of hours needed to work.