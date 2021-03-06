import pytest
import student 

default_list = [72, 90, 23, 22, 81, 12, 49, 71, 68, 29, 8, 52, 25, 25, 85, 8, 54, 90, 68, 85, 45, 45, 30, 68, 2, 27, 40, 93, 88, 89, 73, 71, 84, 99, 7, 33, 15, 13, 8, 43, 39, 65, 26, 81, 19, 67, 59, 59, 66, 94, 6, 66, 37, 23, 14, 99, 60, 12, 46, 81, 28, 77, 90, 21, 96, 91, 7, 84, 99, 56, 77, 1, 39, 20, 1, 90, 94, 10, 61, 76, 79, 67, 77, 5, 97, 32, 58, 31, 85, 95, 87, 36, 69, 77, 72, 90, 74, 13, 0, 78]
pos_list = [[440, 432, 190, 634, 494, 672, 831, 302, 727, 637], [649, 33, 37, 864, 622, 441, 907, 778, 382, 940], [1, 432, 562, 700, 704, 636, 893, 225, 485, 994], [485, 773, 911, 914, 672, 838, 471, 0, 367, 690], [456, 920, 783, 23, 213, 603, 210, 684, 719, 265], [65, 522, 325, 928, 28, 217, 938, 484, 189, 149], [31, 282, 175, 971, 215, 30, 579, 279, 270, 76], [55, 984, 972, 196, 9, 507, 239, 780, 9, 126], [440, 287, 878, 611, 102, 125, 629, 902, 241, 285], [993, 76, 379, 267, 137, 425, 12, 483, 871, 532]]
pos_sol = [831, 940, 994, 914, 920, 938, 971, 984, 902, 993]
neg_list = [[-761, -527, -117, -12, -294, -619, -951, -632, -715, -883], [-620, -587, -501, -500, -310, -642, -785, -34, -923, -356], [-809, -427, -482, -702, -379, -250, -51, -412, -745, -769], [-525, -407, -769, -325, -27, -490, -86, -722, -3, -627], [-726, -624, -949, -97, -987, -514, -797, -814, -190, -860], [-905, -784, -684, -334, -713, -859, -800, -256, -445, -355], [-216, -424, -811, -982, -932, -192, -353, -394, -701, -785], [-926, -816, -8, -627, -297, -402, -125, -914, -936, -836], [-753, -9, -470, -706, -981, -968, -812, -405, -750, -113], [-186, -216, -689, -824, -899, -928, -502, -225, -626, -339]]
neg_sol = [-12, -34, -51, -3, -97, -256, -192, -8, -9, -186]

def test_default():
    assert student.maximum(default_list) == 99, "Make sure it works for the test case given"

def test_positive_solutions():
    for i in range(len(pos_list)):
        assert student.maximum(pos_list[i]) == pos_sol[i]
       
def test_negative_solutions():
    for i in range(len(neg_list)):
        assert student.maximum(neg_list[i]) == neg_sol[i]
