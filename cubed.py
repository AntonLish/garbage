"""cubed.py"""
x = input("введіть число: ")
x = int(x)

try:
	def function(x):
	        return x**3

except (ValueError, TypeError, NameError):
	print("Only integer")

print(function(x))
