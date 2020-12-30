def isValidSudoku(board):
    row,col,block = set(),set(),set()
    for i in range(9):
        for j in range(9):
            if(board[i][j] != '.'):
                r_key=(i,board[i][j])
                c_key=(j,board[i][j])
                b_key=(i//3),j//3,board[i][j])
                if( (r_key in row) or (c_key in col) or (b_key in block)):
                    return False
                row.add(r_key)
                col.add(c_key)
                block.add(b_key)
    return True


#Kinda dont get this one but will study more
#basically created a list for row col and block
#values will be inserted into row col and block and if there is any matching value it is a false
#hazy on how block gives any problems though because only rows and columns matter