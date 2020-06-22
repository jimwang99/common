import enum
import math
import random
import cocotb.binary

class BinaryValue(cocotb.binary.BinaryValue):
    def __init__(self, n_bits, binaryRepresentation):
        assert binaryRepresentation in [0, 2]
        super().__init__(value=0, n_bits=n_bits, bigEndian=False, binaryRepresentation=binaryRepresentation)

    @property
    def vhex(self):
        nhex = math.ceil(self.n_bits/4)
        shex = (f'%{nhex}s' % hex(self.integer)[2:]).replace(' ', '0')
        return f"{self.n_bits}'h{shex}"

    def rand(self):
        if (self.binaryRepresentation == 0):
            self.integer = random.randint(0, pow(2, self.n_bits))
        else:
            self.integer = random.randint(-1*pow(2, self.n_bits-1), pow(2, self.n_bits-1))


class Int32(BinaryValue):
    def __init__(self):
        super().__init__(self, 32, 2)


class UInt32(BinaryValue):
    def __init__(self):
        super().__init__(self, 32, 0)
