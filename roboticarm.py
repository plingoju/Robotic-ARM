def sort(width, height, length, mass):
    """
    Dispatch packages into stacks:
      - Bulky: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
      - Heavy: mass >= 20 kg
      - REJECTED: both bulky and heavy
      - SPECIAL: bulky or heavy (but not both)
      - STANDARD: neither bulky nor heavy
    """
    # input validation
    for name, value in (("width", width), ("height", height), ("length", length), ("mass", mass)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number. got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"{name} must be non-negative. got {value}")

    volume = width * height * length
    bulky = (volume >= 1_000_000) or (width >= 150) or (height >= 150) or (length >= 150)
    heavy = mass >= 20

    # final dispatch decision (using nested ternary as required)
    return "REJECTED" if (bulky and heavy) else ("SPECIAL" if (bulky or heavy) else "STANDARD")


# --- Example Tests ---
if __name__ == "__main__":
    tests = [
        (10, 10, 10, 5, "STANDARD"),      # small package
        (200, 1, 1, 5, "SPECIAL"),       # bulky (dim >= 150)
        (100, 100, 100, 10, "SPECIAL"),  # bulky (volume = 1,000,000)
        (100, 100, 100, 20, "REJECTED"), # bulky + heavy
        (50, 50, 50, 20, "SPECIAL"),     # heavy only
    ]

    for w, h, l, m, expected in tests:
        result = sort(w, h, l, m)
        print(f"sort({w}, {h}, {l}, {m}) -> {result} | expected: {expected}")
