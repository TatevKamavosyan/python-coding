def generate_natural_numbers(n):
    return list(range(1, n + 1))

def average(generate_natural_numbers,n):
    natural_numbers = generate_natural_numbers(n)
    if sum(natural_numbers) / n in natural_numbers:
        return "Average of natural numbers can be a natural number"
    else:
        return "Average of natural numberscan't be a natural number"
print(average(generate_natural_numbers,20))   

