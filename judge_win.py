import numpy as np 

#判断ME有没有赢
def judge(chessboard,ME,FOE,EMPTY):
	w,h = chessboard.shape #获取棋盘的宽和高
	#横向
	for i in range(h):
		last_chess = FOE
		count = 0
		for j in range(w):
			current_chess = chessboard[i][j]
			if current_chess == EMPTY:
				if last_chess == ME:
					count = 0
			elif current_chess == FOE:
				if last_chess == ME:
					count = 0
			elif current_chess == ME:
				count += 1
				if count == 5:
					return True
			last_chess = current_chess #更新上一个棋子

	#纵向
	for j in range(w):
		count = 0
		for i in range(h):
			current_chess = chessboard[i][j]
			if current_chess == EMPTY:
				if last_chess == ME:
					count = 0
			elif current_chess == FOE:
				if last_chess == ME:
					count = 0
			elif current_chess == ME:
				count += 1
				if count == 5:
					return True
			last_chess = current_chess #更新上一个棋子

	#左上右下
	for i in range(2*w - 1):
		count = 0
		if i < w:
			for k,j in zip(range(w-i-1,w),range(0,i+1)):
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						count = 0
				elif current_chess == ME:
					count += 1
					if count == 5:
						return True
				last_chess = current_chess #更新上一个棋子
		else:
			for k,j in zip(range(0,2*w -1 -i),range(i-w+1,w)):
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						count = 0
				elif current_chess == ME:
					count += 1
					if count == 5:
						return True
				last_chess = current_chess #更新上一个棋子
	#左下右上
	for i in range(2*w - 1):
		last_chess = FOE
		count = 0
		is_live = False
		if i < w:
			for j in range(0,i+1):
				k = i - j
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						count = 0
				elif current_chess == ME:
					count += 1
					if count == 5:
						return True
				last_chess = current_chess #更新上一个棋子
		else:
			for j in range(i-w+1,w):
				k = i - j
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						count = 0
				elif current_chess == ME:
					count += 1
					if count == 5:
						return True
				last_chess = current_chess #更新上一个棋子
	return False