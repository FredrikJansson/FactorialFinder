"""

   Fredrik Jansson

"""

# ===============================
# =           Classes           =
# ===============================

class FactorialRecursion:
	def __init__(self, n):
		if n < 0:
			raise ValueError("Input must be positive.")
		res = self.main(n)
		print("[Recursion]: The factorial of {} is {}.".format(n, res))

	def main(self, n):
		if n == 1:
			return n
		return n * self.main(n - 1)

class FactorialLoop:
	def __init__(self, n):
		if n < 0:
			raise ValueError("Input must be positive.")
		res = self.main(n)
		print("[Loop]: The factorial of {} is {}.".format(n, res))

	def main(self, n):
		val = 1
		while n != 1:
			val *= n
			n -= 1
		return val

# ====================================
# =           Main Section           =
# ====================================

if __name__ == "__main__":
	choice = int(input("Enter 0 for Loop-version, anything else (or nothing) for Recursion: ") or 1)
	n = int(input("Enter inital value: "))
	factorial = FactorialRecursion(n) if choice else FactorialLoop(n)