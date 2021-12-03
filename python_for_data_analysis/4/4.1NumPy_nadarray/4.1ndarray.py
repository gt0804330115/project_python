"""
    ndarray:多维数组对象
"""
import numpy as np

# 4.1.1 生成ndarray
data = np.random.randn(2, 3)
print(data)
print(data * 10)
print(data + data)
print(data.shape)

# 生成ndarray   函数array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)  # [6.  7.5 8.  0.  1. ]
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
# [[1 2 3 4]
#  [5 6 7 8]]
print(arr2.ndim)  # 2
print(arr2.shape)  # (2, 4)
print(arr1.dtype)  # float64
print(arr2.dtype)  # int32
print(np.zeros(10))  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(np.zeros((3, 6)))
# [[0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]]
print(np.empty((2, 3, 2)))
# [[[0. 0.]
#   [0. 0.]
#   [0. 0.]]
#
#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]]]

# arange 是Python内建函数range的数组版
print(np.arange(15))  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# 4.1.2 ndarray的数据类型
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)  # float64
print(arr2.dtype)  # int32

# 转换数组的数据类型  --> astype
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # int32
float_arr = arr.astype(np.float64)
print(float_arr.dtype)  # float64

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)  # [ 3.7 -1.2 -2.6  0.5 12.9 10.1]
print(arr.astype(np.int32))  # [ 3 -1 -2  0 12 10]
# 字符串转换数字
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings.astype(float))  # [ 1.25 -9.6  42.  ]

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(int_array.astype(calibers.dtype))  # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

# 4.1.3NumPy数组算术
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
# [[1. 2. 3.]
#  [4. 5. 6.]]
print(arr * arr)
# [[ 1.  4.  9.]
#  [16. 25. 36.]]
print(arr - arr)
# [[0. 0. 0.]
#  [0. 0. 0.]]
print(1 / arr)
# [[1.         0.5        0.33333333]
#  [0.25       0.2        0.16666667]]
print(arr ** 0.5)
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]

# 同尺寸数组之间的比较，会产生一个布尔值数组
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2)
# [[ 0.  4.  1.]
#  [ 7.  2. 12.]]
print(arr2 > arr)
# [[False  True False]
#  [ True False  True]]

# 4.1.4基础索引与切片
arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]
print(arr[5])  # 5
print(arr[5:8])  # [5 6 7]
arr[5:8] = 12
print(arr)  # [ 0  1  2  3  4 12 12 12  8  9]

arr_slice = arr[5:8]
print(arr_slice)  # [12 12 12]
arr_slice[1] = 12345
print(arr)  # [    0     1     2     3     4    12 12345    12     8     9]
arr_slice[:] = 64
print(arr)  # [ 0  1  2  3  4 64 64 64  8  9]
# 多维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])  # [7 8 9]
print(arr2d[0][2])  # 3
print(arr2d[0, 2])  # 3
# 在一个Numpy数组中对元素进行索引
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print(arr3d[0])  # arr3d[0]是一个2*3的数组
# [[1 2 3]
#  [4 5 6]]
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
# [[[42 42 42]
#   [42 42 42]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
arr3d[0] = old_values
print(arr3d)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
print(arr3d[1, 0])  # 返回一个一维数组
# [7 8 9]

