from Help_Fn.functions import *


files = Files()

path = files.get_tree('f:\Work area\Buty NN\Buty_frames', ['jpg', 'bat'])

for i in path:
    print(files.get_dict_file(i))