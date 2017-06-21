#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://qiita.com/hitsumabushi845/items/270d81c5c8017014df95

#import modules
import argparse
import networkx as nx

#functions
def add_node_example(Graph):
    #ノードの追加
    Graph.add_node('hoge')
    Graph.add_node('fuga')
    print(Graph.nodes())

    #ノードのまとめての追加
    Graph.add_nodes_from(['foo','bar'])
    print(Graph.nodes())

    #属性付きノードの追加
    Graph.add_node('hoge', color = 'green')
    Graph.add_node('fuga', color = 'red')
    Graph.add_node('foo', color = 'white', lang = 'en')
    print(Graph.nodes(data=True))

    #ノードの削除
    #Graph.remove_node('bar')
    #print(Graph.nodes(data=True))

    return(Graph)

def add_edge_example(Graph):
    #エッジの追加
    Graph.add_edge('hoge','fuga')
    Graph.add_edge('foo','bar')
    print(Graph.edges())
    print(Graph.edges(data=True))

    #重み付きエッジの追加
    Graph.add_edge('foo', 'hoge', weight=0.7)
    Graph.add_edge('bar', 'fuga', weight=0.5)
    print(Graph.edges(data=True))

    #まとめて重み付きエッジの追加
    Graph.add_weighted_edges_from([('hoge','fuga',0.4),('foo','bar',0.2)])
    print(Graph.edges(data=True))

    return Graph

#main function
if __name__ == '__main__':
    #オブジェクトの作成
    graph = nx.DiGraph()

    #ノードの追加
    print("=====add nodes=====")
    graph = add_node_example(Graph=graph)

    #エッジの追加
    print("=====add edges=====")
    graph = add_edge_example(Graph=graph)

    #グラフの削除
    #print("=====delete graph=====")
    #graph.clear()
    #print(graph.nodes())
    #print(graph.edges())

    #パスの出力
    print("=====export paths=====")
    for path in nx.all_simple_paths(graph, source='foo', target='bar'):
        print(path)
