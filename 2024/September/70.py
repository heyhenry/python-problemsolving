# Solution Credit to AlgoEngine:  https://leetcode.com/problems/climbing-stairs/solutions/5772835/video-visualization-of-bottom-up-dynamic-programming/

def climb_stars(n):

    if n == 1:
        return 1

    n_one = 1
    n_two = 1
    total = 0

    for _ in range(n-1):
        total = n_one + n_two
        n_one = n_two
        n_two = total

    return total

def main():
    print(climb_stars(2))
    print(climb_stars(3))

if __name__ == "__main__":
    main()