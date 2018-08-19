'''
Page 98 - Problem 1.1
Is Unique: Implement an algorithm to determine if a string
has all unique characters. What if you cannot use additional
data structures?
'''

# O(log n)
def is_unique(s):
	s = list(s)
	# O(log n)
	s.sort()
	# O(n)
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			return False
	return True
