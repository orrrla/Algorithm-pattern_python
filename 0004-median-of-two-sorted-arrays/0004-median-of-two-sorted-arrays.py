class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a,b = b,a 
        m,n = len(a),len(b)
        a = [-inf] + a + [inf]
        b = [-inf] + b + [inf]

        i = 0
        j = (m+n+1)//2-i

        while True:
            if a[i]<=b[j+1] and b[j]<a[i+1]:
                num1 = max(a[i],b[j])
                num2 = min(a[i+1],b[j+1])
                return (num1+num2)/2 if (m+n)%2 == 0 else num1
            i+=1
            j-=1