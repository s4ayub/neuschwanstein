def canJumpBacktrack(position, nums):
    if position == len(nums) - 1: # you made it!
        return True
    
    furthestJump = min(position + nums[position], len(nums) - 1)

    for i in range(position + 1, furthestJump + 1):
        if canJumpBacktrack(i, nums):
            return True
    
    return False

def canJumpDynamicTopDown(position, nums):
    memo = ["UNKNOWN"] * len(nums)
    
    def recurse(position, nums):
        if memo[position] != "UNKNOWN": # you made it!
            return memo[position] == "GOOD"
        
        furthestJump = min(position + nums[position], len(nums) - 1)

        for i in range(position + 1, furthestJump + 1):

            if recurse(i, nums):
                memo[position] = "GOOD"
                return True
        
        memo[position] = "BAD"
        return False   
    
    memo[len(nums)-1] = "GOOD"
    return recurse(position, nums)

print(canJumpDynamicTopDown(0, [2,3,1,1,4]))
print(canJumpDynamicTopDown(0, [3,2,1,0,4]))

def canJumpDynamicBottomUp(position, nums):
    memo = [False] * len(nums)
    memo[len(nums) - 1] = True

    for i in range(len(nums) - 2, -1, -1):
        furthestJump = min(i + nums[i], len(nums) - 1)

        for j in range(i + 1, furthestJump + 1):
            if memo[j] == True:
                memo[i] = True
                break
    
    return memo[0]

print(canJumpDynamicBottomUp(0, [2,3,1,1,4]))
print(canJumpDynamicBottomUp(0, [3,2,1,0,4]))

# BEST ONE: time -> O(n), space -> O(1)
def canJumpGreedy(position, nums):
    # just check if you can get to the left most good index, if you can get there
    # you can get to the good indexes past it as well.

    leftMostGoodIndex = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= leftMostGoodIndex:
            leftMostGoodIndex = i
    
    return leftMostGoodIndex == 0

print(canJumpGreedy(0, [2,3,1,1,4]))
print(canJumpGreedy(0, [3,2,1,0,4]))