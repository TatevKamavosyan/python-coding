odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]

# ա) երկու թվանշաններն էլ կենտ
odd_numbers = [
    10 * a + b
    for a in odd
    for b in odd
]

# բ) երկու թվանշաններն էլ զույգ
even_numbers = [
    10 * a + b
    for a in even
    if a != 0          # երկնիշ թիվ, առաջին թվանշանը չի կարող լինել 0
    for b in even
]

print("ա) Կենտ թվանշաններով երկնիշ թվերի քանակը:", len(odd_numbers))
print("բ) Զույգ թվանշաններով երկնիշ թվերի քանակը:", len(even_numbers))
