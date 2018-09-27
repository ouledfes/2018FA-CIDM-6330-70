from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):
	#def test_bad_maths(self):
		#self.assertEqual( 1 + 1 , 3)
		
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')