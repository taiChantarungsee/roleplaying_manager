from django.test import TestCase
from django.test.client import Client

from .forms import CampaignForm
from .models import Campaign

class Views_Tests(TestCase):

	#Test fixtures
	def test_urls(self):
		c = Client()
		res = c.get("/character/")
		self.assertEquals(res.status_code, 200)
		self.assertIn(b"Click here to log in", res.content)

		res = c.get("/new_user/")
		self.assertEquals(res.status_code, 200)

		res = c.get("/login/")
		self.assertEquals(res.status_code, 200)

		res = c.get("/GM/")
		self.assertEquals(res.status_code, 200)

		res = c.get("/INVALID/")
		self.assertEquals(res.status_code, 404)

class Form_Tests(TestCase):

	def test_form(self):
		Form = CampaignForm()

		# Check some fields are there, as_p() renders in html
		self.assertIn("name", Form.as_p())
		self.assertIn("system", Form.as_p())

		#Let users create supplements...
		Form = CampaignForm(data= {
							   "name": "test_name",
							   "system": "DND",
							   "gm_name": "test",
							   "min_level": 2,
								})
	
		self.assertTrue(Form.is_valid())
		self.assertIn("name", Form.as_p()) 

		# Now save the data, which will clean it, and test it
		saved = Form.save()

		self.assertEqual(saved.name, "test_name")
		self.assertEqual(saved.min_level, 2)

		#Now change the data in a field to an invalid data type, and check the error message
		Form = CampaignForm(data= {
							   "name": "test_name",
							   "system": "DND",
							   "gm_name": "test",
							   "min_level": "ERROR",
								})
		# is_valid should return false if there are errors
		self.assertFalse(Form.is_valid())


class Model_Tests(TestCase):
	#A series of model tests querying and saving data

	def create_data(self):
		return Campaign.objects.create(
			name = "test_name",
			system = "dnd" 
			)

	def test_string_representation(self):
		data = self.create_data()
		self.assertEqual(data.__str__(), "test_name")

	def test_creation(self):
		data = self.create_data()
		self.assertTrue(isinstance(data, Campaign))

	def test_query(self):
		data = self.create_data()
		data.save()
		test = Campaign.objects.get(name="test_name")
		self.assertEquals(test.system, "dnd")