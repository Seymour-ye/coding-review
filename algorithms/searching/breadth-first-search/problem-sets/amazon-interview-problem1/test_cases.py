input1 = [['x', '.', 'x'],
         ['.', '.', '.'],
         ['.', 'x', 'p']]
output1 = {(1,2)}

input2 = [['p', '.', '.'],
         ['.', 'x', '.'],
         ['.', 'x', 'p']]
output2 = {(0,2)}

input3 = [['p', '.', 'p'],
         ['.', '.', '.'],
         ['x', 'x', 'p']]
output3 = {(1,1)}


tests = [(input1, output1),
         (input2, output2),
         (input3, output3)]