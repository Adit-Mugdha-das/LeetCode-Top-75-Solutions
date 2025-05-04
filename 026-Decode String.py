class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        curnum=0
        curstr=""
        for ch in s:
            if ch.isdigit():
                curnum=curnum*10+int(ch)
            elif ch=="[":
                st.append((curstr,curnum))
                curstr=""
                curnum=0
            elif ch=="]":
                prev,num=st.pop()
                curstr=prev+num*curstr
            else:
                curstr+=ch
        return curstr

'''SOLVED BY ADIT MUGDHA DAS'''