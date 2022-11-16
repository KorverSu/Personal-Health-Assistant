import os
import tempfile


class Picture:

    def __init__(self):
        self.__picture_directory = '/usr/local/forTest/photo'
        self.__picture_file_path = None
        self.__file_name = None

    def read_picture_from_bot(self, message_content):
        with tempfile.NamedTemporaryFile(dir='/usr/local/forTest/photo', prefix='bmp', delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            temp_file_path = tf.name
        self.__picture_file_path = temp_file_path + '.' + 'bmp'
        self.__file_name = os.path.basename(self.__picture_file_path)
        os.rename(temp_file_path, self.__picture_file_path)
