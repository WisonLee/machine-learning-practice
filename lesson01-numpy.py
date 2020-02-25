from numpy import *

# 数组

# 一维数组
one_array = array([1, 2, 3]) #[1 2 3]
# 一些方法
ones_data = ones(3) #[1. 1. 1.]
zeros(3) #[0 0 0]
random.random(3) #[0.26963245 0.32582268 0.19486039]

#数组运算
one_array + ones_data # [2. 3. 4.]
one_array - ones_data # [0. 1. 2.]
one_array * ones_data # [1. 2. 3.]
one_array / ones_data # [1. 2. 3.]

#聚合函数
one_array.max() # 3
one_array.min() # 1
one_array.sum() # 6

#矩阵
'''
[[1 2]
 [3 4]]
 '''
matrix_array = array([[1,2],[3,4]])

'''
[[1. 1.]
 [1. 1.]]
 '''
ones_matrix = ones((2,2))

'''
[[0. 0.]
 [0. 0.]]
 '''
zeros_matrix = zeros((2,2))

'''
[[0.029876   0.87287105]
 [0.12177904 0.92707455]]
 '''
random_matrix = random.random((2,2))

'''
[[2. 3.]
 [4. 5.]]
'''
matrix_array + ones_matrix

'''
[[0. 1.]
 [2. 3.]]
'''
matrix_array - ones_matrix

'''
[[1. 2.]
 [3. 4.]]
'''
matrix_array * ones_matrix

'''
[[ 1  4]
 [ 9 16]]
 '''
square(matrix_array)

matrix_array.max() # 4
matrix_array.min() # 1
matrix_array.sum() # 10
matrix_array.max(axis=0) #按列聚合 [3 4]
matrix_array.max(axis=1) # 按行聚合[2 4]

#矩阵索引
matrix_array[0,1] # 2
matrix_array[0:1] # [[1 2]]
matrix_array[0:1,1] # [2]

#矩阵转置 重塑
'''
[[1 3]
 [2 4]]
'''
matrix_array.T

'''
[[1 2]
 [3 4]]
'''
matrix_array.reshape(2,2)


#多维数组
#n_array = array([[[1,2][3,4]],[[5,6],[7,8]]])

