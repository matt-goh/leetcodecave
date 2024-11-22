# Import required libraries
from typing import List
import time
import random
import string
import statistics
from collections import defaultdict

def generate_test_cases():
    """Generate three test cases of different sizes for comparison"""
    # Test case 1: Small predefined example
    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # Test case 2: Medium - 200 random strings
    test2 = []
    for _ in range(200):
        length = random.randint(3, 8)  # Slightly shorter strings
        test2.append(''.join(random.choices(string.ascii_lowercase, k=length)))
    
    # Test case 3: Large - 500 random strings
    test3 = []
    for _ in range(500): 
        length = random.randint(3, 8)
        test3.append(''.join(random.choices(string.ascii_lowercase, k=length)))
    
    return [test1, test2, test3]

class OriginalSolution:
    """
    Big O Analysis:
    Time: O(m * n * k * log k), where:
        - m is number of strings
        - n is average size of groups (could be m in worst case)
        - k is average length of strings (for sorting)
        This is because for each string (m), we might check every group (n),
        and for each check we sort and compare strings (k log k)
    
    Space: O(m * k), where:
        - m is number of strings
        - k is average length of strings
        We store all strings in our answer groups
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Start with first string in its own group
        answer = [[strs[0]]]
        
        # Process remaining strings
        for str in strs[1:]:
            found_match = False
            # Check each existing group
            for index, subList in enumerate(answer):
                # Only need to check first item in sublist since all items are anagrams
                for listItem in subList:
                    # Compare sorted versions to identify anagrams
                    if "".join(sorted(str)) == "".join(sorted(listItem)):
                        found_match = True
                        answer[index].append(str)
                        break
            # Create new group if no match found
            if found_match == False:
                answer.append([str])
        return answer

class OptimizedSolution:
    """
    Big O Analysis:
    Time: O(m * k * log k), where:
        - m is number of strings
        - k is average length of strings
        For each string, we sort it (k log k) and do a hash map operation (O(1))
    
    Space: O(m * k), where:
        - m is number of strings
        - k is average length of strings
        We store all strings plus their sorted versions in hash map
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        # Key: sorted string (anagram identifier)
        # Value: list of strings that are anagrams
        groups = {}
        
        for str in strs:
            # Sort string to create key - all anagrams will have same sorted string
            sorted_str = "".join(sorted(str))
            
            # Add to existing group or create new group
            if sorted_str in groups:
                groups[sorted_str].append(str)
            else:
                groups[sorted_str] = [str]
                
        return list(groups.values())

class CountingSolution:
    """
    Big O Analysis:
    Time: O(m * k), where:
        - m is number of strings
        - k is average length of strings
        For each string, we count its characters (k) and do a hash map operation (O(1))
        Note: While this has better theoretical complexity, for shorter strings
        the sorting solution might be faster due to Python's optimized sorting
    
    Space: O(m), where:
        - m is number of strings
        We store all strings and fixed-size count arrays (26 integers each)
        The count array is constant space regardless of string length
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        # Key: tuple of character counts
        # Value: list of strings that are anagrams
        res = defaultdict(list)
        
        for s in strs:
            # Create count array for current string
            count = [0] * 26  # Array for a-z character counts
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Add string to its group using count array as key
            res[tuple(count)].append(s)
            
        return list(res.values())

def run_comparison():
    """Run and compare all solutions with different test cases"""
    original = OriginalSolution()
    optimized = OptimizedSolution()
    counting = CountingSolution()
    test_cases = generate_test_cases()
    
    print("Comparing Solutions Performance:\n")
    print("Big O Analysis Summary:")
    print("-" * 50)
    print("Original Solution:")
    print("Time: O(m * n * k * log k) - worst performing")
    print("Space: O(m * k)")
    print("\nOptimized Solution:")
    print("Time: O(m * k * log k) - removes nested loop")
    print("Space: O(m * k)")
    print("\nCounting Solution:")
    print("Time: O(m * k) - best theoretical complexity")
    print("Space: O(m) - best space usage")
    print("\nWhere:")
    print("m = number of strings")
    print("n = average size of groups")
    print("k = average length of strings")
    print("-" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i} (Size: {len(test_case)} strings)")
        print("-" * 50)
        
        # Test original solution with multiple runs
        original_times = []
        for _ in range(3):  # Reduced from 5 to 3 runs for faster results
            start = time.perf_counter()
            result1 = original.groupAnagrams(test_case.copy())
            end = time.perf_counter()
            original_times.append(end - start)
        
        # Test optimized solution with multiple runs
        optimized_times = []
        for _ in range(3):  # Reduced from 5 to 3 runs for faster results
            start = time.perf_counter()
            result2 = optimized.groupAnagrams(test_case.copy())
            end = time.perf_counter()
            optimized_times.append(end - start)

        # Test counting solution with multiple runs
        counting_times = []
        for _ in range(3):  # Reduced from 5 to 3 runs for faster results
            start = time.perf_counter()
            result3 = counting.groupAnagrams(test_case.copy())
            end = time.perf_counter()
            counting_times.append(end - start)
        
        # Calculate and display results
        avg_original = statistics.mean(original_times)
        avg_optimized = statistics.mean(optimized_times)
        avg_counting = statistics.mean(counting_times)
        
        print(f"Original Solution Average Time:  {avg_original:.6f} seconds")
        print(f"Optimized Solution Average Time: {avg_optimized:.6f} seconds")
        print(f"Counting Solution Average Time:  {avg_counting:.6f} seconds")
        print(f"\nSpeed Comparison:")
        print(f"Optimized vs Original: {(avg_original/avg_optimized):.2f}x faster")
        print(f"Counting vs Original:  {(avg_original/avg_counting):.2f}x faster")
        print(f"Counting vs Optimized: {(avg_optimized/avg_counting):.2f}x faster")
        
        # Verify solutions produce same results
        result1_sorted = sorted([sorted(group) for group in result1])
        result2_sorted = sorted([sorted(group) for group in result2])
        result3_sorted = sorted([sorted(group) for group in result3])
        print(f"All results match: {result1_sorted == result2_sorted == result3_sorted}")
        
        # Show example output only for first (small) test case
        if i == 1:
            print("\nExample groupings for test case 1:")
            print("Original solution:", result1)
            print("Optimized solution:", result2)
            print("Counting solution:", result3)

if __name__ == "__main__":
    run_comparison()