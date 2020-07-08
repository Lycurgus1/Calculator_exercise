# Importing parent class
from base_functions import Base_functions

# Inheriting parent class
class More_functions(Base_functions):

    # Intiliasing class
    def __init__(self):
        pass

# Creating class object and calling function
obj1 = More_functions()
obj1.divide()