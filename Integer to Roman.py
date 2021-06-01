class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        if num >= 1000:
            s = 'M'*(num // 1000)
            num = num % 1000
        if num >= 500:
            s += 'D'*(num // 500)
            num = num % 500
        if num >= 100:
            s += 'C'*(num // 100)
            num = num % 100
        if num >= 50:
            s += 'L'*(num // 50)
            num = num % 50
        if num >= 10:
            s += 'X'*(num // 10)
            num = num % 10
        if num >= 5:
            s += 'V'*(num // 5)
            num = num % 5
        if num >= 1:
            s += 'I'*(num // 1)
            num = num % 1
        while 'VIIII' in s:
            s = s.replace('VIIII', 'IX')
        while 'IIII' in s:
            s = s.replace('IIII', 'IV')

        while 'LXXXX' in s:
            s = s.replace('LXXXX', 'XC')
        while 'XXXX' in s:
            s = s.replace('XXXX', 'XL')

        while 'DCCCC' in s:
            s = s.replace('DCCCC', 'CM')
        while 'CCCC' in s:
            s = s.replace('CCCC', 'CD')

        return s
