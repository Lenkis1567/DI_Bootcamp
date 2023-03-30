def check_win(matrix:list) -> str:
    results = ''
    for i in range(0, len(matrix)):
        for y in range(0, len(matrix)): 
            if (matrix[i][y] == matrix[i][y+1] == matrix[i][y+2] !=""):
                results = matrix[i][0]
            break
        if (matrix[i][y] == matrix[i+1][y] == matrix[i+2][y] !=""):
                results = matrix[i][y]
        break
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] !=""):
    results = matrix[0][0]
    break
    elif (matrix[2][0] == matrix[1][1] == matrix[0][2] !=""):
        results = matrix[2][0]
    break
    else:
        results = "z"
    return(results)

list_game = [['o','o','o'],['o','o', 'x'],['x', 'x', 'x']]                   
print(check_win(list_game))
        
