# -*- coding: utf-8 -*-
import sys
import os
from random import randrange
from time import sleep

from requestium import Session
from bs4 import BeautifulSoup
from requests import ConnectionError


class RugratsBot:
    def __init__(self, userLogin=str(), userPass=str()):
        self._rugratSession = Session(
            "./chromedriver", browser="chrome", default_timeout=15
        )
        self._userLogin = userLogin
        self._userPassword = userPass
        self._isLogged = False

        # default/recomended range seconds between
        self._rangeTimeBetComments = 400
        self._rangeTimeBetFollow = 400

    def setLoginInfo(self, userLogin, userPass):
        self._userLogin = userLogin
        self._userPassword = userPass

    def setInstagramPageUrl(self, instaPageUrl):
        self._instagramPageUrl = instaPageUrl

    def setListOfComments(self, listOfComments):
        self._listOfComments = listOfComments

    def setTimeBetComments(self, timeBetweenComments):
        self._rangeTimeBetComments = timeBetweenComments

    def isInternetOn(self):
        url = "http://www.google.com/"
        timeout = 5
        try:
            _ = self._rugratSession.get(url, timeout=timeout)
            return True
        except ConnectionError:
            print("No connection available")
        return False

    def login(self, saveLoginInformatin=True):
        if self._userLogin == "" or self._userPassword == "":
            return

        # Sign in on instagram **outset**
        self._rugratSession.driver.get(
            "https://www.instagram.com/accounts/login/?hl=pt-br"
        )
        sleep(5)

        self._rugratSession.driver.ensure_element_by_css_selector(
            "input[name='username']"
        ).send_keys(self._userLogin)
        self._rugratSession.driver.ensure_element_by_css_selector(
            "input[name='password']"
        ).send_keys(self._userPassword)

        sleep(5)
        self._rugratSession.driver.ensure_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]"
        ).click()
        # Sign in on instagram **end**

        if saveLoginInformatin == True:
            # Save login information on Chromium driver **outset**
            sleep(5)
            self._rugratSession.driver.ensure_element_by_xpath(
                "/html/body/div[1]/section/main/div/div/div/section/div/button"
            ).click()

            sleep(5)
            self._rugratSession.driver.ensure_element_by_xpath(
                "/html/body/div[4]/div/div/div/div[3]/button[1]"
            ).click()
            # Save login information on Chromium driver **end**

        self._isLogged = True

    def signOut(self):
        if self._isLogged:
            self._rugratSession.driver.get("https://www.instagram.com")
            self._rugratSession.driver.ensure_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img"
            ).click()
            self._rugratSession.driver.ensure_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div"
            ).click()
            sleep(5)

    def followProfilesTargetProfile(self, targetUser):
        if self._isLogged == False:
            raise Exception(
                "First, yout should be logged in. Before start to follow, run 'yourBabyRugrat.signIn()'"
            )

        self._rugratSession.driver.get("https://www.instagram.com/" + targetUser)
        self._rugratSession.driver.ensure_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a"
        ).click()

        self._rugratSession.transfer_driver_cookies_to_session

        profileResponse = self._rugratSession.get(
            "https://www.instagram.com/" + targetUser
        )
        soupResponse = BeautifulSoup(profileResponse, "lxml")
        numberOfFollowers = soupResponse.find_all(targetUser + "/followers/")
        print(numberOfFollowers)

    def startCommenting(self, instagramUrlToComment, listOfComments):
        if self._isLogged == False:
            raise Exception(
                "First, yout should be logged in. Before start commenting, run 'yourBabyRugrat.signIn()'"
            )

        # Load target instagram page **outset**
        self._rugratSession.driver.get(instagramUrlToComment)
        # Load target instagram page **end**

        # start commenting
        while True:
            maxTimeToComment = self._rangeTimeBetComments + 100
            try:
                index = randrange(0, len(listOfComments))
                sleepTime = randrange(self._rangeTimeBetComments, maxTimeToComment)
                commentArea = self._rugratSession.driver.ensure_element_by_class_name(
                    "Ypffh"
                )
                commentArea.click()
                commentArea = self._rugratSession.driver.ensure_element_by_class_name(
                    "Ypffh"
                )

                if self.isInternetOn() == False:
                    continue

                commentArea.send_keys(listOfComments[index])
                commentArea.submit()
                sleep(sleepTime)

            except KeyboardInterrupt as interrupted:
                try:
                    print(interrupted)
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
