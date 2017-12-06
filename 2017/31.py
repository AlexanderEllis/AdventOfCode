import math


def spiral_memory_distance(number):

    # 1 is edge case
    if number == 1:
        return 0
    
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

    y = 0
    x = 0

    if distance_along_outside >= 3 * edge_length:
        x = distance_along_outside - 3 * edge_length
    elif distance_along_outside >= edge_length and distance_along_outside <= (2 * edge_length):
        x = distance_along_outside - edge_length
    else:
        x = edge_length

    if distance_along_outside >= 2 * edge_length and distance_along_outside <= (3 * edge_length):
        y = distance_along_outside - (2 * edge_length)
    elif distance_along_outside <= edge_length:
        y = distance_along_outside
    else:
        y = edge_length

    y = abs(y - half_edge_length)
    x = abs(x - half_edge_length)

    return x + y


assert spiral_memory_distance(1) == 0
assert spiral_memory_distance(12) == 3
assert spiral_memory_distance(23) == 2
assert spiral_memory_distance(1024) == 31

print(spiral_memory_distance(277678))