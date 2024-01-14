


"""
    This will define all the endpoints for the api
"""

class MP3File:
    """
    This will define a mp3 file to transfer over the internet
    """
    def __init__(self, file_name: str, file_path: str, file_size: int):
        """
        This will be the init for the mp3 file
        :param file_name: the name of the file
        :param file_path: the path of the file
        :param file_size: the size of the file
        """
        self.file_name = file_name
        self.file_path = file_path
        self.file_size = file_size


def Iris(wh):
    """
    This will be the main function for the api
    :return: Return an mp3 file of the response
    """