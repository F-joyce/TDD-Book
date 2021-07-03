from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #You hear about a new website for creating and editing to do lists
        #You go to the website from your browser
        self.browser.get('http://localhost:8000')

        #At the first look, the website tilte and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

    #You are asked to insert a to-do item right away

    #She types something

    #Etc

    #Etc

if __name__ == '__main__':
    unittest.main()

