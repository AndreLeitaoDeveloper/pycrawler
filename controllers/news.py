from conf.confbd import Connect

class NewsController(object):
    
    @staticmethod
    def verify_news(title):
        """
        This function is responsable for verify if the news already exist

        Args:
            title (str)  : Title the news
        Returns:
           bool: The return value. True for success, False otherwise.
        """
        connectbd = Connect("local", "noticias")

        data = connectbd.collection.find({"title": title}).count()

        if data == 0:
            return True
        else:
            return False


    @staticmethod
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

    @staticmethod
    def insert_new(noticia):
        """
        Return error 

        Args:
            noticia (array)  : Array with elements the news
        Returns:
           str: Return error
        """
        connectbd = Connect("local", "noticias")
        connectbd.collection.insert_one(noticia)