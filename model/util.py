
def mat2dget(mat, pos, height):
    return mat[pos[0] + pos[1] * height]

def mat2dset(mat, pos, height, val):
    mat[pos[0] + pos[1] * height] = val