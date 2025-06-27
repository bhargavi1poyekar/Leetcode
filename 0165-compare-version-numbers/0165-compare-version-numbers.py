class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def convert_str_to_num(string):
            num = 0
            for ch in string:
                num = num*10 + int(ch)
            return num
        
        version1 = version1.split('.')
        version2 = version2.split('.')

        length = max(len(version1), len(version2))

        for i in range(length):
            if i >= len(version1):
                ver1 = 0
            else:ver1 = convert_str_to_num(version1[i])

            if i >= len(version2):
                ver2 = 0
            else:
                ver2 = convert_str_to_num(version2[i])
            
            print(ver1, ver2)
            if ver1 < ver2:
                return -1
            elif ver1 > ver2:
                return 1
            
        return 0

