"""This is module1."""


def area_rect(width, height):
    """Calculate the area of a rectangle given its width and height.

    :param width: Width of the rectangle
    :type width: float
    :param height: Height of the rectangle
    :return: Area of the rectangle
    :rtype: float
    """
    return width * height


def area_circle(radius: float) -> float:
    return 3.14 * radius ** 2
