from BinaryFile import BinaryFile

class Project:

    # Initializer / Instance Attributes
    def __init__(self, name, binary, description):
        self.name = name
        self.description = description
        self.binary = binary