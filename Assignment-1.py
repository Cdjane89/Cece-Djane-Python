#Section 1: Variables and Types
name="cece"
age=32
height=5.5
is_student=True

print(name, type(name))
print(age,type(age))
print(height, type(height))
print(is_student,type(is_student))


name= input("what is your name?")
age=int(input("what is your age?"))
print(f"Hi, {name}! you are aproximately {age} years old.")

#Section 3: Type Conversion and f-strings

a=float(input("enter a separate input "))
b=float(input("enter a separate input "))
total= a*b
print(f"{a} * {b} = {total}")

#Section 4: Formatted Receipt
Item="Iphone"
Price=29.99
Quantity=10
Total=Price*Quantity
print("=================================")
print("             RECEIPT")
print("=================================")
print(f"Iphone: {Item}")
print(f"Price: ${Price:.2f}")
print(f"Quantity: {Quantity}")
print("----------------------------------")
print(f"Total: ${Total:.2f}")
print("==================================")


#Section 5: Mini-Project — Profile Card

name=input("what is your name?")
Hometown=input("what is your hometown?")
Hobby=input("what is your favorite hobby?")
Fun_fact=input("what is one fun fact about you?")
birth_year=int(input("what year were you born?"))
current_year=int(input("what year is it?"))
Age=current_year-birth_year
print("╔══════════════════════════════╗")
print("      PROFILE:Cece Djane")
print("╚══════════════════════════════╝")
print(f"Hometown: {Hometown}")
print(f"Hobby: {Hobby}")
print(f"Fun_fact: {Fun_fact}")
print(f"Age: {Age}")
add assignment 1
