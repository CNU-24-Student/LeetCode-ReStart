from typing import List
import json

def function(temperatures:List[int]) -> List[int]:
    n = len(temperatures)
    ans = [0] * n
    st = []
    for i in range(n-1,-1,-1):
        t = temperatures[i]
        while st and t >= temperatures[st[-1]]:
            st.pop()
        if st:
            ans[i] = st[-1] - i
        st.append(i)
    return ans

if __name__ == "__main__":
    arr = json.loads(input())
    print(function(arr))