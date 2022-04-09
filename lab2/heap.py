#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:36:07 2021

@author: agnieszkawojtowicz
"""
from math import floor 
class MinHeap:
    def __init__(self):
        self.elems = []
        
    def swap(self, idx1, idx2):
        self.elems[idx1], self.elems[idx2] = self.elems[idx2],self.elems[idx1]
        
    def size(self):
        return len(self.elems)
        
    def push(self, value):
        self.elems.append(value)
            # print('doing up')
        self.up_heap()
    
            
    def has_parent(self, idx):
        return idx>0
    
    def print_elems(self):
        print('ALL ELEMENTS LIST')
        all_list = [str(i) for i in self.elems]
        print(' '.join(all_list))
        
    def pop(self):
        self.elems[0] = self.elems[-1]
        self.elems.pop()
        self.down_heap()
        
    def parent(self, idx):
        if idx <= 0:
            return 0
        return (idx-1)//3
    
    def get_min_child_idx(self, idx):
        
        if 3*idx+1 <= self.size()-1: 
            smallest = 3*idx+1
            for i in [2,3]:
                if 3*idx+i <= self.size() - 1:
                    if self.elems[smallest] > self.elems[3*idx+i]:
                        smallest = 3*idx+i           
            return smallest
        return None
        

    
    def up_heap(self):
        idx = self.size() - 1
        while self.has_parent(idx): #dopoki ma rodzicow 
            if self.elems[idx] < self.elems[self.parent(idx)]: #jesli rodzic jest mneijsze
                self.swap(idx, self.parent(idx))  #to zmien z rodzicem 
            idx-=1
          
                 
    def down_heap(self):
        idx = 0
        while idx*3+1 <= self.size()-1: #dopóki idx ma dzieci
            smi = self.get_min_child_idx(idx) #najmniejsze dziecko 
            if self.elems[idx] < self.elems[smi]:#jesli juz bedzie wieksze to koniec
                break 
            self.swap(idx, smi)
            idx = smi

    
            
    def display(self):
        starti = 0
        level = 0
        nelems = 0
        lines = []
        while starti <len(self.elems):
            nelems = 3**level
            level_list = [str(i) for i in self.elems[starti:starti+nelems]]
            lines.append(level_list)
            level+=1
            starti+=nelems
        level = level -1
    
        nr = level
        for li in range(len(lines)):
            k = '|'
            N = 3
            lines[li] = list(' '.join(i + k * (N % 3 == 2)for N, i in enumerate(lines[li])))
        str_line = [''.join(li) for li in lines]
        lens = [len(line) for line in str_line]
        max_len = lens[-1]/2
        added = [' '*int(max_len - lens[i]/2)+str_line[i] for i in range(len(str_line))]
        for line in added:
            print(line)
           