from collections import deque

def coffeeMachine(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = {}
    queue = deque([])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'p':
                queue.append(((i,j), (i,j)))
                visited[(i,j)] = []
    
    def check(person, row, col):
        # print('check: ', row, ',', col)
        if row < 0  or row >= m:
            return False
        if col >= n or col < 0:
            return False
        if matrix[row][col] != '.':
            return False 
        if [row, col] in visited[person]:
            return False 
        return True
    
    def found():
        # print(visited)
        res = None
        for p, e in visited.items():
            if res == None:
                res = e
            else:
                res = [idx for idx in e if idx in res]
        return res

    
    while queue:
        person, cur_spot = queue.popleft()
        # Add to visited
        if person != cur_spot:
            visited[person].append(cur_spot)

        # up
        if check(person, cur_spot[0]-1, cur_spot[1]):
            queue.append((person, (cur_spot[0]-1, cur_spot[1])))
        # down
        if check(person, cur_spot[0]+1, cur_spot[1]):
            queue.append((person, (cur_spot[0]+1, cur_spot[1])))
        # left
        if check(person, cur_spot[0], cur_spot[1]-1):
            queue.append((person, (cur_spot[0], cur_spot[1]-1)))
        # right
        if check(person, cur_spot[0], cur_spot[1]+1):
            queue.append((person, (cur_spot[0], cur_spot[1]+1)))
        

        res = found()
        if len(res) > 0:
            return res 
    return None


def solution(i):
    return set(coffeeMachine(i))