class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr=[]
        prefix=""
        i=0
        while i<len(strs):
            j=i+1
            while j<len(strs):
                for a,b in zip(strs[i],strs[j]):
                    if a==b:
                        prefix+=a
                    else:
                        break
                arr.append(prefix)
                prefix=""
                j+=1
            i+=1
        if strs==[]:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            prefix=min(arr,key=len)
            return prefix
            