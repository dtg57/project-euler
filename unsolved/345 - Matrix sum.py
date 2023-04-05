matrix1 =[[7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583], 
        [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913], 
        [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743], 
        [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350], 
        [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350], 
        [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803], 
        [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326], 
        [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973], 
        [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848], 
        [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198], 
        [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390], 
        [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574], 
        [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699], 
        [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107], 
        [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]]

mx = 0
for a in matrix1:
    for b in a:
        if b > mx:
            mx = b

matrix = []
for row in matrix1:
    matrix.append([])
    for n in row:
        matrix[-1].append(mx - n)

def rowtocolumn(matrix):
    end = []
    for a in range(len(matrix)):
        end.append([])
        for b in range(len(matrix)):
            end[-1].append(matrix[b][a])
    return end

def reducecolumns(matrix):
    columns = rowtocolumn(matrix)
    end = []
    for i in columns:
        end.append([])
        m = min(i)
        for n in i:
            end[-1].append(n - m)
    return rowtocolumn(end)
            
def reduce(matrix):
    endmatrix = []
    for row in matrix:
        m = min(row)
        endmatrix.append([])
        for n in row:
            endmatrix[-1].append(n - m)
    return reducecolumns(endmatrix)

def mostzeros(matrix):
    mx = (0, 0)
    pos = 0
    for row in matrix:
        c = row.count(0)
        if c > mx[1]:
            mx = (True, pos)
        pos += 1
    pos = 0
    for column in rowtocolumn(matrix):
        c = column.count(0)
        if c > mx[1]:
            mx = (False, pos)
        pos += 1
    return mx

def checkzero(matrix):
    for row in matrix:
        if 0 in row:
            return True
    return False

def getlines(matrix):
    check = []
    for row in matrix:
        check.append([])
        for cell in row:
            check[-1].append(int(bool(cell)))
    lines = 0
    while checkzero(check):
        line = mostzeros(check)
        lines += 1
        if line[0]:
            pos = 0
            for cell in check[line[1]]:
                check[line[1]][pos] = int(check[line[1]][pos] == 2) + 2
                pos += 1
        else:
            pos = 0
            for row in check:
                check[pos][line[1]] = int(check[pos][line[1]] == 2) + 2
                pos += 1
    return lines, check

def minuncovered(check, matrix):
    mn = 10 ** 4
    rowpos = 0
    pos = 0
    for row in check:
        for cell in row:
            element = matrix[rowpos][pos]
            if cell < 2 and element < mn:
                mn = element
            pos += 1
        pos = 0
        rowpos += 1
    return mn

def step6(check, matrix):
    mn = minuncovered(check, matrix)
    rowpos = 0
    pos = 0
    for row in check:
        for cell in row:
            matrix[rowpos][pos] += (cell - 1) * mn
            pos += 1
        pos = 0
        rowpos += 1
    return matrix

def minimum(matrix):
    mn = 10 ** 4
    for row in matrix:
        for cell in row:
            if cell < mn:
                mn = cell
    return mn

def step7(matrix):
    mn = minimum(matrix)
    rowpos = 0
    pos = 0
    for row in matrix:
        for cell in row:
            matrix[rowpos][pos] -= mn
            pos += 1
        pos = 0
        rowpos += 1
    return matrix

def totallines(matrix):
    matrix = reduced(matrix)
    lines = 0
    times = 1
    lines, check = getlines(matrix)
    print(matrix)
    while lines != len(matrix):
        lines, check = getlines(matrix)
        matrix = step6(check, matrix)
        print(matrix, check)
        matrix = step7(matrix)
        print(matrix, times)
        times += 1
        lines, check = getlines(matrix)
    return matrix, times
        
        
        
    
m = [[10, 19, 8, 15, 19],
     [10, 18, 7, 17, 19],
     [13, 16, 9, 14, 19],
     [12, 19, 8, 18, 19],
     [14, 17, 10, 19, 19]]


print(totallines(m))
#print(getlines([[0, 4, 0, 2, 2], [1, 4, 0, 5, 3], [2, 0, 0, 0, 1], [2, 4, 0, 5, 2], [2, 0, 0, 4, 0]]))
