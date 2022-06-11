from Buty.Buty_interface import *

import pickle
import DFLIMG
import cv2

import os
import sys

class Meta_data:
    def __init__(self):

        self.default_meta = {'identifier': 0,
                     'name': 0,
                     'sex': 0,
                     "scores": 0,
                     "history_comparison": set()
                     }

    def read_metadata(self, path):
        self.__path(path)
        dflimg = DFLIMG.DFLJPG.load(self.path)
        try:
            meta = dflimg.get_dict()
            meta["history_comparison"]
            print(f'metadata from {self.name} read: ', meta)
            return meta
        except:
            print(f'{self.name} have no metadata')
            return self.default_meta

    def save_metadata(self, path, meta):
        self.__path(path)
        dflimg = DFLIMG.DFLJPG.load(self.path)
        dflimg.set_dict(dict_data=meta)
        dflimg.save()
        print('Meta_data save ', self.name, meta)

    def del_metadata(self):
        dflimg = DFLIMG.DFLJPG.load(self.path)
        dflimg.set_dict(dict_data={})
        dflimg.save()

    def __path(self, path):
        self.path = path
        self.name = os.path.basename(self.path)

class Buty(Ui_MainWindow):
    def __init__(self, MainWindow):
        super(Buty, self).__init__()
        self.setupUi(MainWindow)
        #Static:
            #paths:
        self.dir_frames = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buty_frames'))
        self.dir = os.path.join(self.dir_frames, 'Leonardo_DiCaprio_all')

        self.files_list = os.listdir(self.dir)
        self.len_files_list = len(self.files_list)

            #Classes
        self.meta_data = Meta_data()

            #variables:
        self.file_1_index = 0
        self.file_2_index = 0

            #setupUi:

        #----------------------------------------------------------------------------

        self.actions()
        self.add_function()

    # функция которую надо запускать что бы обновить окно и данные
    def actions(self):
        self.paths()
        self.meta_1 = self.meta_data.read_metadata(self.path_file_1)
        self.meta_2 = self.meta_data.read_metadata(self.path_file_2)
        self.setupUi_chenges()

    # рассчитывается индекс изображения в списке файлов и формируется имя файла
    def paths(self):
        self.file_name_1 = self.files_list[self.file_1_index % self.len_files_list]
        self.path_file_1 = os.path.join(self.dir, self.file_name_1)

        self.file_name_2 = self.files_list[self.file_2_index % self.len_files_list]
        self.path_file_2 = os.path.join(self.dir, self.file_name_2)

    # переопределённые данные которые необходимо обновлять во время работы программы
    def setupUi_chenges(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.path_file_1)), QtGui.QIcon.Normal,
                       QtGui.QIcon.On)
        self.img_1.setIcon(icon)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(self.path_file_2)), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.img_2.setIcon(icon1)

    # на данный момент это функция реагирования на нажатие
    def add_function(self):
        self.img_1.clicked.connect(lambda: self.on_click(self.img_1.objectName()))
        self.img_2.clicked.connect(lambda: self.on_click(self.img_2.objectName()))

    # инструкции при нажатии
    def on_click(self, btn_name):
        self.meta_data.save_metadata(self.path_file_1, self.meta_1)
        self.meta_data.save_metadata(self.path_file_2, self.meta_2)
        if btn_name == "img_1":
            self.file_1_index += 1
        elif btn_name == "img_2":
            self.file_2_index += 1
        self.actions()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Buty(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())