'''
Page 90 - Problem 1.3
URLify: Write a method to replace all spaces in a
string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional
characters, and that you are given the "true" length
of the string. (Not: If implementing in Java, please
use a character array so that you can perform this 
operation in place.)
'''

# O(n)
def URLify(s, l):
	new_s = []
	# O(n)
	for i in range(l):
		if s[i] == " ":
			new_s += "%20"
		else:
			new_s += s[i]
	# O(n)
	return "".join(new_s)

print(URLify("Mr John Smith        ", 13))