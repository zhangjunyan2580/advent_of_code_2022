from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, positives, rays, rays_from_inside


def solve(grid):
    height = len(grid)
    width = len(grid[0])

    best = 0
    
    for y in range(height):
        for x in range(width):
            h = grid[y][x]
            raysfrom = rays_from_inside(grid, y, x)
            lengths = []

            for ray in raysfrom:
                length = 0
                for tree in ray:
                    length += 1
                    if tree >= h:
                        break
                lengths.append(length)

            best = max(best, multall(lengths))

    return best


def main():
    lines = []

    with open('8.txt') as f:
        for line in f.readlines():
            lines.append(digits(line))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())