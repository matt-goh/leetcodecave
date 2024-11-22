from typing import List
import time

class Solution:
    def hasDuplicateOriginal(self, nums: List[int]) -> bool:
        # first try solution - O(n²) time, O(n) space
        numList = []
        for num in nums:
            for num2 in numList:
                if num == num2:
                    return True
            numList.append(num)
        return False
    
    def hasDuplicateOptimized(self, nums: List[int]) -> bool:
        # Optimized solution - O(n) time, O(n) space
        return len(nums) != len(set(nums))  # Even more concise! set can only contain unique elements so if the length of the set is less than the length of the list, there must be duplicates

def test_performance():
    solution = Solution()
    
    # Test cases
    small_test = [1, 2, 3, 1]  # Small test with duplicate
    large_test = list(range(10000)) + [1]  # Large test with duplicate at the end
    
    print("Testing small array:", small_test)
    
    # Test original solution
    start = time.perf_counter()
    result1 = solution.hasDuplicateOriginal(small_test)
    time1 = time.perf_counter() - start
    print(f"Original solution - Result: {result1}, Time: {time1:.6f} seconds")
    
    # Test optimized solution
    start = time.perf_counter()
    result2 = solution.hasDuplicateOptimized(small_test)
    time2 = time.perf_counter() - start
    print(f"Optimized solution - Result: {result2}, Time: {time2:.6f} seconds")
    
    print("\nTesting large array with 10,001 elements...")
    
    # Test original solution
    start = time.perf_counter()
    result3 = solution.hasDuplicateOriginal(large_test)
    time3 = time.perf_counter() - start
    print(f"Original solution time: {time3:.6f} seconds")
    
    # Test optimized solution
    start = time.perf_counter()
    result4 = solution.hasDuplicateOptimized(large_test)
    time4 = time.perf_counter() - start
    print(f"Optimized solution time: {time4:.6f} seconds")
    
    if time4 > 0:
        print(f"\nPerformance improvement: {time3/time4:.2f}x faster")

if __name__ == "__main__":
    test_performance()