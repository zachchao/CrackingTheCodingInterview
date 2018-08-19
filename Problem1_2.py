'''
Page 98 - Problem 1.2
Check Permutation: Given two strings, write a method
to decide if one is a permutation of the other.
'''
# O(n), specifically... O(2n+k)
# Where k is the number of unique characters
def check_permutation(s1, s2):
	d = {}
	for c in s1:
		if c not in d:
			d[c] = 0
		d[c] += 1
	for c in s2:
		if c not in d:
			return False
		d[c] -= 1
	for key in d:
		if d[key] != 0:
			return False
	return True

print(check_permutation("asdf", "fdsa"))
