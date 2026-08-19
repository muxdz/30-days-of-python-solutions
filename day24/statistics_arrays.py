import numpy as np

# Checking version and available methods
print('numpy:', np.__version__)

print(dir(np))

# Creating numpy arrays from python lists
python_list = [1,2,3,4,5]

print('Type:', type(python_list))
print(python_list)

two_dimesional_list = [[0,1,2], [3,4,5], [6,7,8]]

print('Type:', type(two_dimesional_list))
print(two_dimesional_list)

numpy_array = np.array(python_list)

print('Type:', type(numpy_array))
print(numpy_array)

numpy_array2 = np.array(python_list, dtype=float)

print('Type:', type(numpy_array2))
print(numpy_array2)

numpy_bool_array = np.array([0,1,-1,0,0], dtype=bool)

print('Type:', type(numpy_bool_array))
print(numpy_bool_array)

numpy_2d_array = np.array(two_dimesional_list)

print('Type:', type(numpy_2d_array))
print(numpy_2d_array)

print('one dimensional array:', numpy_array.tolist())
print('two dimensional array:', numpy_2d_array.tolist())

# Creating numpy arrays from tuples

python_tuple = (1,2,3,4,5)

print('Type:', type(python_tuple))
print(python_tuple)

numpy_array = np.array(python_tuple)

print('Type:', type(numpy_array))
print(numpy_array)

# Shapes of numpy arrays

print(numpy_array)
print('shape of numpy array:', numpy_array.shape)

print(numpy_2d_array)
print('shape of numpy array:', numpy_2d_array.shape)

three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10,11]])

print(three_by_four_array)
print('shape of numpy array:', three_by_four_array.shape)

# Data types of numpy array

int_array = np.array([0,1,2,3,4,5], dtype=int)

print(int_array)
print('data type of numpy array:', int_array.dtype)

float_array = np.array([0,1,2,3,4,5], dtype=float)

print(float_array)
print('data type of numpy array:', float_array.dtype)

bool_array = np.array([0,1,-1,0,0], dtype=bool)

print(bool_array)
print('data type of numpy array:', bool_array.dtype)

# Size of numpy array

print(numpy_array)
print('size of numpy array:', numpy_array.size)

print(numpy_2d_array)
print('size of numpy array:', numpy_2d_array.size)

print(three_by_four_array)
print('size of numpy array:', three_by_four_array.size)

# Mathematical operations using numpy

print('original array:', numpy_array)
ten_plus_original = numpy_array + 10
print('ten plus original array:', ten_plus_original)

print('original array:', numpy_array)
ten_minus_original = numpy_array - 10
print('ten minus original array:', ten_minus_original)

print('original array:', numpy_array)
ten_times_original = numpy_array * 10
print('ten times original array:', ten_times_original)

print('original array:', numpy_array)
ten_divided_by_original = numpy_array / 10
print('ten divided by original array:', ten_divided_by_original)

print('original array:', numpy_array)
ten_exponent_of_original = numpy_array ** 10
print('ten exponent of original array:', ten_exponent_of_original)

print('original array:', numpy_array)
ten_modulo_of_original = numpy_array % 10
print('ten modulo of original array:', ten_modulo_of_original)

print('original array:', numpy_array)
ten_floor_divided_by_original = numpy_array // 10
print('ten floor divided by original array:', ten_floor_divided_by_original)


# Getting items from numpy array

print(numpy_array)
print('first item:', numpy_array[0])
print('second item:', numpy_array[1])
print('last item:', numpy_array[-1])

print(numpy_2d_array)
print('first row:', numpy_2d_array[0])
print('second row:', numpy_2d_array[1])
print('last row:', numpy_2d_array[-1])

print(three_by_four_array)
print('first column:', three_by_four_array[:,0])
print('second column:', three_by_four_array[:,1])
print('last column:', three_by_four_array[:,-1])

# Slicing numpy arrays

print(numpy_2d_array)
print('first two rows and columns', numpy_2d_array[:2,:2])
print('reversal', numpy_2d_array[::-1,::-1])

# zeros and ones and empty

numpy_zeros = np.zeros((2,2), dtype=int, order='C')
print('zeros:', numpy_zeros)

numpy_ones = np.ones((2,2), dtype=int, order='C')
print('ones:', numpy_ones)

numpy_empty = np.empty((2,2), dtype=int, order='C')
print('empty:', numpy_empty)

# rearranging numpy arrays

first_shape = np.array([(1,2,3), (4,5,6)])
print(first_shape)

reshaped = first_shape.reshape(3,2)
print(reshaped)

flattened = first_shape.flatten()
print(flattened)

np_list1 = np.array([1,2,3])
np_list2 = np.array([4,5,6])

concatenated = np.concatenate((np_list1, np_list2))
print(concatenated)

h_stacked = np.hstack((np_list1, np_list2))
print('horizontally stacked:', h_stacked)

v_stacked = np.vstack((np_list1, np_list2))
print('vertically stacked:', v_stacked)