# Bot que busca un usuario y descarga una n cantidad de fotos indicada por el usuario
from selenium import webdriver
from time import sleep
#from secrets import pw
from selenium.webdriver.common.keys import Keys
from urllib import request
from os import makedirs

class InstaBot:

    # Cancelamos el inicio de sesion por que no nos lo pide
    # def __init__(self, username, pw):
    #     self.driver = webdriver.Chrome()
    #     self.username = username
    #     self.driver.get("https://instagram.com")
    #     sleep(2)
    #     # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
    #     #     .click()
    #     # sleep(2)
    #
    #     # Busca el xpath que tenga un input con name = username
    #     self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
    #         .send_keys(username)
    #     self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
    #         .send_keys(pw)
    #     self.driver.find_element_by_xpath('//button[@type="submit"]')\
    #         .click()
    #     sleep(4)
    #     self.driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]")\
    #         .click()
    #     sleep(2)

    def __init__(self,user,cant):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com/{}".format(user))
        sleep(3)
        fotos = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[*]/div[*]/a/div/div[1]/img')
        #i = 0                                      //*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[1]/img
        directorio = "Probando giladas\\instagram-bot-2\\{}".format(user)
        makedirs(directorio, exist_ok = True) # Si la carpeta ya existe no da error
        for i in range(cant):
            print(len(fotos))
            # //*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[1]/img
            link = fotos[i].get_attribute('src')
            request.urlretrieve(link, "{}/0{}.jpg".format( directorio, str(i+1)))
            sleep(1)

        self.driver.close()

my_bot = InstaBot('twitter', 10)
