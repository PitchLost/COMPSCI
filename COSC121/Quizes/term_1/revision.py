class Solution:
    def isValid(self, s: str) -> bool:
        the_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for i, char in enumerate(s):
            if char in the_map:

                print(i, s[i + 1])
                
                if i + 1 >= len(s) or s[i + 1] != the_map[char]:
                    return False
        
        return True