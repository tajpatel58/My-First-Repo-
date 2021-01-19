
# This is merely me getting used to git.


def sum_of_n_sqrd(n):
    total = 0
    for j in range(1, n+1):
        total = total + j**2
    return total

print(sum_of_n_sqrd(50))