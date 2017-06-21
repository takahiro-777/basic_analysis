#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://www.amazon.co.jp/Chainer%E3%81%AB%E3%82%88%E3%82%8B%E5%AE%9F%E8%B7%B5%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92-%E6%96%B0%E7%B4%8D%E6%B5%A9%E5%B9%B8/dp/4274219348
#http://rest-term.com/archives/2999/

#import modules
import numpy as np

#functions
def generate_basic_array():
    print("======you run generate_basic_array function=====")
    #generate_basic_array
    data1 = np.array([1,2,3,4,5])
    data2 = np.arange(10)
    data3 = np.array([[0,1,2],[3,4,5]])
    data4 = np.arange(6).reshape(2,3)
    data5 = np.arange(27).reshape(3,3,3)
    data6 = np.zeros(5)
    #区間(0,1)の一様分布に従う乱数を3個作成
    data7 = np.random.uniform(0,1,3)
    #平均1.5、標準偏差2の正規分布に従う乱数を3個作成
    data8 = np.random.normal(1.5,2.0,3)
    #要素をシャッフルした配列の生成
    data9 = np.random.permutation(range(6))
    print(data4)
    print(data5.shape)
    print(data7)
    print(data8)
    print(data9)

def processing_basic_array():
    print("======you run processing_basic_array function=====")
    #processing basic array
    data1 = np.arange(30).reshape(5,6)
    print(data1)
    print(data1[[0,2,4],:])
    print(data1[:,[0,2,4,5]])
    data1[data1 % 2 == 0] = -1
    print(data1)

def array_operation():
    print("======you run array_operation function=====")
    #matrix -> matrix
    data1 = np.arange(1,7).reshape(2,3)
    print("・ori==")
    print(data1)
    print("・+1==")
    print(data1+1)
    print("・multi==")
    print(data1**2)
    print("・log==")
    print(np.log(data1))

    #matrix -> value
    print("=====")
    print(np.sum(data1))
    print(np.mean(data1))

    #matrix -> vector
    print(np.sum(data1,axis=0))
    print(np.sum(data1,axis=1))

def save_and_load():
    print("======you run save_and_load function=====")
    #data load
    #data = np.loadtxt("../data/numpy_sample.data")

    #data save
    data = np.random.randn(10000).reshape(100,100)
    np.savetxt("../data/numpy_sample.data",data)
    print("success save array")

def data_type():
    print("======you run data_type function=====")
    #when array is generated
    print("・when array is generated=====")
    data1 = np.array([1,2,3,4,5])    #dtype: int64
    print("data1.dtype:  "+str(data1.dtype))
    data2 = np.array([1.0,2.0,3.0,4.0,5.0])    #dtype:  float64
    print("data2.dtype:  "+str(data2.dtype))
    print("data2.itemsize:  "+str(data2.itemsize))
    data3 = np.array([1,2,3], dtype=np.int32)   #32ビット符号付き整数
    print("data3.dtype:  "+str(data3.dtype))
    data4 = np.array([1,2,3], dtype=np.uint8)  #8ビット符号無し整数 (画像処理ではよく使われる)
    print("data4.dtype:  "+str(data4.dtype))

    #update array data_type
    print("・update array data_type=====")
    data1.astype(np.int32)  #int64 -> int32
    print("data1.dtype:  "+str(data1.dtype))
    data2.astype(np.int64)  #float64 -> int64
    print("data2.dtype:  "+str(data2.dtype))

def sort_array():
    print("======you run sort_array function=====")
    ## numpy.sort() で配列をソートしてコピーを返す
    data1= np.random.randint(0,100,10)
    print(data1)    #array([75, 24, 74, 49, 93, 18, 19, 85, 73, 90])
    print(np.sort(data1))    #array([18, 19, 24, 49, 73, 74, 75, 85, 90, 93])

    ## ndarray.sort() で配列を破壊的(in-place)にソートする
    data1.sort()
    print(data1)    #array([18, 19, 24, 49, 73, 74, 75, 85, 90, 93])

    ## 多次元配列の場合
    data2 = np.array([[1,4,2],[9,6,8],[5,3,7]])
    print(data2)
    """array([[1, 4, 2],
            [9, 6, 8],
            [5, 3, 7]])"""
    print(np.sort(data2))
    """array([[1, 2, 4],
            [6, 8, 9],
            [3, 5, 7]])"""

    ## 軸を指定する (ここでは列でソート)
    print(np.sort(data2, axis=0))
    """array([[1, 3, 2],
            [5, 4, 7],
            [9, 6, 8]])"""

    ## 一次元配列にしてソート
    print(np.sort(data2, axis=None))   #array([1, 2, 3, 4, 5, 6, 7, 8, 9])

def generate_array_advance():
    print("======you run generate_array_advance function=====")
    #単位行列 (正方行列なので引数は1つ)
    data1 = np.identity(3)
    print("・np.identity(3)")
    print(data1)
    """array([[ 1.,  0.,  0.],
            [ 0.,  1.,  0.],
            [ 0.,  0.,  1.]])"""
    #numpy.linspace() で生成、arange() と似ているが要素数を指定できる
    print("・np.linspace(1, 4, 6)")
    data2 = np.linspace(1, 4, 6)
    print(data2)    #array([ 1. ,  1.6,  2.2,  2.8,  3.4,  4. ])
    #numpy.tile() で生成、要素を繰り返した配列を返す
    print("・np.tile([0,1,2,3,4], 2)")
    data3 = np.tile([0,1,2,3,4], 2)
    print(data3)    #array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4])

#main function
if __name__ == '__main__':
    generate_basic_array()
    #processing_basic_array()
    array_operation()
    #save_and_load()
    data_type()
    sort_array()
    generate_array_advance()
