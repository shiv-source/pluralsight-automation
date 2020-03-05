from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time


# For user prompt
user_name = input("Enter your pluralsight user name :")
user_password = input("Enter your pluralsight password :")
course_name = input("Enter course name :")


# Login url of pluralsight
url = "https://app.pluralsight.com/id?"
# For opening chrome webdriver
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get(url)


class Pluralsight():
    def __init__(self,userId,password,courseName):
        self.userId = userId
        self.password = password
        self.courseName = courseName

    # For user Login
    def login(self):
        try:
            userElement = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='Username']"))
            )
            time.sleep(1)
            userElement.send_keys(self.userId)
            print("Located your user xpath")
            time.sleep(1)

            passElement = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='Password']"))
            )
            time.sleep(1)
            passElement.send_keys(self.password)
            time.sleep(1)
            print("Located your password xpath")

            btnElement = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='login']"))
            )
            time.sleep(1)
            btnElement.click()
            print("Located your click xpath")
            time.sleep(5)
        except:
            print("Oops! Error occurs, please restart all the process again.")

        finally:
            time.sleep(1)


    # For user search course name
    def search_querry(self):
        try:
            user_querry = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='prism-search-input']"))
            )
            time.sleep(1)
            user_querry.send_keys(self.courseName,Keys.ENTER)
            print("Located your user querry xpath")
            time.sleep(1)
        except:
            print("Oops! Error occurs, please restart all the process again.")

        finally:
            time.sleep(2)
            # driver.close()

    def course_library(self):
        try:
            video_querry = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='mixed-list']/li[1]/div/div[1]/div[1]/a/h3/div/span/span[1]"))
            )
            time.sleep(1)
            video_querry.click()
            print("Clicking on the video url")
        except:
            print("Oops! Error occurs, please restart all the process again.")

        finally:
            time.sleep(2)

    def start_course(self):
        try:
            start_querry = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//*[@id='ps-main']/div/div[2]/section/div[1]/div[2]/a"))
            )
            time.sleep(2)
            start_querry.click()
            print("your course is started")
        except:
            print("Oops! Error occurs, please restart all the process again.")

        finally:
            time.sleep(5)
            # driver.close()

if __name__ == "__main__":
    obj = Pluralsight(user_name,user_password,course_name)
    obj.login()
    obj.search_querry()
    obj.course_library()
    obj.start_course()

