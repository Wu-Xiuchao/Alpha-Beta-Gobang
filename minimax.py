#minimax算法实践
import random
INF = 100000000000 #代表正无穷
N_INF = -INF #代表负无穷
# 叶子节点：编号，类型，值，孩子
O = ['O','max',3,[]]
P = ['P','max',17,[]]
Q = ['Q','max',2,[]]
R = ['R','max',12,[]]
S = ['S','max',15,[]]
T = ['T','max',25,[]]
U = ['U','max',0,[]]
V = ['V','max',2,[]]
W = ['W','max',5,[]]
X = ['X','max',3,[]]
Y = ['Y','max',2,[]]
Z = ['Z','max',14,[]]

#非叶子节点：编号，类型，值，孩子
H = ['H','min',INF,[O,P]]
I = ['I','min',INF,[Q,R]]
J = ['J','min',INF,[S]]
K = ['K','min',INF,[T,U]]
L = ['L','min',INF,[V,W]]
M = ['M','min',INF,[X]]
N = ['N','min',INF,[Y,Z]]

D = ['D','max',N_INF,[H,I]]
E = ['E','max',N_INF,[J,K]]
F = ['F','max',N_INF,[L,M]]
G = ['G','max',N_INF,[N]]

B = ['B','min',INF,[D,E]]
C = ['C','min',INF,[F,G]]

#A 代表一棵树的根
A = ['A','max',N_INF,[B,C]]

#每个结点产出一个值
def generate_value(Node,alpha,beta):
	#叶子节点，直接返回
	if len(Node[-1]) == 0: return Node[-2]
	#非叶子节点
	children = Node[-1] #孩子集合
	for child in children:
		if beta <= alpha: break
		c_value = generate_value(child,alpha,beta)
		if Node[1] == 'min' and c_value < beta:
			beta = c_value
		elif Node[1] == 'max' and c_value > alpha:
			alpha = c_value
	if Node[1] == 'min':
		return beta
	else:
		return alpha

#Alpha-Beta Prune Algorithm
def Alpha_Beta_Prune_Algorithm(Root):
	return generate_value(Root,N_INF,INF)

def get_next(Root):
	max_value = N_INF
	next_step_list = []
	for child in Root[-1]:
		value = generate_value(child,N_INF,INF)
		if value > max_value:
			next_step_list.clear()
			max_value = value
			next_step_list.append(child[0])
		elif value == max_value:
			next_step_list.append(child[0])

	length = len(next_step_list)
	index = random.randint(0,length-1)
	return next_step_list[index]
