class Solution:

    def encode(self, strs: List[str]) -> str:
        #substitution encoding
        k = 2
        for i in range(len(strs)):
            new_str =  f"{str(len(strs[i]))}#"
            for ch in strs[i]:
                new_str += chr((ord(ch) + k) % 260)
            strs[i] = new_str

        strs.append(str(k))
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        k = int(s[-1])
        new_s = s[:-1]
        res_list = list()
        i =  0
        res_str = ""
        while i < len(new_s):
            j = i
            while new_s[j] != '#':
              j+=1

            length = int(new_s[i:j])
            i = j+1+length
            
            for ind in range(j+1, i):
                res_str += chr((ord(new_s[ind]) - k) % 260)
            res_list.append(res_str)
            res_str = ""
            


        if res_str:
            res_list.append(res_str)
        return res_list
        
                
