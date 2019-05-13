#coding:utf-8
from __future__ import division

import random
#树节点
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#数字全排列
import itertools

def shu_list(li):
    oprand_list=[]
    for i in itertools.permutations(li,4):
        a=list(i)

        oprand_list.append(a)
    return oprand_list
#运算符排列的生成
from itertools import product
op=["+","-","*","÷"]
operators_list=[]
for i in [0,0,0,0]:
    a=op.pop(i)
    ops=list(product(op,repeat=3))
    op.append(a)
    #print(ops)
    for j in range(len(ops)) :
        q=list(ops[j])
        operators_list.append(q)
#print(e)
#print(len(e))

def one_expression_tree(operators, operands):
    root_node = Node(operators[0])
    operator1 = Node(operators[1])
    operator2 = Node(operators[2])
    operand0 = Node(operands[0])
    operand1 = Node(operands[1])
    operand2 = Node(operands[2])
    operand3 = Node(operands[3])
    root_node.left = operator1
    root_node.right =operand0
    operator1.left = operator2
    operator1.right = operand1
    operator2.left = operand2
    operator2.right = operand3
    return root_node

def two_expression_tree(operators, operands):
    root_node = Node(operators[0])
    operator1 = Node(operators[1])
    operator2 = Node(operators[2])
    operand0 = Node(operands[0])
    operand1 = Node(operands[1])
    operand2 = Node(operands[2])
    operand3 = Node(operands[3])
    root_node.left = operator1
    root_node.right =operator2
    operator1.left = operand0
    operator1.right = operand1
    operator2.left = operand2
    operator2.right = operand3
    return root_node

#根据两个数和一个符号，计算值
def cal(a, b, operator):
    return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '÷' and float(a)/float(b)


def cal_tree(node):
    if node.left is None:
        return node.val
    return cal(cal_tree(node.left), cal_tree(node.right), node.val)


def str_expression_tree(node):
    if node is None :
        return
    if node.left is None and node.right is None:
        return str(node.val)
    else:
        return '('+str_expression_tree(node.left) + str(node.val) + str_expression_tree(node.right) + ')'


#def print_node(node):


def print_expression_tree(root):
    return str_expression_tree(root) + '=24'


def calculate(nums):
    nums_possible = shu_list(nums)
    operators_possible =operators_list
    # print(operators_possible)
    goods_noods = []
    for nums in nums_possible:
        for op in operators_possible:
            #print(op)
            node = one_expression_tree(op, nums)
            try:
                if cal_tree(node) == 24:
                    goods_noods.append(node)
                node = two_expression_tree(op, nums)
                if cal_tree(node) == 24:
                    goods_noods.append(node)
            except ZeroDivisionError:
                pass
    #map(lambda node: print_expression_tree(node), goods_noods)
    return goods_noods
#jisuanshu=[]
#for i in range(4):

#         jisuanshu.append(input("请输入四个1-10之间的数："))

#for j in range(len(calculate(jisuanshu))):

#      print (print_expression_tree((calculate(jisuanshu))[j]))