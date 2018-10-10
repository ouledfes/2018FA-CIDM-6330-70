from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):

	

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
		
	def test_can_start_a_list_and_retrieve_it_later(self):

		# Manal has heard about a cool new online to-do-app.
		# She goes to check out its homepage

		self.browser.get(self.live_server_url)

		# She notices the page title and the header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy Mineral Water" into a text box 
		inputbox.send_keys('Buy mineral water.')

		# When she hits <enter>, the page updates, and now the page lists
		# "1: Buy mineral water" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy mineral water.')

		#table = self.browser.find_element_by_id('id_list_table')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(
		#	any(row.text == '1: Buy mineral water' for row in rows), 
		#	f"New to-do item did not appear in table. Contents were:\n{table.text}"
		#)
		#self.assertIn('1: Buy mineral water.', [row.text for row in rows])

		# There is still a text box inviting her to add another item.
		# She enters "Replace water in the hair removal machine."
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Replace water in the hair removal machine.')
		inputbox.send_keys(Keys.ENTER)
				

		# The page updates again, and now shows both items on her list.
		self.wait_for_row_in_list_table('2: Replace water in the hair removal machine.')
		self.wait_for_row_in_list_table('1: Buy mineral water.')

		
		

		# Manal wonders whether the site will remember her list.
		# Then she sees that the site has generated a unique URL for her
		self.fail('Finish the test!')

		# She visists that URL - her to -do list is still there.

		# satisfied, she goes back to sleep.
		
#if __name__ == '__main__':
#	unittest.main(warnings='ignore')

