def userInfo(name, lastName, age):
	return f"hello {name} {lastName} {age}"

name = input("Enter first name: ")
lastName = input("Enter last name: ")
age = input("Enter your age: ")

user = userInfo(name, lastName, age)
print(user)
