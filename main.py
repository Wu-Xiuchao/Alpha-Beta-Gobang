import pygame
# import pygame.locals for easier access to key coordinates
from pygame.locals import *
import numpy as np
import compute
import threading
import judge_win
import time

pygame.init()

screen = pygame.display.set_mode((770,770))
pygame.display.set_caption('gobang')
screen.fill((255,193,37))


font=pygame.font.Font(None,100)
text=font.render("",1,(255,10,10))
#获取中心的坐标
center=(screen.get_width()/2,screen.get_height()/2)

chessboard = np.zeros((10,10))

running = True

B = -1 #黑方AI
W = 1 #白方 玩家
turn = W #白方先下
Game_end = False #游戏结束
Winner = 0 #赢家
last_chess = (-1,-1)

def draw(chessboard):
    for i in range(1,11):
        pygame.draw.line(screen,(0,0,0),[i*70,70],[i*70,700],5)
        pygame.draw.line(screen,(0,0,0),[70,i*70],[700,i*70],5)
    for i in range(10):
        for j in range(10):
            if chessboard[i][j] == -1:
                pygame.draw.circle(screen,(0,0,0),[(i+1)*70,(j+1)*70],20,20)
            elif chessboard[i][j] == 1:
                pygame.draw.circle(screen,(255,255,255),[(i+1)*70,(j+1)*70],20,20)
    if last_chess[0] != -1:
    	pygame.draw.circle(screen,(0,0,255),[(last_chess[0]+1)*70,(last_chess[1]+1)*70],20,5)

#AI思考线程
def AI_mind():
	global last_chess
	global Winner
	while running:
		if Winner != 0:
			break
		global turn
		if turn == B:
			print('AI下棋中...')
			copy = chessboard.copy()
			n_x,n_y = compute.compute_next(copy,3)
			chessboard[n_x][n_y] = turn
			turn = turn * -1
			print('AI下完了...')
			last_chess = (n_x,n_y)
			if judge_win.judge(chessboard,-1,1,0) == True:
				turn = 2
				Winner = -1

#游戏结束
def Game_Over():
	global text
	while running:
		if Winner == 1:
			text=font.render("You WIN",1,(255,10,10))
		elif Winner == -1:
			text=font.render("You Lose",1,(255,10,10))


#开辟AI思考线程
AI = threading.Thread(target = AI_mind, name = 'AIThread')
AI.start()

check = threading.Thread(target = Game_Over, name = 'game_over')
check.start()

FPS = 30
clock = pygame.time.Clock()
while running:
	# 设置屏幕刷新频率
	clock.tick(FPS)
	#事件监听
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type ==  MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			x = (x//70 + x%70//35) - 1
			y = (y//70 + y%70//35) - 1
			if x>=0 and x<10 and y>=0 and y<10 and turn == W and chessboard[x][y] == 0:
				chessboard[x][y] = turn
				turn = turn * -1 #交换
				last_chess = (x,y)
				if judge_win.judge(chessboard,1,-1,0) == True:
					turn = 2
					Winner = 1

	draw(chessboard)
	if Winner != 0:
		textpos = text.get_rect(center=center)
		screen.blit(text,textpos)
	pygame.display.flip()


