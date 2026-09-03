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

display(">-Name:-<", name)
display(">Current Age:<", age)
display(">Height (in cm):<", height)
display(">Countries I wanna visit:<", countries_i_wanna_visit[0], countries_i_wanna_visit[1], countries_i_wanna_visit[2])
display(">Am I a new student in OBMC?:<", student_type)
display(">Favorite color, dream car, shoe size, best friend:<")
display(extras["color"], extras["car_brand"], extras["shoe_size"], extras["best_friend"])
display(">Favorite Fruits:<", fav_fruits)
display(">My favorite day of the week:<", seven_days_of_the_week[5])
