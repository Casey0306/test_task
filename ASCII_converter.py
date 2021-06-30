class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        numb = columnNumber
        ostatok = 1
        result = str()
        flag = False
        if numb % 26 == 0:
            flag=True
        while ostatok > 0:
            ostatok = numb//26
            if numb == 26:
                result = chr(numb + 64) + result
                ostatok = 0
            elif numb - ostatok*26 == 0:
                result = chr(26 + 64) + result
                numb = numb//26
            else:
                if flag and numb > 1:
                    result = chr(numb - ostatok*26 + 63) + result
                else:
                    result = chr(numb - ostatok*26 + 64) + result
                numb = numb//26
        return result

test = Solution()
print(test.convertToTitle(2147483647))