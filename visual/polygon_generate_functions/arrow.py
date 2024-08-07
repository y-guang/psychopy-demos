import math

def generate_arrow_vertices(length: float, arrow_width: float, body_width: float):
    """
    generate elegant arrow 2d-vertices.
    """
    # normalize the parameters according to the length
    arrow_width /= length
    body_width /= length
    length = 1.0

    # assume arrow points to top, and stand on the origin
    bottom_left = (-body_width / 2, 0)
    bottom_right = (body_width / 2, 0)
    top = (0, length)

    # calculate the arrow left and right points
    arrow_length = arrow_width / 2 * math.sqrt(3)
    arrow_left = (-arrow_width / 2, length - arrow_length)
    arrow_right = (arrow_width / 2, length - arrow_length)

    # calculate the conjugate point of the arrow and the body
    drilling_depth = (arrow_width - body_width) / 2 / math.sqrt(3)
    net_body_length = length - arrow_length + drilling_depth
    conjugate_left = (-body_width / 2, net_body_length)
    conjugate_right = (body_width / 2, net_body_length)

    vertices = [bottom_left, bottom_right, conjugate_right, arrow_right, top, arrow_left, conjugate_left]
    
    # centering the arrow
    vertices = [(x, y - length / 2) for x, y in vertices]
    return vertices

if __name__ == "__main__":
    print(generate_arrow_vertices(3, 1, 0.2))