# 4.1.4.1数组的切片索引
print(arr)
# [ 0  1  2  3  4 64 64 64  8  9]
print(arr[1:6])
# [ 1  2  3  4 64]
print(arr2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(arr2d[:2])
# [[1 2 3]
#  [4 5 6]]

# 多组切片
print(arr2d[:2, 1:])
# [[2 3]
#  [5 6]]
print(arr2d[1, :2])  # 第二行，前两列
# [4 5]
print(arr2d[:2, 2])  # 第三列，前两行
# [3 6]
print(arr2d[:, :1])
# [[1]
#  [4]
#  [7]]
arr2d[:2, 1:] = 0
print(arr2d)
# [[1 0 0]
#  [4 0 0]
#  [7 8 9]]

# 4.1.5布尔索引
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names)
# ['Bob' 'Joe' 'Will' 'Bob' 'Will' 'Joe' 'Joe']
print(data)
# [[-0.40747864  0.39408813 -0.45218688  0.28172206]
#  [-1.86624507 -0.8419252  -0.29366731 -0.24126181]
#  [ 0.24022511 -1.49292435 -2.20562637 -0.13953862]
#  [-0.16563306 -1.59582048  0.0885316   2.8249799 ]
#  [-2.06745237  0.35774876  1.72433164 -1.45083907]
#  [ 1.10616785 -0.93390631  0.76389481 -0.1348312 ]
#  [-0.34356328  1.14655979  0.64879493  0.37738432]]
print(names == 'Bob')
# [ True False False  True False False False]
print(data[names == 'Bob'])
# [[-0.20781559  0.28492074 -1.72538502  1.30235031]
#  [ 0.67652837 -0.27759504  0.63219054  0.54830165]]
print(data[names == 'Bob', 2:])
# [[-0.52413422 -0.61987835]
#  [-0.26109115  0.09870209]]
print(data[names == 'Bob', 3])
# [-0.61987835  0.09870209]
print(names != 'Bob')
# [False  True  True False  True  True  True]
#  ~对一个通用条件取反时使用
print(data[~(names != 'Bob')])
# [[-0.7000713  -0.81633558  1.61770601  1.35069605]
#  [ 0.84277136 -0.65322272 -0.00379195 -0.85041336]]
# 布尔算数运算符 -->  &(and) 和  |(or)
mask = (names != 'Bob') | (names != 'Will')
print(mask)
# [ True  True  True  True  True  True  True]
# 将data中所有的负值设置为 0
data[data < 0] = 0
print(data)
# [[0.         0.         0.         0.31698524]
#  [0.8015005  0.49262482 0.5793793  0.        ]
#  [0.         0.         0.         2.066584  ]
#  [1.13044278 2.38963348 0.08129309 0.43526564]
#  [0.60774478 0.         1.52312356 0.        ]
#  [1.1683325  0.         2.16999805 0.        ]
#  [0.87375658 0.         0.         0.        ]]
data[names != 'Joe'] = 7
print(data)
# [[7.         7.         7.         7.        ]
#  [0.         0.57206219 0.         0.129576  ]
#  [7.         7.         7.         7.        ]
#  [7.         7.         7.         7.        ]
#  [7.         7.         7.         7.        ]
#  [0.37522152 0.04305452 1.79011825 0.        ]
#  [1.31529562 0.         0.         0.10829697]]

# 4.1.6神奇索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
# [[0. 0. 0. 0.]
#  [1. 1. 1. 1.]
#  [2. 2. 2. 2.]
#  [3. 3. 3. 3.]
#  [4. 4. 4. 4.]
#  [5. 5. 5. 5.]
#  [6. 6. 6. 6.]
#  [7. 7. 7. 7.]]
# 选出符合特定顺序的子集
print(arr[[4, 3, 0, 6]])
# [[4. 4. 4. 4.]
#  [3. 3. 3. 3.]
#  [0. 0. 0. 0.]
#  [6. 6. 6. 6.]]
print(arr[[-3, -5, -7]])
# [[5. 5. 5. 5.]
#  [3. 3. 3. 3.]
#  [1. 1. 1. 1.]]

arr = np.arange(32).reshape((8, 4))
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  [24 25 26 27]
#  [28 29 30 31]]
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
# [ 4 23 29 10]
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
# [[ 4  7  5  6]
#  [20 23 21 22]
#  [28 31 29 30]
#  [ 8 11  9 10]]
# 4.1.7数组转置和换轴
arr = np.arange(15).reshape((3,5))
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
print(arr.T)
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]
