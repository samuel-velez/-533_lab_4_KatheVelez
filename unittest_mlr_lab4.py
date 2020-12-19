from lr_for_the_masses.lr_mlr import mlr as mlr
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

A3 = [[0, 0], [1, 1], [2, 2]]
A4 = [0, 1, 2]

class Testmlr(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        try:
            self.p4 = mlr.mullin(A3,A4)
            self.p5 = mlr.mullin(A3,A4)
            print('set Up')
        except:
            print("Check the appropriate syntax, for example self.p4 = mlr.mullin(A3, A4)")
        
    def test_setlin(self): # test routine
        try:
            p4 = mlr.mullin(A3,A4)
            self.assertEqual(round(p4.summary_mul1()[0],2),0.5)
            self.assertEqual(str(type(p4.summary_mul1())),str("""<class 'numpy.ndarray'>"""))
            self.assertEqual(round(p4.summary_mul1()[1],2),0.5)
            self.assertEqual(str(type(p4.summary_mul1()[1])),str("""<class 'numpy.float64'>"""))
        except:
            print("Make sure A3 and A4 are of comparable dimensions")

    def test_setlin2(self): # test routine
        try:
            p5 = mlr.mullin(A3,A4)
            p6 = p5.summary_mullin()
            self.assertEqual(round(p5.summary_mul2(),2),0)
            self.assertEqual(str(type(p5.summary_mul2())),str("""<class 'numpy.float64'>"""))
            self.assertEqual(round(p5.test_diag1(),2),100)
            self.assertEqual(str(type(p5.test_diag1())),str("""<class 'numpy.float64'>"""))
        except:
            print("Make sure A3 and A4 are of appropriate dimensions")
        
    def tearDown(self): # Setting up for the test
        print('Tear Down')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
unittest.main(argv=[''], verbosity=2, exit=False)
