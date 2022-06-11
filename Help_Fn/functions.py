import pickle
import DFLIMG
import cv2

import os
import sys

# Считывание, запись и удаление метаданных
class Meta_data:
    def __init__(self):

        self.default_meta = {
                     'identifier': 0,
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

    #создание пути и имени файла
    def __path(self, path):
        self.path = path
        self.name = os.path.basename(self.path)

# Составление древа файлов
class Files:
    # path - путь к папке из которой нужно получить древо
    # extention - расширение подавать в виде списка
    def get_tree(self, path, extension=None):
        filelist = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if extension:
                    for i in extension:
                        if (file.endswith('.' + i)):
                            filelist.append(os.path.join(root, file))
                else:
                    filelist.append(os.path.join(root, file))
        return filelist

    def get_deep_file(self, path, deep):
        path = path.split('\\')[-deep:]
        return os.path.join(*path)