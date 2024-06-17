import random

class QuestionGenerator:
    # Fundamental operations
    f_limit = 10
    # Rooting and potentiation
    h_limit = 30

    operations = {
        '+': 'Adição',
        '-': 'Subtração',
        'x': 'Multiplicação',
        '/': 'Divisão',
        '^': 'Potenciação',
        '#': 'Radiciação'
    }
    @classmethod
    def gen_question(cls, operation):
        match operation:
            case '+':
                return cls.__add_question()
            case '-':
                return cls.__subtraction_question()
            case 'x':
                return cls.__multiplication_question()
            case '/':
                return cls.__division_question()
            case '^':
                return cls.__potentiation_question()
            case '#':
                return cls.__rooting_question()
            case _:
                raise AttributeError(
                    'operation must be one of these: ["+", "-", "x", "/", "^", "#"]'
                )

    @classmethod
    def __add_question(cls):
        # Addition operation
        n1 = random.randint(0, cls.f_limit)
        n2 = random.randint(0, cls.f_limit)
        return f"{n1} + {n2} = ?", n1 + n2

    @classmethod
    def __subtraction_question(cls):
        # Subtraction operation with non-negative result
        n2 = random.randint(0, cls.f_limit)
        n1 = random.randint(n2, cls.f_limit + n2)
        return f"{n1} - {n2} = ?", n1 - n2

    @classmethod
    def __multiplication_question(cls):
        # Multiplication operation
        n1 = random.randint(0, cls.f_limit)
        n2 = random.randint(0, cls.f_limit)
        return f"{n1} x {n2} = ?", n1 * n2

    @classmethod
    def __division_question(cls):
        # Division operation
        n1 = random.randint(1, cls.f_limit)
        n2 = random.randint(1, cls.f_limit)
        return f"{n1 * n2} dividido por {n1} = ?", n2

    @classmethod
    def __potentiation_question(cls):
        # Potentiation operation (no negative expoents)
        n1 = random.randint(1, cls.h_limit)
        return f'{n1} elevado a 2 = ?', n1 ** 2

    @classmethod
    def __rooting_question(cls):
        # Rooting operation
        n1 = random.randint(1, cls.h_limit)
        return f'Raiz quadrada de {n1 ** 2} = ?', n1
