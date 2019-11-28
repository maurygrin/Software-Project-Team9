from BinaryFile import BinaryFile


class Plugin:

    ### Initializer / Instance Attributes #######
    def __init__(self, name, description, structure, data_set):
        self.name = name
        self.description = description
        self.data_set = data_set
        self.structure = structure
