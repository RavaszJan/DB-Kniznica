
class Author:

    def __init__(self,ID,name,text):
        self.ID=ID
        self.name=name
        self.text=text

    def __str__(self):
        return f'ID Author{self.ID}\nMeno:{self.name} \nBio:{self.text}'