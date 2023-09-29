def rect_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("length and width are not positive numbers")
    return length * width


def rect_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("length and width are not positive numbers")
    return 2 * (length + width)


try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = rect_area(length, width)
    perimeter = rect_perimeter(length, width)

    print(f"The area of the rectangle: {area}")
    print(f"The perimeter of the rectangle: {perimeter}")
except ValueError as e:
    print(f"Error: {e}")