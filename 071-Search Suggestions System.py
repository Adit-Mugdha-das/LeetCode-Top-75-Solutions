class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        pre=""
        for c in searchWord:
            pre+=c
            i=bisect.bisect_left(products,pre)
            m=[]
            for j in range(i,min(i+3,len(products))):
                if products[j].startswith(pre):
                    m.append(products[j])
                else:
                    break
            res.append(m)
        return res
    
'''SOLVED BY ADIT MUGDHA DAS'''