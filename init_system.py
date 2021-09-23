import numpy as np
import sys


class SysInit:
    # this class used for update initial params of app
    def __init__(self, parent = None):
        self._filetype = 'ini'

    @staticmethod
    def load_file(self, path):
        data = np.load(path)
        return data

    def update_params(self):
        pass

    @staticmethod
    def save_params(self, path, data, file_type='ini'):
        # save updated params to file
        if file_type == 'ini':
            np.savetxt(path+'\\default.ini', data, None, ',', '\n', 'init file', '',
                       '# file created automatic by software')
        else:
            np.savetxt(path, data, None, ',', '\n', 'init file', '', '#file created automatic by software')

    def info_out(self, format_to_out='console'):
        if format_to_out == 'console':
            print('filetype: {}'.format(self._filetype))
        else:
            pass
