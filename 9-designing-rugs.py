# Write a function that accepts the height and width (m, n) and an optional proc s and generates a list with m elements. Each element is a string consisting of either:
#   The default character (hash #) repeating n times (if no proc is given).
#   The character passed in through the proc repeating n times.

def make_rug(m, n, s = '#'):
    rug = []
    n_string = s * n
    i = 0
    while i < m:
        rug.append(n_string)
        i += 1
    return rug

print(make_rug(3, 5, '#'))
