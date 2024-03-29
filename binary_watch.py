'''

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

'''

def get_times(n):
    ans = []
    def backtrack(h=0, m=0, top = 0, bot = 0):
        if top+bot == n:
            if m < 10:
                minute = '0'+str(m)
            else:
                minute = str(m)
            ans.append(str(h)+':'+minute)
        else:
            for i in range(4):
                backtrack(h+2**i,m,top+1,bot)
            for j in range(6):
                backtrack(h, m+2**j,top, bot+1)
    backtrack()
    return ans

print(get_times(1))
        