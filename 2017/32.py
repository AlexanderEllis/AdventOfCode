import math


def sum_spiral_memory(number):

    array_width = 21

    spiral_memory = [0] * array_width
    for i in range(array_width):
        spiral_memory[i] = [0] * array_width

    center_x = array_width // 2
    center_y = array_width // 2

    x = 0
    y = 0


    for i in range(1, number + 1):
        (x_index, y_index) = find_indices(i)
        x_position = center_x + x_index
        y_position = center_y - y_index

        neighbors_total = sum_neighbors(spiral_memory, x_position, y_position)

        if i == 1:
            neighbors_total = 1
        
        if (neighbors_total > 277678):
            print(neighbors_total)
            return

        spiral_memory[y_position][x_position] = neighbors_total

    return 0


def find_indices(number):

    if (number == 1):
        return (0, 0)
    # Find closest bottom right corner by finding closest odd sqrt
    closest_root = math.floor(math.sqrt(number))

    # If this is even, then it's the next lowest one
    if not closest_root % 2:
        closest_root -= 1

    # Get bottom right corner value
    bottom_right_corner = closest_root ** 2

    # Get edge length, which is one more than the closest_root
    edge_length = closest_root + 1
    half_edge_length = edge_length / 2

    # Determine how far along outside we've gone
    distance_along_outside = number - bottom_right_corner

    y_offset = 0
    x_offset = 0

    if distance_along_outside == 0:
        y_offset = -1 * (half_edge_length - 1)
        x_offset = half_edge_length - 1
    elif distance_along_outside > 3 * edge_length:
        x_offset = distance_along_outside - (3 * edge_length) - half_edge_length
        y_offset = -1 * half_edge_length
    elif distance_along_outside <= 3 * edge_length and distance_along_outside >= 2 * edge_length:
        x_offset = -1 * half_edge_length
        y_offset = -1 * (distance_along_outside - (2 * edge_length) - half_edge_length)
    elif distance_along_outside < 2 * edge_length and distance_along_outside > edge_length:
        x_offset = -1 * (distance_along_outside - (edge_length) - half_edge_length)
        y_offset = half_edge_length
    else:
        x_offset = half_edge_length
        y_offset = (distance_along_outside - half_edge_length)

    # print('number:', number)
    # print('bottom_right_corner', bottom_right_corner)
    # print('distance_along_outside', distance_along_outside)
    # print('edge_length', edge_length)
    # print('half_edge_length', half_edge_length)

    # print('y_offset:', y_offset)
    # print('x_offset:', x_offset)

    return (int(x_offset), int(y_offset))


def odd_square_number(odd_square):
    i = 1
    while i ** 2 < odd_square:
        i += 1

    return i


def sum_neighbors(two_dimensional_array, x_index, y_index):
    total = 0
    total += two_dimensional_array[y_index - 1][x_index - 1]
    total += two_dimensional_array[y_index - 1][x_index]
    total += two_dimensional_array[y_index - 1][x_index + 1]
    total += two_dimensional_array[y_index][x_index - 1]
    total += two_dimensional_array[y_index][x_index + 1]
    total += two_dimensional_array[y_index + 1][x_index - 1]
    total += two_dimensional_array[y_index + 1][x_index]
    total += two_dimensional_array[y_index + 1][x_index + 1]

    return total


sum_spiral_memory(400)
# assert sum_spiral_memory(1) == 1
# assert sum_spiral_memory(2) == 1
# assert sum_spiral_memory(3) == 2
# assert sum_spiral_memory(4) == 4
# assert sum_spiral_memory(5) == 5