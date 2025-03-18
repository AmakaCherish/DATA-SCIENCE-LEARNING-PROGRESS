from datetime import date

d_o_b = int(input('what is your year of birth?'))

# get current year from datetime module
current_year = date.today().year

age = current_year - d_o_b 

print("Your age is: ", age) #print output to user 
