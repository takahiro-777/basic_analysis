#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://qiita.com/mzmttks/items/82ea3a51e4dbea8fbc17

"""
import pulp
problem = pulp.LpProblem('Problem Name', pulp.LpMinimize) # 最小化する場合
problem = pulp.LpProblem('Problem Name', pulp.LpMaximize) # 最大化する場合
"""

#import modules
import pulp

#functions

#main function
if __name__ == '__main__':
    #最小化問題と宣言
    problem = pulp.LpProblem('test', pulp.LpMinimize)

    #pulp.LpVariable('変数名', 変数の最小値, 変数の最大値, 変数の種類)
    a = pulp.LpVariable('a', 0, 1)
    b = pulp.LpVariable('b', 0, 1)

    #目的関数を作成
    problem += a + 2*b

    #制約条件の設定
    problem += a >= 0
    problem += b >= 0.1
    problem += a + b == 0.5

    #解けるかどうかの判定
    status = problem.solve()
    print "Status", pulp.LpStatus[status]

    #問題の概要の出力
    print problem

    #結果の出力
    print "Result"
    print "a", a.value()
    print "b", b.value()
