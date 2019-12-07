class Project:

    # Initializer / Instance Attributes
    def __init__(self, name, binary, description):
        self.__name = name
        self.__binary = binary
        self.__description = description

    # Returns the project name
    def get_name(self):
        return self.__name

    # Returns the binary instance
    def get_binary(self):
        return self.__binary

    # Returns the project description
    def get_description(self):
        return self.__description
