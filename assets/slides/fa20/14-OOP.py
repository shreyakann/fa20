class Animal:

	# Attributes: color, sound, name
	def __init__(self, color, sound, name):
		self._color=color
		self._sound=sound
		self._name=name

	def makesound(self):
		print(self._sound)

	def callName(self, name):
		if (name==self._name):
			self.makesound()

class Dog(Animal):
	
	def walk(self):
		pass #implement walk method later

class Cat(Animal):

	# Cats react differently to being called
	def callName(self, name):
		self.makesound()

mycat=Cat("black","miou","max")
mydog=Dog("brown","wow","fluffy")

mydog.makesound() # == Dog.makesound(mydog)
mycat.makesound() # == Cat.makesound(mycat)
# mycat.walk() # Error!
mycat.callName("max") # result: miou
mycat.callName("fluffy") # result: miou
mycat.callName("") # result: miou

mydog.callName("fluffy") # result: wow
mydog.callName("max") # result: 



