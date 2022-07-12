class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',
                90:'XC',50:'L',40:'XL',10:'X',9:'IX',
                5:'V',4:'IV',1:'I'}
        ans = ""
        if num >= 1000:
            ans += num/1000 * roman[1000]
            num %= 1000
        if num >= 900:
            ans += roman[900]
            num -= 900
        if num >= 500:
            ans += roman[500]
            num -= 500
        if num >= 400:
            ans += roman[400]
            num -= 400
        if num >= 100:
            ans += num/100 * roman[100]
            num %= 100
        if num >= 90:
            ans += roman[90]
            num -= 90
        if num >= 50:
            ans += roman[50]
            num -= 50
        if num >= 40:
            ans += roman[40]
            num -= 40
        if num >= 10:
            ans += num/10 * roman[10]
            num %= 10
        if num >= 9:
            ans += roman[9]
            num -= 9
        if num >= 5:
            ans += roman[5]
            num -= 5
        if num >= 4:
            ans += roman[4]
            num -= 4
        if num:
            ans += num * roman[1]
        return ans

class Solution:

    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def intToRoman(self, num):
        roman = list()
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)

class Solution:
    def intToRoman(self, num):
        romans = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        ans = []
        for value, symbol in romans:
            while num >= value:
                num -= value
                ans.append(symbol)
            if num == 0:
                break
        return "".join(ans)

class Solution:
    def intToRoman(self, num):
        THOUSANDS = ["", "M", "MM", "MMM"]
        HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ans =  THOUSANDS[num // 1000] + HUNDREDS[num % 1000 // 100] + TENS[num % 100 // 10] + ONES[num % 10]
        return ans
