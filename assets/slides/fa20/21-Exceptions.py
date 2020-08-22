try:
	age=input("What is your age:")
	assert int(age)>0, "Dude, negative age, really?"
	ageindays=int(age)*365
	print("your age in days:",ageindays)
except AssertionError:
	print("Need an age >0")
except:
	print("Need a valid age")
