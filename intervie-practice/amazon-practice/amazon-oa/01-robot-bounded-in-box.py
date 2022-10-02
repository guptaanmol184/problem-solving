# https://cybergeeksquad.co/2021/06/robot-bounded-in-circle-solution-amazon-oa.html

def isRobotBounded(instructions: str) -> bool:

    offset_dict_l = {}
    offset_dict_l[(0,  1)] = (-1, 0)
    offset_dict_l[(-1, 0)] = (0, -1)
    offset_dict_l[(0, -1)] = (1,  0)
    offset_dict_l[(1,  0)] = (0,  1)

    offset_dict_r = {}
    offset_dict_r[(0,  1)] = (1,  0)
    offset_dict_r[(1,  0)] = (0, -1)
    offset_dict_r[(0, -1)] = (-1, 0)
    offset_dict_r[(-1, 0)] = (0,  1)

    cx, cy = 0, 0
    
    c_dir = (0, 1)

    for inst in instructions:
        if inst == 'G':
            cx += c_dir[0]
            cy += c_dir[1]
        elif inst == 'L':
            c_dir = offset_dict_l[c_dir]
        else:
            c_dir = offset_dict_r[c_dir]
    
    if cx == 0 and cy == 0:
        return True
    elif c_dir != (0, 1):
        return True
    else:
        return False
