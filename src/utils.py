def greet(name):
    # Intentional style issue: bad formatting
    return f"Hello, {name}!"

import os
import math
import datetime
from typing import List, Any, Optional


class PyUtilities:
    """A collection of common Python utility functions."""

    # ---------------- STRING UTILITIES ----------------
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Check if a string is a palindrome (case-insensitive)."""
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def reverse_string(s: str) -> str:
        """Return the reversed version of a string."""
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        return s[::-1]

    # ---------------- MATH UTILITIES ----------------
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Compute the greatest common divisor."""
        if not all(isinstance(x, int) for x in (a, b)):
            raise TypeError("Inputs must be integers.")
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Compute the least common multiple."""
        if not all(isinstance(x, int) for x in (a, b)):
            raise TypeError("Inputs must be integers.")
        return abs(a * b) // math.gcd(a, b) if a and b else 0

    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
