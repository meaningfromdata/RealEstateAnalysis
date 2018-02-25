from unittest import TestCase, skip
import RealEstateAnalysis
from RealEstateAnalysis.data import DataStream
class RealEstateAnalysisTest(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	@skip("fails")
	def test_something(self):
		self.assertTrue(False)

class DataStreamTest(TestCase):
	def setUp(self):
		self.stream = DataStream.DataStream("https://data.brla.gov/resource/pz73-gh9s.json")
		self.stream.load()
	
	def tearDown(self):
		pass
	
	def test_canGetData(self):
		self.assertNotEqual(len(self.stream),0)

	def test_canIterate(self):		
		L = [x for x in self.stream]
		self.assertEqual(len(L), len(self.stream))

	def test_canFilter(self):
		self.stream.where(zip = 70808)
		self.stream.load()
		for x in self.stream:
			if x['zip'] != 70808:
				self.fail
	
	def test_canSample(self):
		N = len(self.stream)
		a = self.stream.sample(9)
		self.assertEqual(len(a), 9)
		self.assertEqual(len(self.stream), N -9)