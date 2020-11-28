class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_length = 0
    
        for string in s:
            if string in str_list:
                str_list = str_list[str_list.index(string)+1:]
       
            str_list.append(string)   
            
            max_length = max(max_length, len(str_list))
            print(max_length)
        return max_length
