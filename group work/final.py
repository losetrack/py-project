import random

class Matrix:

    def __init__(self, data=None, dim=None, init_value=0):

        if data == None and dim == None:
            raise Exception("DataEmpty") 

        if not data == None:
            self.data = data

            a = len(data)
            b = len(data[0])
            self.dim = (a,b)

        if data == None:

            mat = [[init_value for i in range(dim[1])] for j in range(dim[0])]
            self.data = mat

        self = self.data
        pass


    def shape(self):
        return self.dim
    

    def reshape(self, newdim):

        if newdim[0] * newdim[1] != self.dim[0] * self.dim[1]:
            raise Exception("newdimError")
        
        ele = []
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                ele.append(self.data[i][j])

        k = 0
        newdata = []
        for i_ in range(newdim[0]):

            newele = []
            for j_ in range(newdim[1]):
                newele.append(ele[k])
                k += 1
            newdata.append(newele)

        return Matrix(data=newdata).data
       
       
    
    def dot(self, other):

        if self.dim[1] != other.dim[0]:
            raise Exception("DimError")
        
        result = Matrix(dim=(self.dim[0],other.dim[1]))

        for i in range(self.dim[0]):

            for j in range(other.dim[1]):

                number = 0
                for k in range(other.dim[0]):
                    number += self.data[i][k] * other.data[k][j]
                
                result.data[i][j] = number

        return result
    
    
    def T(self):
        copy = (self.data).copy()
        newMat = Matrix(dim = (self.dim[1],self.dim[0]))

        for i in range(self.dim[1]):
            
            for j in range(self.dim[0]):
                 newMat.data[i][j] = copy[j][i]

        return newMat
    
  
    
    def sum(self, axis=None):
        if axis == 0:

            newMat = []
            for i  in range(self.dim[1]):

                num = 0
                for j  in range(self.dim[0]):
                    num += self.data[j][i]

                newMat.append(num)

            return Matrix(data=[newMat])

        if axis == 1:

            newMat = []
            for i in range(self.dim[0]):

                num = 0
                for j in range(self.dim[1]):
                    num += self.data[i][j]

                newMat.append([num])

            return Matrix(data=newMat)

        if axis == None:

            num = 0
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    num += self.data[i][j]

            return Matrix(data=[[num]])
        
        
    def copy(self):
        copy = Matrix(data=self.data)
        return copy
    
    
    
    def Kronecker_product(self, other):

        result = []
        for row1 in self.data:

            for row2 in other.data:

                temp_row = []
                for ele1 in row1:
                    temp_row.extend(ele1 * ele2 for ele2 in row2)

                result.append(temp_row)

        newMat = Matrix(data=result)
        return newMat
    
    
    
    def __getitem__(self, key):

        if isinstance(key[1],slice):
            #定义省略
            row_start = key[0].start
            row_stop = key[0].stop
            col_start = key[1].start
            col_stop = key[1].stop

            if row_start == None:
                row_start = 0
            if col_start == None:
                col_start = 0
            if row_stop == None:
                row_stop = self.dim[0]
            if col_stop == None:
                col_stop = self.dim[1]
            

            result = []
            for i in range(row_start,row_stop):

                temp_row = []
                for j in range(col_start,col_stop):
                    temp_row.append(self.data[i][j])

                result.append(temp_row)
            
            return result
        
        else:
            return self.data[key[0]][key[1]]
        
        
    
    def __setitem__(self, key, value):

        if isinstance(key[1],slice):

            row_start = key[0].start
            row_stop = key[0].stop
            col_start = key[1].start
            col_stop = key[1].stop

            if row_start == None:
                row_start = 0
            if col_start == None:
                col_start = 0
            if row_stop == None:
                row_stop = self.dim[0]
            if col_stop == None:
                col_stop = self.dim[1]

            for i in range(row_start,row_stop):
                for j in range(col_start,col_stop):
                    self.data[i][j] = value.data[i-row_start][j-col_start]

        else:
            self.data[key[0]][key[1]] = value
            
            
    
    def __pow__(self, n):
            
        result = Matrix(data=self.data)
    
        for i in range(n-1):
            result = result.dot(self)
                
        return result
    
    
    def __add__(self, other):
        
        newMat = Matrix(dim=(self.dim[0],self.dim[1]))
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                newMat.data[i][j] = self.data[i][j] + other.data[i][j]
                
        return newMat


    def __sub__(self, other):
        
        newMat = Matrix(dim=(self.dim[0],self.dim[1]))
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                newMat.data[i][j] = self.data[i][j] - other.data[i][j]
                
        return newMat
    
    
    def __mul__(self, other):
        
        newMat = Matrix(dim=self.dim)
        for i in range(self.dim[0]):
            
            for j in range(self.dim[1]):
                newMat.data[i][j] =self.data[i][j] + other.data[i][j]
                
        return newMat
    
    
    def __len__(self):
        
        length = self.dim[0] * self.dim[1]
        return length


