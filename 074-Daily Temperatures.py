class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]  
        for i,t in enumerate(temperatures):
            while st and temperatures[i]>temperatures[st[-1]]:
                pre=st.pop()
                ans[pre]=i-pre
            st.append(i)
        return ans

'''SOLVED BY ADIT MUGDHA DAS'''