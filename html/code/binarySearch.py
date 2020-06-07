def binarySearch(arr, target):
	if not arr:
		return -1

	l = 0
	r = len(arr) -1 

	while l <= r:
		# mid = (l + r) // 2
		mid = l + (h - l) // 2 # avoid overflow

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			# target is in the right half
			l = mid + 1
		else:
			#target is in the left half
			r = mid - 1

	return -1 	# target not found
	# return max(l, r) # target not found and the position that target should be inserted is returned
	return l # target not found and the position that target should be inserted is returned --> YOU DON"T NEED MAX
	# 																							max(l, r) will always be l, 
	#																							given the while loop condition above
	# TO MAKE SENSE OF THIS
	# when l and r is above to cross, they must pointing at the same index x
	# if arr[x] < target, we want to insert target after arr[x]
	#		in this case, l will be incremented, so l is the right position to insert
	# if arr[x] > target, we want to insert target at x's position and push x and everything else one slot to the right
	#		in this case, r will be decremented, so l is still at x's position and is the right value to return


# search the last position of target value in an array with duplicates
def searchLastPositionOfElement(arr, target):
	if not arr:
		return -1

	l = 0
	r = len(arr) -1

	while l <= r :
		mid = l + (r - l)//2

		if arr[mid] <= target :
			# when equal, move to the right as well
			l = mid + 1
		else :
			r = mid - 1

	rv = r if arr[r] == target else -1
	return rv

# search the first position of target value in an array with duplicates
def searchFirstPositionOfElement(arr, target):
	if not arr:
		return -1

	l = 0
	r = len(arr) - 1

	while l <= r :
		mid = l + (r - l) // 2

		if arr[mid] >= target :
			# when equal, move to the left as well for the first element position
			r = mid - 1
		else:
			l = mid + 1

	rv = l if arr[l] == target else -1
	return rv







def main():
	arr = [1,2,3,3,3,6,7]
	target = 3
	print (searchFirstPositionOfElement(arr, target))


if __name__ == '__main__':
	main()