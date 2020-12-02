import unittest
from TreeSetDS import TreeSet 

class TestTreeSet(unittest.TestCase):

	def setUp(self):
		self.ts = TreeSet()


	def tearDown(self):
		del self.ts


	def test_add(self):
		self.ts.add(10)
		self.ts.add(199)
		self.ts.add(-133)

		self.assertEqual(self.ts.d[10], 1)
		self.assertEqual(self.ts.d[199], 1)
		self.assertEqual(self.ts.d[-133], 1)
		self.assertEqual(self.ts.d[999], 0)
		self.assertEqual(self.ts.d[100], 0)


	def test_clear(self):
		self.ts.clear()
		self.assertEqual(len(self.ts), 0)

	def test_copy(self):
		temp=list(self.ts.copy())
		self.assertTrue(temp==self.ts.l)

		self.ts.add(19999)
		temp1=list(self.ts.copy())
		self.assertTrue(temp1==self.ts.l)

	def test_isSubset(self):
		self.assertFalse(self.ts.isSubset({10, 20}))
		self.ts.add(10)
		self.ts.add(20)
		self.ts.add(30)
		self.assertTrue(self.ts.isSubset({10, 20, 30}))

	def test_len(self):
		self.assertEqual(len(self.ts), 0)
		self.ts.add(100)
		self.ts.add(200)
		self.ts.add(322)
		self.assertEqual(len(self.ts), 3)
		self.ts.pop(100)
		self.assertEqual(len(self.ts), 2)

	def test_pop(self):
		self.assertEqual(self.ts.pop(100),-1)
		self.ts.add(1333)
		self.ts.add(888)
		self.ts.add(5464)

		self.assertEqual(self.ts.pop(888),888)
		self.assertEqual(self.ts.pop(4999),-1)

		self.assertEqual(self.ts.pop(5464),5464)


	def test_remove(self):
		self.assertEqual(self.ts.remove(100), None)

		self.ts.add(1999)
		self.ts.add(2000)
		self.ts.add(3333)

		self.ts.remove(3333)
		self.assertEqual(self.ts.d[3333], 0)
		self.ts.remove(1999)
		self.assertEqual(self.ts.d[1999], 0)
		self.assertEqual(self.ts.remove(4444), None)

	def test___repr__(self):
		self.assertEqual(self.ts.__repr__(),'{}')
		self.ts.add(10)
		self.ts.add(30)
		self.assertEqual(self.ts.__repr__(),'{10, 30}')
		self.ts.pop(10)
		self.assertEqual(self.ts.__repr__(),'{30}')



if __name__=='__main__':
	unittest.main()