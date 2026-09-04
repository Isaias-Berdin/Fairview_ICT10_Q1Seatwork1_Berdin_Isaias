from pyscript import document, display

display("Data Types:", target="div1") #this display will show the leading text along with the target (div1)


#data types and assigned values (these will NOT be shown in the webpage as there is an absence of a 'display')
name = "Isaias Miguel S. Berdin III" #this is a string
age = 15 #this is an integer
height = 162.56 #this is a floating point
countries_i_wanna_visit = ["Tokyo, Japan", "New York City, USA", "Seoul, South Korea"] #this is a list
student_type = False #this is a boolean
extras = {
    "color" : "Scarlet Red",
    "car_brand" : "Jaguar",
    "shoe_size" : 9,
    "best_friend" : "Mira Gille"
} #this is a dictionary
fav_fruits = {"Clementines", "Red Grapes", "Red Apples", "Mangoes", "Watermelons"} #this is a set
seven_days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") #this is a tuple


#the displayed elements wil show via the excecution of div1 (THESE ones will show up on the webpage)
display(type(name), target="div1")
display(type(age), target="div1")
display(type(height), target="div1")
display(type(countries_i_wanna_visit), target="div1")
display(type(student_type), target="div1")
display(type(extras), target="div1")
display(type(fav_fruits), target="div1")
display(type(seven_days_of_the_week), target="div1")


display("Get to know me!", target="div2") #this display will also show the leading text along with the target (div2). these will show the actual value of the data types, just in a different div

display(f"Name: {name}")
display(f"Current Age: {age}")
display(f"Height (in cm): ")
display(f"Countries I wanna visit:  {countries_i_wanna_visit}")
display(f"Am I a new student in OBMC?: {student_type}")
display(f"Favorite color, dream car, shoe size, best friend:")
display(extras["color"], extras["car_brand"], extras["shoe_size"], extras["best_friend"])
display(f"Favorite Fruits: {fav_fruits}")
display(f"My ranking of the days of the week (best to worst): {seven_days_of_the_week[5]}, {seven_days_of_the_week[6]}, {seven_days_of_the_week[0]}, {seven_days_of_the_week[4]}, {seven_days_of_the_week[2]}, {seven_days_of_the_week[3]}, {seven_days_of_the_week[1]} ")


def add_a_number_yuh(e):
    document.getElementById("output1").innerHTML = "" #clears prev result
    
    num1 = float(document.getElementById("input1").value) # get input value
    num2 = float(document.getElementById("input2").value) # get input value
    result1 = num1 + num2 # "+" means addition
    display(result1, target="output1") # displays output of combined variables
    result2 = num1 - num2 # "-" means subtract
    display(result2, target="output1") # displays output of combined variables
    result3 = num1 * num2 # "*" means multiplication
    display(result3, target="output1") # displays output of combined variables
    result4 = num1 / num2 # "/" means floating point division
    display(result4, target="output1") # displays output of combined variables
    result5 = num1 // num2 # "//" means floor division (quotient is rounded down)
    display(result5, target="output1") # displays output of combined variables
    result6 = num1 % num2 # "%" means remainder
    display(result6, target="output1") # displays output of combined variables
    result7 = num1 ** num2 # "**" means exponentation
    display(result7, target="output1") # displays output of combined variables