class Metadata:

    # Initializer / Instance Attributes
    def __init__(self, arch, os, binaryType, machine, classVariable, bits, language, canary,
                 endian, crypto, nx, pic, relocs, stripped, type):
        self.__arch = arch
        self.__os = os
        self.__binaryType = binaryType
        self.__machine = machine
        self.__classVariable = classVariable
        self.__bits = bits
        self.__language = language
        self.__canary = canary
        self.__endian = endian
        self.__crypto = crypto
        self.__nx = nx
        self.__pic = pic
        self.__relocs = relocs
        self.__stripped = stripped
        self.__type = type

    # Returns the binary arch
    def get_arch(self):
        return self.__arch

    # Returns the binary os
    def get_os(self):
        return self.__os

    # Returns the binary type
    def get_binaryType(self):
        return self.__binaryType

    # Returns the binary machine
    def get_machine(self):
        return self.__machine

    # Returns the binary class
    def get_classVariable(self):
        return self.__classVariable

    # Returns the binary bits
    def get_bits(self):
        return self.__bits

    # Returns the binary language
    def get_language(self):
        return self.__language

    # Returns the binary canary
    def get_canary(self):
        return self.__canary

    # Returns the binary endian
    def get_endian(self):
        return self.__endian

    # Returns the binary crypto
    def get_crypto(self):
        return self.__crypto

    # Returns the binary nx
    def get_nx(self):
        return self.__nx

    # Returns the binary pic
    def get_pic(self):
        return self.__pic

    # Returns the binary relocs
    def get_relocs(self):
        return self.__relocs

    # Returns the binary stripped
    def get_stripped(self):
        return self.__stripped

    # Returns the binary extension
    def get_type(self):
        return self.__type