import unittest

UNIVERSAL_GRID = [[0]] * 1000

for i in range(999):
    UNIVERSAL_GRID[i].append(0)


def clear_grid():
    for i in range(999):
        UNIVERSAL_GRID[i].append(0)


class TestChristmasLights(unittest.TestCase):
    def test_grid_size(self):
        sum_of_row = 0
        for row in UNIVERSAL_GRID:
            sum_of_row += len(row)
        assert sum_of_row == 1000000

    def test_one_light(self):
        turn_on_light((0, 0))
        assert UNIVERSAL_GRID[0][0] == 1
        clear_grid()

    def test_turning_on_range_of_lights(self):
        turn_on_range((0, 0), (2, 2))
        assert check_light_range_is_on((0, 0), (2, 2)) == True
        clear_grid()

    def test_instruction_one(self):
        turn_on_range((887, 9), (959, 629))
        assert check_light_range_is_on((887, 9), (959, 629)) == True
        clear_grid()

    def test_turn_off_light(self):
        turn_on_light((0, 0))
        assert UNIVERSAL_GRID[0][0] == 1
        turn_off_light((0, 0))
        assert UNIVERSAL_GRID[0][0] == 0
        clear_grid()


def check_light_range_is_on(start: tuple, end: tuple):
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if UNIVERSAL_GRID[x][y] != 1:
                return False
    return True


def turn_off_light(coordinate: tuple):
    x = coordinate[0]
    y = coordinate[1]
    UNIVERSAL_GRID[x][y] = 0


def turn_on_range(start: tuple, end: tuple):
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            turn_on_light((x, y))


def turn_on_light(coordinate: tuple):
    x = coordinate[0]
    y = coordinate[1]
    UNIVERSAL_GRID[x][y] = 1


# 887,9 through 959,629
#   c o l
# r 0 0 0
# o 0 0 1
# w 0 0 0

# x = (1,2)
