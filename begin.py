class SelfIntroduction:
    def _init_(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def introduce(self):
        introduction = f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.occupation}. Nice to meet you!"
        return introduction

# Replace these with your own details
name = "prakash"
age = 20
occupation = "student"

intro_object = SelfIntroduction(name, age, occupation)
introduction = intro_object.introduce()
print(introduction)