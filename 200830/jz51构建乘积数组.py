#题目描述
#给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
#对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
#题解 讨论 通过的代码笔记 纠错 收藏
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here

        B =[1] * len(A) 

        for i in range(1,len(B)):
            B[i] = B[i - 1] * A[i - 1]

        for i in range(len(A) - 2, -1 -1):
            tmp *= A[i + 1]
            B[i] = B[i] * tmp

        return B
