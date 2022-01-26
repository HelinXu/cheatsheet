import sys
import random

def error_fn(input: int):
    while True:
        rand_num = random.randint(0, 10)
        print(f'{input} / {rand_num} = {input / rand_num}')


try:
    error_fn(123456789)
except ZeroDivisionError as e:
    if 'division' in str(e):
        print(str(e))
        sys.exit(99)
    else:
        raise e