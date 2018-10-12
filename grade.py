#评分 电脑为MAX 玩家为MIN
#得到一盘棋黑棋的评分
#我们对五子棋的评分是简单的把棋盘上的各种连子的分值加起来得到的，对各种连子的基本评分规则如下：
# 成五，100000
# 活四, 10000
# 活三 1000
# 活二 100
# 活一 10
# 如果一侧被封死但是另一侧没有，则评分降一个档次，也就是死四和活三是相同的分
# 死四, 1000
# 死三 100
# 死二 10

import numpy as np 
# 给一个棋盘打分(主角是ME)
def evaluate(chessboard,ME,FOE,EMPTY):
	w,h = chessboard.shape #获取棋盘的宽和高
	live = [0] * 11
	dead = [0] * 11

	#横向
	for i in range(h):
		last_chess = FOE
		count = 0
		is_live = False #默认一侧被封死
		for j in range(w):
			current_chess = chessboard[i][j]
			if current_chess == EMPTY:
				if last_chess == ME:
					if is_live == False:
						dead[count] += 1
					else:
						live[count] += 1
					count = 0
			elif current_chess == FOE:
				if last_chess == ME:
					if is_live == True:
						is_live = False
						dead[count] += 1
					count = 0
			elif current_chess == ME:
				count += 1
				if last_chess == FOE:
					is_live = False
				elif last_chess == EMPTY:
					is_live = True
			last_chess = current_chess #更新上一个棋子
		if is_live == True:
			dead[count] += 1

	#纵向
	for j in range(w):
		last_chess = FOE
		count = 0
		is_live = False
		for i in range(h):
			current_chess = chessboard[i][j]
			if current_chess == EMPTY:
				if last_chess == ME:
					if is_live == False:
						dead[count] += 1
					else:
						live[count] += 1
					count = 0
			elif current_chess == FOE:
				if last_chess == ME:
					if is_live == True:
						is_live = False
						dead[count] += 1
					count = 0
			elif current_chess == ME:
				count += 1
				if last_chess == FOE:
					is_live = False
				elif last_chess == EMPTY:
					is_live = True
			last_chess = current_chess #更新上一个棋子
		if is_live == True:
			dead[count] += 1

	#左上右下
	for i in range(2*w - 1):
		last_chess = FOE
		count = 0
		is_live = False
		if i < w:
			for k,j in zip(range(w-i-1,w),range(0,i+1)):
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						if is_live == False:
							dead[count] += 1
						else:
							live[count] += 1
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						if is_live == True:
							is_live = False
							dead[count] += 1
						count = 0
				elif current_chess == ME:
					count += 1
					if last_chess == FOE:
						is_live = False
					elif last_chess == EMPTY:
						is_live = True
				last_chess = current_chess #更新上一个棋子
			if is_live == True:
				dead[count] += 1
		else:
			for k,j in zip(range(0,2*w -1 -i),range(i-w+1,w)):
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						if is_live == False:
							dead[count] += 1
						else:
							live[count] += 1
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						if is_live == True:
							is_live = False
							dead[count] += 1
						count = 0
				elif current_chess == ME:
					count += 1
					if last_chess == FOE:
						is_live = False
					elif last_chess == EMPTY:
						is_live = True
				last_chess = current_chess #更新上一个棋子
			if is_live == True:
				dead[count] += 1
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
						if is_live == False:
							dead[count] += 1
						else:
							live[count] += 1
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						if is_live == True:
							is_live = False
							dead[count] += 1
						count = 0
				elif current_chess == ME:
					count += 1
					if last_chess == FOE:
						is_live = False
					elif last_chess == EMPTY:
						is_live = True
				last_chess = current_chess #更新上一个棋子
			if is_live == True:
				dead[count] += 1
		else:
			for j in range(i-w+1,w):
				k = i - j
				current_chess = chessboard[k][j]
				if current_chess == EMPTY:
					if last_chess == ME:
						if is_live == False:
							dead[count] += 1
						else:
							live[count] += 1
						count = 0
				elif current_chess == FOE:
					if last_chess == ME:
						if is_live == True:
							is_live = False
							dead[count] += 1
						count = 0
				elif current_chess == ME:
					count += 1
					if last_chess == FOE:
						is_live = False
					elif last_chess == EMPTY:
						is_live = True
				last_chess = current_chess #更新上一个棋子
			if is_live == True:
				dead[count] += 1
	value = 0
	for c in range(5,11):
		value = value + (100000 * (live[c] + dead[c]))
	value = value + 10000 * live[4] + 1000 * live[3] + 100 * live[2] + 10 * live[1] + 1000 * dead[4] + 100 * dead[3] + 10 * dead[2]
	return value

#获得整个棋盘的评分
def get_grade(chessboard):
	r1 = evaluate(chessboard,-1,1,0)
	r2 = evaluate(chessboard,1,-1,0)
	return r1 - r2



	
