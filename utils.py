#!/bin/python3
import numpy as np
def read_orbitals(filename, norbs):
    ''' reads any file containing a square matrix into an numpy squaree array'''
    with open(filename) as f:
        lines = f.readlines()
    coefficients = []
    for line in lines:
        entries = line.split()
        for entry in entries:
            coefficients.append(float(entry))
    orbitals = np.reshape(coefficients, (norbs, norbs))
    return orbitals


def read_header(filename):
    header = []
    with open(filename,'r') as f:
        for line in f:
            if 'ORBITALS' in line:
                return header 
            header.append(line)



def write_matrop(fname, mat1, mat2, new_dim, nelec,header):
    '''  takes matrix, extracts upper traingale, writes it in columns of 3 into file'''
    # write header
    with open(fname, 'w') as fin:
        for line in header:
            fin.write(line.replace('RHF','FCI'))

    n = nelec[0]+nelec[1]
    excess = nelec[0]-nelec[1]
    microheaders = [' DENSITY      CHARGE           1    1    1    '+str(n)+'    '+str(excess)+'\n', ' DENSITY      SPIN             2    1    1    '+str(n)+'    '+str(excess)+'\n']
    for j,mat in enumerate([mat1, mat2]):
        vector = mat[0,0]
        for i in range(1,new_dim):
            vector = np.append(vector, mat[:i+1,i])
        with open(fname, 'a') as fin:
            fin.write(microheaders[j])
            if (len(vector)%3==0):
                for i in range(0,len(vector),3):
                    fin.write("%0.15E, %0.15E, %0.15E,\n"%(vector[i], vector[i+1], vector[i+2]))
            if (len(vector)%3==1):
                for i in range(0,len(vector)-3,3):
                    fin.write("%0.15E, %0.15E, %0.15E,\n"%(vector[i], vector[i+1], vector[i+2]))
                fin.write("%0.15E,\n"%vector[-1])
            if (len(vector)%3==2):
                for i in range(0,len(vector)-3,3):
                    fin.write("%0.15E, %0.15E, %0.15E,\n"%(vector[i], vector[i+1], vector[i+2]))
                fin.write("%0.15E, %0.15E,\n"%vector[-2], vector[-1])
    with open(fname, 'a') as fin:
        fin.write(" ---")

def read_orbitals_from_record(filename, norbs):
    ''' Reads Molpro record file and parses Orbitals intpó matrix'''
    with open(filename) as f:
        lines = f.readlines()
    words = []
    for line in lines:
        line.replace('D+','E+')
        for word in line.replace(',','').replace('D+','E+').replace('D-','E-').split():
            words.append(word)
    start = words.index("ORBITALS")+7
    end = words.index('EIG')
    orbitals = np.reshape(np.array(words[start:end]), (norbs, norbs)).astype(float).transpose()
    return orbitals
