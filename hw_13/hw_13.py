import time

'''
Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.
Example:

@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)
> 3

add(1, "2")
> TypeError: Argument b must be int, not str
'''


def typed(type_):
    def check_types(func):
        def wrapper(*args):

            for arg in args:
                if type(arg) != type_:
                    return f'TypeError: Argument {arg} must be {type_}, not {type(arg)}'

            return func(*args)

        return wrapper

    return check_types


@typed(int)
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(3, "5"))
    # print(add(3, 5))

'''
Write a decorator that will calculate the execution time of a function.
Example:

    @calculate_execution_time
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    > 3
    > Execution time: 0.0005 seconds
'''


def calculate_execution_time(func):

    def wrapp(*args):

        start_time = time.time()
        result = func(*args)

        return f"Result: {result} \nExecution time: {(time.time() - start_time)*1000} seconds"

    return wrapp


@calculate_execution_time
def add2(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(add2(1, 2))