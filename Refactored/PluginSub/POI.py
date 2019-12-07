class POI:

    # Initializer / Instance Attributes
    def __init__(self, name, typeP, output):
        self.__name = name
        self.__typeP = typeP
        self.__out = output

    # Returns the POI name
    def get_name(self):
        return self.__name

    # Returns the POI type
    def get_typeP(self):
        return self.__typeP

    # Returns the POI output
    def get_out(self):
        return self.__output
