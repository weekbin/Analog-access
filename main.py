import os
import time

import schedule
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from driver import set_driver
from url import url_list
from useragent import ua_list


class Access(object):
    """
    main function
    """
    def __init__(self, url_list, driver):
        """
        
        """
        self.url_list = url_list
        self.driver = driver
    
    def access(self):
        """
        
        """
        j = 1
        k = 1
        sleeping = 10
        driver = self.driver
        while True:
            try:
                for i in self.url_list:
                    try:
                        driver.get(i)
                        print(i + " is connected successfully")
                        time.sleep(2)
                    except:
                        pass
                print("成功访问"+"(" + str(j) + ")次")
                j += 1
                driver.quit()
                print("Next access will be " + str(sleeping) + " later")
                time.sleep(sleeping)
            except:
                print("访问出错"+"(" + str(k) + ")次")
                k += 1
                driver.quit()
                time.sleep(5)

if __name__ == "__main__":
    driver = set_driver()
    Connection = Access(url_list, driver)
    Connection.access()
