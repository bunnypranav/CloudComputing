import requests

e = input("Enter Equation: ")
url = f"https://newton.now.sh/api/v2//simplify/{e}"

data = requests.get(url).json()
print(data)

print("Operation to be performed: " + data["operation"])
print("Expression to be performed: " + data["expression"])
print("Result to be performed: " + data["result"])
