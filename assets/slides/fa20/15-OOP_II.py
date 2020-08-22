class Animal:
	# properties: sound, name, color
	def __init__(self, sound, name, color):
		self._sound=sound
		self._name=name
		self._color=color

	def makesound(self):
		print(self._sound)

	def callName(self,name):
		if (self._name==name):
			self.makesound()

class Cat(Animal):
	def callName(self,name):
		self.makesound()

class Dog(Animal):
	def walk(self):
		pass

mycat=Cat("miow","Kaleesi","gray")
mydog=Dog("wow","khal drogo","black")

mycat.makesound() # miow # == Cat.makesound(mycat)
mydog.makesound() # wow  # == Dog.makesound(mydog)

mydog.callName("khal drogo") # wow
mydog.callName("whatever")   # No response

mycat.callName("whatever") # miow
mydog.walk() ## do nothing
#mycat.walk() ## Error!


