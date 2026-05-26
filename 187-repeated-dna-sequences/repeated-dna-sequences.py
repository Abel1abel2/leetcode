class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        k=10
        sub=set()
        res=set()
        for i in range(n-k+1):
            if s[i:k+i] in sub:
                res.add(s[i:k+i])
            sub.add(s[i:k+i])
        arr=[*list(res)]
        return arr
