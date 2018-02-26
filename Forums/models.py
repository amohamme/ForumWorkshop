########################################
# Models
########################################

class member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return """Name: {} , Age: {}""".format(self.name, self.age)


class post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return """Title: {} , Content: {}""".format(self.title, self.content)
