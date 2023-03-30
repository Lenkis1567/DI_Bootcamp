def check_win(matrix:list) -> str:
    results = ''
    for i in range(0, len(matrix)):
        if (matrix[i][0] == matrix[i][1] == matrix[i][2] !=""):
            results = matrix[i][0]
            break
        else:       
            for y in range(0, len(matrix)): 
                if (matrix[0][y] == matrix[1][y] == matrix[2][y] !=""):
                    results = matrix[0][y]
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

list_game = [['x','o','o'],['o','o', 'x'],['o', 'x', 'x']]                   
print(check_win(list_game))
        
