import sys
import os
sys.path.append(os.path.abspath("../conf"))
from confbd import Connect

def verify_news(title):
    """
    This function is responsable for verify if the news already exist

    Args:
        title (str)  : Title the news
    Returns:
       bool: The return value. True for success, False otherwise.
    """
    connectbd = Connect("local", "noticias")

    data = connectbd.collection.find({"noticias.title": "title"}).count()

    if data == 0:
        return True
    else:
        return False

def error_exist(error):
    """
    Return error 

    Args:
        error (str)  : Text of error
    Returns:
       str: Return error
    """
    print error
    return