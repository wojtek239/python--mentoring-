from functools import reduce

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

add = lambda x, y: x + y

result = reduce(add, nums1 + nums2 + nums3)

print(f'Sum of these three lists is: ', result)
print(sum(list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))))
