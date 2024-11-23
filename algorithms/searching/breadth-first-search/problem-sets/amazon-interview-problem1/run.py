from solution import solution
from test_cases import tests 

if __name__ == '__main__':
    for i in range(len(tests)):
        _input = tests[i][0]
        _output = tests[i][1]
        sol = solution(_input)
        if sol == _output:
            print('Testcase ', i , ': passed')
        else:
            print('Testcase ', i, ': failed')
            print('Output:          ', sol )
            print('Expected Output: ', _output)