import unittest
from  Inset import InorderSet

class TestInset(unittest.TestCase):

  def setUp(self):
	  #print('setUp')
	  self.ino = InorderSet()


  def tearDown(self):
    #print('tearDown\n')
    del self.ino


  def test_add(self):
    self.ino.add(10)
    self.ino.add(199)
    self.ino.add(-133)

    self.assertEqual(self.ino.d[10], 1)
    self.assertEqual(self.ino.d[199],1)
    self.assertEqual(self.ino.d[-133],1)
    
    with self.assertRaises(KeyError):
      self.assertEqual(self.ino.d[999],0)
      self.assertEqual(self.ino.d[100],0)



  def test_clear(self):
    self.ino.clear()

    self.assertEqual(self.ino.len(),0)


  def test_copy(self):

    temp=self.ino.copy()

    self.assertTrue(temp==self.ino.d)


    self.ino.add(19999)
    temp1=self.ino.copy()
    self.assertTrue(temp1==self.ino.d)


    #Test case yet to be implemented for false test case


  def test_isSubset(self):

    self.assertFalse(self.ino.isSubset([10,20]))

    self.ino.add(10)
    self.ino.add(20)
    self.ino.add(30)

    self.assertTrue(self.ino.isSubset([10,20,30]))



  def test_len(self):
    self.assertEqual(self.ino.len(),0)
    self.ino.add(100)
    self.ino.add(200)
    self.ino.add(322)
    self.assertEqual(self.ino.len(),3)
    self.ino.pop(100)
    self.assertEqual(self.ino.len(),2)


  def test_pop(self):
    self.assertEqual(self.ino.pop(100),-1)
    self.ino.add(1333)
    self.ino.add(888)
    self.ino.add(5464)

    self.assertEqual(self.ino.pop(888),888)
    self.assertEqual(self.ino.pop(4999),-1)

    self.assertEqual(self.ino.pop(5464),5464)


  def test_remove(self):
    self.assertEqual(self.ino.remove(100),None)

    self.ino.add(1999)
    self.ino.add(2000)
    self.ino.add(3333)

    self.ino.remove(3333)
    self.assertEqual(self.ino.d[3333],0)
    self.ino.remove(1999)
    self.assertEqual(self.ino.d[1999],0)

    self.assertEqual(self.ino.remove(4444),None)



  def test___repr__(self):
    self.assertEqual(self.ino.__repr__(),'{}')

    self.ino.add(10)
    self.ino.add(30)
    self.assertEqual(self.ino.__repr__(),'{10,30}')

    self.ino.pop(10)
    self.assertEqual(self.ino.__repr__(),'{30}')




if __name__=='__main__':
	unittest.main()

