import os
import random
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
    def __init__(self, url_list, driver, sleeping, rating):
        """
        Passing the main parameters
        """
        self.url_list = url_list
        self.driver = driver
        self.sleeping = sleeping
        self.rating = rating

    def random_rate(self):
        """
        A number between 0 and 1 indicates probability
        eg: 0.8 means 80% posibility
        """
        r = random.random()
        if r <= self.rating:
            return True
        else:
            return False
    
    def access(self):
        """
        Loop through the sites in the url access list
        """
        sleeping = self.sleeping
        driver = self.driver
        try:
            for i in self.url_list:
                if self.random_rate():
                    try:
                        driver.get(i)
                        print(i + " is connected successfully")
                        time.sleep(2)
                    except:
                        print(i + " is connected failed")
                else:
                    print(i + " is skipped")
            driver.quit()
            return True
        except:
            driver.quit()
            time.sleep(2)
            return False

if __name__ == "__main__":
    j = 0
    k = 0
    while True:
        """
        Declaration the main parameters
        """
        driver = set_driver()
        sleeping = 10
        rating = 0.5
        Connection = Access(url_list, driver, sleeping, rating)
        result = Connection.access()
        print(result)
        if result == True:
            j += 1
            print("成功访问"+"(" + str(j) + ")次")
            print("Next access will be " + str(sleeping) + " seconds later")
            time.sleep(sleeping)
        else :
            k += 1
            print("访问出错"+"(" + str(k) + ")次")
