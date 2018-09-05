from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):

		# Manal has heard about a cool new online to-do-app.
		# She goes to check out its homepage

		self.browser.get('http://localhost:8000')

		# She notices the page title and the header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test'), "Browser title was " + browser.title

		# She is invited to enter a to-do item straight away

		# She types "Buy mineral free water" into a text box

		# When she hits <enter>, the page updates, and now the page lists
		# "1: Buy mineral water" as an item in a to-do list

		# There is still a text box inviting her to add another item.
		# She enters "Replace water in the hair removal machine."

		# The page updates again, and now shows both items on her list.

		# Manal wonders whether the site will remember her list.
		# Then she sees that the site has generated a unique URL for her

		# She visists that URL - her to -do list is still there.

		# satisfied, she goes back to sleep.
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')

