#Leetcode
#206.快乐数
#对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def isHappy(self, n: int) -> bool:
        
        while 1:
            sum = 0
            n = str(n)
            for i in n:
                sum = int(i)**2 + sum
            n = sum
            if n == 4:
                return False
            if n == 1:
                return True
