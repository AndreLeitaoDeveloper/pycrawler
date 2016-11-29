def get_url(url):
    """
    This function is responsable for connection to database and define database name and collection name

    Args:
        self (obj) : Object class Noticia
        Url (str)  : Url of crawler website

    Returns:
        takeaways  : Parse of the website
    
    """
    thisurl = url 
    #Feed HTML file into parser
    item = urllib.urlopen(thisurl).read()
    soup = BeautifulSoup(item, 'html.parser')
    takeaways = soup.findAll('item')
    return takeaways