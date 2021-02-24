class SmartCalculator:

    def __init__(self):
        self.operators = ('+', '-')
        self.memory = dict()

    @staticmethod
    def help():
        print("The program calculates the sum of numbers")

    @staticmethod
    def valid_identifier(identifier):
        return all(True if i.isalpha() else False for i in identifier)

    @staticmethod
    def valid_assignment(identifier):
        return all(True if i.isdigit() else False for i in identifier)

    @staticmethod
    def check_brackets(expr):
        queue = list()
        for i in expr:
            if i == '(':
                queue.append(i)
            elif i == ')':
                try:
                    queue.pop()
                except IndexError:
                    queue.append(-1)
                    break
        return True if not queue else False

    def check_command(self, command):
        if command == '/exit':
            print("Bye!")
            exit(0)
        elif command == '/help':
            self.help()
        else:
            print("Unknown command")

    def check_assignment(self, expression):
        expr = [i.strip() for i in expression.split('=')]
        if len(expr) == 2:
            if not self.valid_identifier(expr[0]):
                print("Invalid identifier")
            elif not self.valid_assignment(expr[1]) and expr[1] not in self.memory:
                print("Invalid assignment")
            else:
                if expr[1] in self.memory:
                    self.memory[expr[0]] = self.memory[expr[1]]
                else:
                    self.memory[expr[0]] = expr[1]
        else:
            print("Invalid assignment")

    def check_expression(self, expression):
        check = True
        # if not expression[-1].isdigit():
        if expression[-1] in self.operators:
            check = False
        else:
            if len(expression.split()) > 1:
                check = any([True for i in self.operators if i in [j for j in expression]])
        return check

    def reformat_expression(self, expression):
        new_expression = ''
        for i, j in enumerate(expression):
            try:
                next_c = expression[i + 1]
            except IndexError:
                next_c = ' '

            if (j in self.operators and next_c != ' ') or (j != ' ' and next_c in self.operators):
                new_expression += j + ' '
            else:
                new_expression += j
        return new_expression

    def evaluate(self, expression):
        resultat = 0
        signe = 1
        for i in expression.split():
            if i in self.operators:
                signe *= int(i + '1')
                continue
            else:
                i = self.memory[i] if i in self.memory else i
                resultat += signe * int(i)
                signe = 1
        return resultat

    def calculate(self):
        while True:
            user_input = input().strip()

            if user_input == '':
                continue
            elif user_input.startswith('/'):
                self.check_command(user_input)
            elif '=' in user_input:
                self.check_assignment(user_input)
            elif user_input in self.memory:
                print(self.memory[user_input])
            elif self.valid_identifier(user_input) and user_input not in self.memory:
                print("Unknown variable")
            else:
                new_expr = self.reformat_expression(user_input)
                if not self.check_expression(new_expr):
                    print("Invalid expression")
                else:
                    try:
                        resultat = self.evaluate(new_expr)
                    except ValueError as e:
                        print(e)
                        print("Invalid expression")
                    else:
                        print(resultat)


calculatrice = SmartCalculator()
calculatrice.calculate()
