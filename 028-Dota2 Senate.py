class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        rad=deque()
        dire=deque()
        for i,s in enumerate(senate):
            if s=='R':
                rad.append(i)
            else:
                dire.append(i)
        while rad and dire:
            rid=rad.popleft()
            did=dire.popleft()
            if rid<did:
                rad.append(rid+n)
            else:
                dire.append(did+n)
        return "Radiant" if rad else "Dire"


'''SOLVED BY ADIT MUGDHA DAS'''