from typing import List

# FizzBuzz function
def fizzbuzz(n: int) -> List[str]:
    if n <= 0:
        raise Exception
    result = []

    for i in range(1, n + 1):
        res = ""
        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"
        if not res:
            res += str(i)
        result.append(res)

    return result

# Run fizzbuzz() function
print(fizzbuzz(10))