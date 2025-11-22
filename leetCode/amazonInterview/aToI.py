# https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, s: str) -> int:
        # "    -123a"
        
        result = 0
        positive = True
        found_number = False
        maxpos = (2**31) -1
        maxmin = -(2**31)
        
        for i in range(0,(len(s))):
            if(found_number):
                if(not s[i].isdigit()):
                    break
                    
                if(s[i].isdigit()):
                    if(result == 0):
                        result += int(s[i])
                    else:
                        result = result*10
                        result += int(s[i])
                    continue
            else:
                if(s[i] == ' '):
                    continue
                
                if(s[i] == '+'):
                    found_number = True
                    continue
                
                if(s[i] == '-'):
                    found_number = True
                    positive = False
                    continue
                    
                if(s[i].isdigit()):
                    found_number = True
                    if(result == 0):
                        result += int(s[i])
                    else:
                        result = result*10
                        result += int(s[i])
                else:
                    break
                        
        if(not positive):
            result = result * -1
    
        if(result > maxpos):
            result = maxpos
        if(result < maxmin):
            result = maxmin
            
        return result
            