class Calculator:
    def __init__(self, opcodes: list, operators=None: list):
        self.opcodes = opcodes
        self.operators = operators if operators is not None else []
   def __str__(self) -> str:
        pass
   def optimise(self):
        for operator in self.operators:
            self.opcodes = operator.process(self.opcodes)

    def validate(self) -> bool:
        pass

