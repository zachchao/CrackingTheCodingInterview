'''
Page 98 - Problem 1.1
Is Unique: Implement an algorithm to determine if a string
has all unique characters. What if you cannot use additional
data structures?
'''

# Initial question
# O(n) is best as all characters must be visisted at least once
def is_unique(s):
	d = {}
	for c in s:
		if c in d:
			return False
		d[c] = True
	return True

print(is_unique("asdf"))
print(is_unique("asdfa"))
# Without additional data structures
# With no memory the best we have is O(n**2)
def is_unique(s):
	for i in range(len(s)):
		for i2 in range(i + 1, len(s)):
			if s[i] == s[i2]:
				return False
	return True

print(is_unique("asdf"))
print(is_unique("asdfa"))
