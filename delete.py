def lengthOfLongestSubstring(s: str) -> int:
    subs_dict = {}
    longest_count = 0
    curr_count = 0
        
    for sub in s:
        if sub in subs_dict or sub == s[-1]:
            subs_dict = {}
            
            if sub == s[-1]:
                curr_count += 1
            
            if longest_count < curr_count:
                longest_count = curr_count 
                
            curr_count = 0
        else:
            subs_dict[sub] = 1
            curr_count += 1
            
            
    return longest_count

print(lengthOfLongestSubstring("eea"))