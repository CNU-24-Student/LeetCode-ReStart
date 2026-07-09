from typing import List
import json

def function(matrix:List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

if __name__== "__main__":
    userInput = input()
    matrix = json.loads(userInput)
    function(matrix)
    print(matrix)