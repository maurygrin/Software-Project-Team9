class Plugin:

    # Initializer / Instance Attributes
    def __init__(self, name, description, structure, data_set):
        self.__name = name
        self.__description = description
        self.__data_set = data_set
        self.__structure = structure

    # Returns the plugin name
    def get_name(self):
        return self.__name

    # Returns the plugin description
    def get_description(self):
        return self.__description

    # Returns the plugin structure
    def get_structure(self):
        return self.__structure

    # Returns the plugin data set
    def get_dataset(self):
        return self.__data_set
