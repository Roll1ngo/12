from typing import Union

Number = Union[int, float]


def plus(x: int | float | str, y: Union) -> Union:
    return x + y


print(plus(5.5, "4"))
