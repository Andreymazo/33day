import re
def to_camel_case(text):
    return re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|-', text)[::])

print(to_camel_case('tyi_kjrv-krhbv'))

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    count_bits = lambda n: bin(n).count('1')

    def digital_root(n):
        if n < 10:
            return n
        else:
            print(digital_root(sum(map(int, str(n)))))

    digital_root(25)

    even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
    print(even_or_odd(6))