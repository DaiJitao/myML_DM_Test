

data = {}
data["name"] = "dai"

data["grade"] = "122"

print(data.get("name", None))

class Person():
    def __init__(self, name):
        self.name = name

    def test(self):
        print("test")

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
    def mm(self):
        super().test()
email = EmailPerson("ddai", "976@aaa")
email.mm()