print('Conditional Execution - Exercise 1 solution\n')
hours = input('Enter hours? ')
rate = input('Enter rate? ')
try:
    hours = int(hours)
    rate = float(rate)
    if hours >= 40:
        pay = (hours * rate) + 25
        print('Payment Overtime=', pay)
    else:
        pay = hours * rate
        print('Payment without overtime=', pay)
    print()
except:
    print('Error, please enter a number')

print('Conditional Execution - Exercise 2 solution\n')
score = input('Enter score? ')
try:
    score = float(score)
    if score  >= 0.9 and score <= 0.99:
        print('A')
    elif score >= 0.8 and score <=0.89:
        print('B')
    elif score >= 0.7 and score <=0.79:
        print('C')
    elif score >= 0.6 and score <=0.69:
        print('D')
    elif score < 0.6:
        print('F')
    else:
        print('Bad score')
except:
    print('Bad score')