
import unittest

from lr_for_the_masses.lr_mlr import lr as lr


A = [1, 2, 3, 4, 5, 6, 7, 8 , 9 , 10]
B = [5, 6, 8, 9, 16, 29, 14, 16, 19, 25]

class MyInputError(Exception):
    
        def __init__(self,value1):
            self.value1 = """Ensure that the format and indentation are correct, for example self.p1 = lr.simlin(A,B)"""
            print(self.value1)

        def __str__(self):
            return(repr(self.value1))

    

class MyInputError2(Exception):
        def __init__(self,value2):
            self.value2 = """The plot definitions should be accurate folks"""
            print(self.value2)
        
        def __str__(self):
            return(repr(self.value2))



class TestPerson(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        try:
            self.p1 = lr.simlin(A,B)
            self.p2 = lr.plotlin(A,B)
            print('set Up')
        except:
            print("Ensure that the format and indentation are correct, for example self.p1 = lr.simlin(A,B)")
        


    def test_set_lin(self): # test routine
        try:
            p1 = lr.simlin(A,B)
        except MyInputError as ex:
            print("Check the syntax to be p1 = lr.simlin(A,B)",ex.value1)
            
        self.p11 = p1.summarylin()
        self.assertEqual(round(p1.summarylin_test_slope(),2),2.05)
        self.assertEqual(round(p1.summarylin_test_inctercept(),2), 3.4)
        self.assertEqual(round(p1.summarylin_test_rval(),2), 0.77)
        self.assertEqual(round(p1.summarylin_test_pval(),2), 0.01)
        

    def test_plot_lin(self): # test routine
        try:
            p2 = lr.plotlin(A,B)
            self.p22 = p2.diagnoselin()
            self.p23 = p2.plotoriginaldata()
            self.p24 = p2.plotfittedline()
            self.p25 = p2.plotconfidence_intervals()
            self.p26 = p2.plottest()
            self.assertEqual(str(type(p2.plotoriginaldata)),str("""<class 'method'>"""))
            self.assertEqual(str(type(p2.plotfittedline)),str("""<class 'method'>"""))
            self.assertEqual(str(type(p2.plotconfidence_intervals)),str("""<class 'method'>"""))
            self.assertNotEqual(str(type(p2.plottest)),str("""<class __'method'>"""))
        
        except MyInputError as ex:
            print("Check the syntax for the plot module",ex2.value2)
            

    def tearDown(self): # Setting up for the test
        print('Tear Down')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
unittest.main(argv=[''], verbosity=2, exit=False)
