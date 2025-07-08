class Student:
    def __init__(self, name):
        self.name = name
        self.Notebook = self.Notebook()

    def print_info(self):
        return f'{self.name} => {Student.Notebook.model(self)}, {Student.Notebook.core_name(self)}, {Student.Notebook.core(self)}'

    class Notebook:
        def model(self):
            return "HP"

        def core_name(self):
            return "i7"

        def core(self):
            return "16"


st1 = Student('Roman')
st2 = Student('Vladimir')
print(f'{st1.print_info()}')
print(f'{st2.print_info()}')
