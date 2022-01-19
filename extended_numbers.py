# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:40:22 2022

@author: QQ
"""

import numpy as np
import numbers

class Q:
    
    def __init__(self, data):
        self.data = np.array(data)
    
    def __repr__(self):
        return "%s + %s i + %s j + %s k" %(self.data[0], self.data[1], self.data[2], self.data[3])
    
    def __eq__(self, other):
        return np.allclose(self.data, other.data)
    
    def __add__(self, other):
        return Q( self.data + other.data )
    
    def __neg__(self):
        return Q( -self.data )
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, Q):
            return Q( (self.data[0]*other.data[0] - self.data[1]*other.data[1] - self.data[2]*other.data[2] - self.data[3]*other.data[3],
                       self.data[0]*other.data[1] + self.data[1]*other.data[0] + self.data[2]*other.data[3] - self.data[3]*other.data[2],
                       self.data[0]*other.data[2] - self.data[1]*other.data[3] + self.data[2]*other.data[0] + self.data[3]*other.data[1],
                       self.data[0]*other.data[3] + self.data[1]*other.data[2] - self.data[2]*other.data[1] + self.data[3]*other.data[0]) )
        elif isinstance(other, numbers.Number):
            return Q( other*self.data )
        else:
            raise ValueError("Can only multiply quaternion by other quaternion or by scalars")
            
    def __rmul__(self, other): #right multiply
        if isinstance(other, numbers.Number):
            return Q( other*self.data )
        else:
            raise ValueError("Can only multiply quaternion by other quaternion or by scalars")
    def conj(self):
        return(Q(self.data * np.array([1, -1, -1, -1])))
            
    
class O:
    
    def __init__(self, data):
        self.data = np.array(data)
    
    def __repr__(self):
        string = str(self.data[0]) + ' e0'
        for i in range(1, len(self.data)):
            string += ' + ' + str(self.data[i]) + ' e' + str(i)
        return string
    
    def __eq__(self, other):
        return np.allclose(self.data, other.data)
    
    def __add__(self, other):
        return O( self.data + other.data )
    
    def __neg__(self):
        return O( -self.data )
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return O( other*self.data )
        else:
            raise ValueError("Can only multiply octonion by scalars")
            
    def __rmul__(self, other): #right multiply
        if isinstance(other, numbers.Number):
            return O( other*self.data )
        else:
            raise ValueError("Can only multiply octonion by scalars")
    def mul(self, other):
        if isinstance(other, O):
            self1, self2 = Q(self.data[:4]), Q(self.data[4:])
            other1, other2 = Q(other.data[:4]), Q(other.data[4:])
            
            mult1 = self1 * other1 - other2.conj() * self2
            mult2 = other2 * self1 + self2 * other1.conj()
            
            new_O_data = np.zeros(8)
            new_O_data[:4] = mult1.data 
            new_O_data[4:] = mult2.data
            return O(new_O_data)
            
        