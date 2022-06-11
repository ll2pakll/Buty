from Help_Fn.functions import *


files = Files()

for i in files.get_tree('f:\Work area\Buty NN\Buty_frames', ['jpg', 'bat']):
    print(i)