class Metadata:

    # Initializer / Instance Attributes
    def __init__(self, arch, os, binaryType, machine, classVariable, bits, language, canary,
                 endian, crypto, nx, pic, relocs, stripped, type):
        self.arch = arch
        self.os = os
        self.binaryType = binaryType
        self.machine = machine
        self.classVariable = classVariable
        self.bits = bits
        self.language = language
        self.canary = canary
        self.endian = endian
        self.crypto = crypto
        self.nx = nx
        self.pic = pic
        self.relocs = relocs
        self.stripped = stripped
        self.type = type
