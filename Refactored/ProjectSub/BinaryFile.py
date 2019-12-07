class BinaryFile:

    # Initializer / Instance Attributes
    def __init__(self, path, metadata):
        self.__path = path
        self.__metadata = metadata

    # Returns the binary file path
    def get_path(self):
        return self.__path

    # Returns the instance of metadata
    def get_metadata(self):
        return self.__metadata
