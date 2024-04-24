import random
import functools


class Puzzle:
    state: list[int] = [0] * 9

    def __init__(self):
        # Generate random starting state
        self.state = list(range(9))
        random.shuffle(self.state)
        self.make_solvable()
        self.is_solvable()

    # directions = up, right, down, left = [0, 1, 2, 3]
    # returns whether move was successful
    def move(self, direction: int) -> bool:
        player_index = self.state.index(0)
        if direction == 0:  # up
            # bounds check: noop if on first row
            if player_index // 3 == 0:
                return False
            target_index = player_index - 3
        elif direction == 1:  # right
            # bounds check: noop if on right col
            if player_index % 3 == 2:
                return False
            target_index = player_index + 1
        elif direction == 2:  # down
            # bounds check: noop if on bottom row
            if player_index // 3 == 2:
                return False
            target_index = player_index + 3
        elif direction == 3:  # left
            # bounds check: noop if on left col
            if player_index % 3 == 0:
                return False
            target_index = player_index - 1

        self.swap(player_index, target_index)

    def swap(self, src: int, dst: int):
        self.state[src], self.state[dst] = (
            self.state[dst],
            self.state[src],
        )
        print(f"swapped ([{src}] = {self.state[src]}, [{dst}] = {self.state[dst]})")

    def is_solved(self):
        return self.state == list(range(1, 9)) + [0]

    # counts the number of inversions, returns True if even, False if odd
    def is_solvable(self):
        inversions = 0
        for i in range(9):
            # take the first element
            inversions += functools.reduce(
                lambda acc, val: acc + (1 if (val > 0 and val < self.state[i]) else 0),
                self.state[i + 1 :],
                0,
            )
        print(f"this shit has {inversions} inversions")
        return inversions % 2 == 0

    def make_solvable(self):
        if self.is_solvable():
            return
        # find first inversion (naively)
        inversion_indices = (-1, -1)
        for i in range(9):
            if self.state[i] == 0:
                continue
            for j in range(i, 9):
                if self.state[j] == 0:
                    continue
                if self.state[j] < self.state[i]:
                    inversion_indices = (i, j)
                    break
            if inversion_indices != (-1, -1):
                break
        self.swap(i, j)

    def print(self):
        for i in range(3):
            print(f"{self.state[3 * i:(i + 1) * 3]}")


def main():
    # random.seed("test")
    print("8puzzle")
    print("solve da puzzo. zero go top left!")
    puzzle = Puzzle()
    puzzle.print()
    print("now move until solved!")
    print("directions = up, right, down, left = [0, 1, 2, 3]")
    valid_inputs = [str(i) for i in range(4)]
    while not puzzle.is_solved():
        while (user_input := input()) not in valid_inputs:
            print("directions = up, right, down, left = [0, 1, 2, 3]")
        direction = int(user_input)
        puzzle.move(direction)
        puzzle.print()
    print("woah! you solved the puzzle! gz")


if __name__ == "__main__":
    main()
