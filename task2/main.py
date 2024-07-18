from circle import Circle
from triangle import Triangle


def sum_of_areas(shapes):
    summary_area = 0
    for shape in shapes:
        summary_area += shape.area()
    return summary_area


if __name__ == '__main__':
    figure1 = Triangle([3, 4, 5])
    print(figure1.area())
    print(figure1.is_rectangular())

    figure2 = Circle(3)
    print(figure2.area())

    figures = [figure1, figure2]
    print(sum_of_areas(figures))
