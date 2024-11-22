def two_sum(nums, target):
    # Hash map to store number -> index mapping
    num_map = {}
    
    # Single pass through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
            
        # Add current number and its index to map
        num_map[num] = i
    return []  # Should never reach here given problem constraints

# Test cases
def run_tests():
    # Test case 1
    assert two_sum([3,4,5,6], 7) == [0,1]
    
    # Test case 2
    assert two_sum([4,5,6], 10) == [0,2]
    
    # Test case 3
    assert two_sum([5,5], 10) == [0,1]
    
    print("All test cases passed!")

run_tests()