def calculate_simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Values must be non-negative")
    interest = (principal * rate * time) / 100
    return interest


if __name__ == "__main__":
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest: "))
        t = float(input("Enter time period (years): "))
        si = calculate_simple_interest(p, r, t)
        total = p + si
        print(f"\nSimple Interest = {si}")
        print(f"Total Amount = {total}")
    except ValueError as e:
        print(f"Error: {e}")
