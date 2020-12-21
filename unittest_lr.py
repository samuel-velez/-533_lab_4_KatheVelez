from lr_for_the_masses.lr_mlr import lr as lr
import unittest
import uncertainties.unumpy as unp
import uncertainties as unc
import scipy
import matplotlib
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sklearn as skl
from sklearn import linear_model
A = [1, 2, 3, 4, 5, 6, 7, 8 , 9 , 10]
B = [5, 6, 8, 9, 16, 29, 14, 16, 19, 25]
# P1 = simlin(A,B)
# print(round(P1.summarylin_test_slope(),2))
# print(round(P1.summarylin_test_inctercept(),2))
# print(round(P1.summarylin_test_rval(),2))
# print(round(P1.summarylin_test_pval(),2))

P2 = lr.plotlin(A,B)
print(str(type(P2.plotoriginaldata)))
x = np.linspace(10,5)
print(str(type(x)))
        
import unittest

from lr_for_the_masses.lr_mlr import lr as lr


class TestPerson(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    
    def setUp(self):
        self.p1 = lr.simlin(A,B)
        self.p2 = lr.plotlin(A,B)
        print('set Up')

    def test_set_lin(self): # test routine
        p1 = lr.simlin(A,B)
        self.assertEqual(round(p1.summarylin_test_slope(),2),2.05)
        self.assertEqual(round(p1.summarylin_test_inctercept(),2), 3.4)
        self.assertEqual(round(p1.summarylin_test_rval(),2), 0.77)
        self.assertEqual(round(p1.summarylin_test_pval(),2), 0.01)
        
    def test_plot_lin(self): # test routine
        p2 = lr.plotlin(A,B)
        self.assertEqual(str(type(p2.plotoriginaldata)),str("""<class 'method'>"""))
        self.assertEqual(str(type(p2.plotfittedline)),str("""<class 'method'>"""))
        self.assertEqual(str(type(p2.plotconfidence_intervals)),str("""<class 'method'>"""))
        self.assertNotEqual(str(type(p2.plottest)),str("""<class __'method'>"""))

        
               

    def tearDown(self): # Setting up for the test
        print('Tear Down')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
unittest.main(argv=[''], verbosity=2, exit=False)

