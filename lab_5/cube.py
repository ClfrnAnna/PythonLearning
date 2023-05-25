from typing import Union


def cube_area(side: Union[int, float]) -> Union[int, float]:
    """
        Функция вычисляет площадь поверхности куба
    """
    if not isinstance(side, (int, float)) or isinstance(side, bool):
        raise TypeError
    elif side <= 0:
        raise ValueError

    return 6 * side ** 2
