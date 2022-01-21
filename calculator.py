from enum import Enum

# Diagnostic #3
# Complete the implementation of the CalculatorPacket class; specifically the perform_calculation method

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

class CalculatorPacket:
    def __init__(self, _operator, _operand_A, _operand_B):
       self.operator=_operator
       self.A=_operand_A
       self.B=_operand_B

    #Perform the calculation inputting into the object. If the calculation is invalid, return None
    def perform_calculation(self):
        oper = self.operator
        num_1 = self.A
        num_2 = self.B
        if oper == Operation.ADD:
            return (num_1 + num_2)
        if oper == Operation.SUBTRACT:
            return (num_1 - num_2)
        if oper == Operation.MULTIPLY:
            return (num_1 * num_2)
        if oper == Operation.DIVIDE:
            return (num_1 / num_2)
        else:
            return "None"






if __name__=="__main__":

    print('We are going to perform some calculations')

    calcA = CalculatorPacket(Operation.ADD,3,5)
    print('Result should be 8. You calculated: '+ str(calcA.perform_calculation()))

    calcB = CalculatorPacket(Operation.SUBTRACT, -7, 52)
    print('Result should be -59. You calculated: ' + str(calcB.perform_calculation()))

    calcC = CalculatorPacket(Operation.MULTIPLY, -10, -7)
    print('Result should be 70. You calculated: ' + str(calcC.perform_calculation()))

    calcD = CalculatorPacket(-1, 3, 5)
    print('Result should be None. You calculated: ' + str(calcD.perform_calculation()))