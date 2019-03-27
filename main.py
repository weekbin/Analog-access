from url import url_list


class Access(object):
    """
    
    """
    def __init__(self, url_list):
        self.url_list = url_list
    
    def access(self):
        print("hello"+str(self.url_list))

if __name__ == "__main__":
    Connection = Access(url_list)
    Connection.access()