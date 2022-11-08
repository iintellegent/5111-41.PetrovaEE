import numpy
import math
first_matrix = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
second_matrix = numpy.array([[10,11,12], [13,14,15], [16,17,18]])

def are_valid(first_matrix:numpy.ndarray,second_matrix:numpy.ndarray):
                return (first_matrix.shape[0]==second_matrix.shape[1]) and (first_matrix.shape[1]==second_matrix.shape[0])
def mat_mult(first_matrix,second_matrix):
        res_matrix = numpy.ndarray((first_matrix.shape[0],second_matrix.shape[1]))
        for i in range(res_matrix.shape[0]):
                for j in range(res_matrix.shape[1]):
                        for k in range(res_matrix.shape[0]):
                                 res_matrix[i,j]+=first_matrix[i,k]*second_matrix[k,j]
        return res_matrix
C = first_matrix.dot(second_matrix)
det_1 = round(numpy.linalg.det(first_matrix))
det_2 = round(numpy.linalg.det(second_matrix))
rank1 = numpy.linalg.matrix_rank(first_matrix)
rank2 = numpy.linalg.matrix_rank(second_matrix)
print(C)
print(det_1)
print(det_2)
print(rank1)
print(rank2)
