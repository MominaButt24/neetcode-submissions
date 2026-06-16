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
        # k = int(s[-1])
        # new_s = s[:-1]
        # res_str = ""
        # res_list = list()
        # for i in range(1, len(new_s)):
        #     if  new_s[i] == '#':
        #         for j in range(i+1, i+int(new_s[i-1])+1):
        #             res_str += chr((ord(new_s[j]) - k) % 260)
        #         res_list.append(res_str)
        #         res_str = ""

        # if res_str:
        #     res_list.append(res_str)
        # return res_list
        k = int(s[-1])   # Extract the key
        new_s = s[:-1]   # Strip the key from the end
        
        res_list = list()
        i = 0
        
        while i < len(new_s):
            # 1. Find the delimiter '#' to parse multi-digit lengths correctly
            j = i
            while new_s[j] != '#':
                j += 1
                
            # 2. Extract the exact full length of the upcoming word
            length = int(new_s[i:j])
            
            # 3. Process the exact block of encrypted characters
            res_str = ""
            word_start = j + 1
            word_end = word_start + length
            
            for index in range(word_start, word_end):
                res_str += chr((ord(new_s[index]) - k) % 260)
                
            res_list.append(res_str)
            
            # 4. Jump your pointer past the current word to the next length prefix
            i = word_end
            
        return res_list
        
                
