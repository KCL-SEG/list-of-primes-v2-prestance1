from typing import List

def _gen_prime() -> int:
    curr_num = 2
    while True:
        if all(
           (curr_num % n != 0) for n in range(2, curr_num) 
        ):
            yield curr_num
        curr_num += 1

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes: int) -> List[int]:
    if number_of_primes < 1:
        raise ValueError("Invalid argument")
    prime_generator = _gen_prime()
    return [next(prime_generator) for _ in range(number_of_primes)]
