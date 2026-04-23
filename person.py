class person:
	name="muhammad younis"
	age=21
	def introduce(self,name,age):
		self.name=name
		self.age=age
		print("my name is ",self.name,"my age is : ",self.age)

person1=person()
print(person1.name)
print(person1.age)
person1.introduce("younis",21)