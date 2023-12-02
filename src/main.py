# # 1.
#
# nums = [3, 2, 4]
# target = 6
#
# for i1, v1 in enumerate(nums):
# 	for i2, v2 in enumerate(nums):
# 		if v1 + v2 == target and i1 < i2:
# 			print([i1, i2])
#
# 2.

class ListNode:

	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

ListNode l1 = None
l1.val = [0]
ListNode l2 = None
l2.val = [0]
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
if len(l1) < len(l2):
	l1 = l1 + [0] * (len(l2) - len(l1))
elif len(l2) < len(l1):
	l2 = l2 + [0] * (len(l1) - len(l2))
l3 = []
carry = 0
for d1, d2 in zip(l1, l2):
	d3 = d1 + d2 + carry
	if d3 > 9:
		l3.append(d3 - 10)
		carry = 1
	else:
		carry = 0
		l3.append(d3)
if carry == 1:
	l3.append(1)
print(l3)
