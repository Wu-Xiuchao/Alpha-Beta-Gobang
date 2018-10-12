import numpy as np 
import grade
import minimax
import judge_win
INF = 100000000000 #代表正无穷
N_INF = -INF #代表负无穷

#构建树
def create_Tree(chessboard,current_deep,deep,node_type,index):
	if current_deep == deep or judge_win.judge(chessboard,-1,1,0) == True or judge_win.judge(chessboard,1,-1,0) == True:
		value = grade.get_grade(chessboard)
		return [index,node_type,value,[]] #返回叶子结点
	Root = [] #当前树根
	if node_type == 'max':
		Root = [index,node_type,N_INF,[]]
	else:
		Root = [index,node_type,INF,[]]
	next_posi = []
	w,h = chessboard.shape
	if node_type == 'min':
		for i in range(h):
			for j in range(w):
				if chessboard[i][j] == 0:
					next_posi.append((i,j))
	else:
		flag = np.zeros(chessboard.shape)
		for i in range(h):
			for j in range(w):
				if chessboard[i][j] != 0:
					if i-1 >= 0 and chessboard[i-1][j] == 0 and flag[i-1][j] == 0:
						next_posi.append((i-1,j))
						flag[i-1][j] = 1
					if i-1 >= 0 and j-1 >= 0 and chessboard[i-1][j-1] == 0 and flag[i-1][j-1] == 0:
						next_posi.append((i-1,j-1))
						flag[i-1][j-1] = 1
					if j-1 >= 0 and chessboard[i][j-1] == 0 and flag[i][j-1] == 0:
						next_posi.append((i,j-1))
						flag[i][j-1] = 1
					if i+1 < h and j-1 >= 0 and chessboard[i+1][j-1] == 0 and flag[i+1][j-1] == 0:
						next_posi.append((i+1,j-1))
						flag[i+1][j-1] = 1
					if i+1 < h  and chessboard[i+1][j] == 0 and flag[i+1][j] == 0:
						next_posi.append((i+1,j))
						flag[i+1][j] = 1
					if i+1 < h and j+1 < w and chessboard[i+1][j+1] == 0 and flag[i+1][j+1] == 0:
						next_posi.append((i+1,j+1))
						flag[i+1][j+1] = 1
					if j+1 < w and chessboard[i][j+1] == 0 and flag[i][j+1] == 0:
						next_posi.append((i,j+1))
						flag[i][j+1] = 1
					if i-1 >= 0 and j+1 < w and chessboard[i-1][j+1] == 0 and flag[i-1][j+1] == 0:
						next_posi.append((i-1,j+1))
						flag[i-1][j+1] = 1

	for item in next_posi:
		i = item[0]; j = item[1]
		index = (i,j)
		if node_type == 'max':
			chessboard[i][j] = -1 #AI默认为-1
			Root[-1].append(create_Tree(chessboard,current_deep+1,deep,'min',index))
			chessboard[i][j] = 0
		else:
			chessboard[i][j] = 1
			Root[-1].append(create_Tree(chessboard,current_deep+1,deep,'max',index))
			chessboard[i][j] = 0
	return Root
	
#计算当前应该走哪一步
def compute_next(chessboard,deep):
	Root = create_Tree(chessboard,1,deep,'max',(-1,-1))
	next_step = minimax.get_next(Root)
	return next_step[0],next_step[1] #返回一个坐标