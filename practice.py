# def add_to_list(value, my_list=[]):
#     my_list.append(value)
#     return my_list

# list1 = add_to_list(1)
# list2 = add_to_list(2)
# print(list1)

# for i in [1, 2, 3, 4][::-1]:
#     print(i)


# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         def check(start, end):
#             chars = set()
#             for i in range(start, end + 1):
#                 c = s[i]
#                 if c in chars:
#                     return False
#                 chars.add(c)
#             return True

#         n = len(s)

#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if check(i, j):
#                     res = max(res, j - i + 1)
#         return res


# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0:
#             return False

#         numInput = x
#         output = 0
#         while x > 0:
#             output = output * 10  + x % 10
#             x = x // 10

#         return numInput == output


# class Solution(object):
#     def isPalindrome(self, x):
#         b = str(x).casefold().replace(" ", "")[::-1]
#         return b == str(x).casefold().replace(" ", "")


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = set(nums)
        return not len(n) == len(nums)
            

b = Solution()
a = [1, 2, 2, 4]
print(b.containsDuplicate(a))
