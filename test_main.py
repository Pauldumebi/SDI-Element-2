from main import tkinter_app
from utils import widgets, monthsDict, requests, filterParams
from modules.stopSearch.index import ageGenderEthnicity
from modules.covid.index import dailyAndCumulativeCases, topFiveRegionWithHighestCases, compareTwoRegions, viewByMonths
from modules.covid.covidFunc import plotDailyCases, viewTopFiveRegionWithHighestCases, plotTwoRegions, plotByMonths
from charts.index import pieChart, lollipopChart, dotPlot, groupBarChart, horizontalBarChart, areaChart, TreeMap
from modules.stopSearch import stopSearchFunc
# from modules.stopSearch.stopSearchFunc import ageRange, searchPurpose, ethnicity
import numpy as np
import matplotlib.pyplot as plt

import unittest
import pytest
import warnings

class widgetsModules(unittest.TestCase):

    @pytest.mark.asyncio
    # To start the tkinter window without launching it
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
    
    def testTkLabel(self):
        #tests if a label from tkinter is returned

        label = widgets.tkLabel(self.main, "Test Label", 0, 0).winfo_class()
        expected = "Label"
        self.assertEqual(label, expected)
    
    def testOptionMenu(self):
    
        dropDownMenu = widgets.optionMenu(self.main, 10, ["One", "Two"], 0, 0).winfo_class()
        expected = "Menubutton"
        self.assertEqual(dropDownMenu, expected)
        
    def testMonthDictionary(self):
        #tests that a dictionary is returned with a length of 12 items

        isMonthDict = monthsDict.monthsDict()
        variableType = isinstance(isMonthDict, dict)
        expected = True
        self.assertEqual(variableType, expected)
        
        message = "You cannot have more than 12 months in a calendar year as at the time of this code"
        isMonthDict = len(monthsDict.monthsDict())
        expected = 12
        self.assertLessEqual(isMonthDict, expected, message)
        
    def testPoliceForceDictionary(self):
        #tests if stop & search police force list request returns a dictionary"""

        policeDict = requests.fetchPoliceForce()
        variableType = isinstance(policeDict, dict)
        expected = True
        self.assertEqual(variableType, expected)
        
    def testRegionList(self):
        #tests if region is a list of items

        regions = filterParams.regionList()
        variableType = isinstance(regions, list)
        expected = True
        self.assertEqual(variableType, expected)
        
    def testYearList(self):
        #tests year is a list

        year = filterParams.monthList()
        variableType = isinstance(year, list)
        expected = True
        self.assertEqual(variableType, expected)
        
    def testDayList(self):
        #tests if day is a list of all days

        days = filterParams.dayList()
        variableType = isinstance(days, list)
        expected = True
        self.assertEqual(variableType, expected)
    
    # Mock test for api to get cases
        

class stopAndSearchModulesIndex(unittest.TestCase):
    """Contains tests for the covid_charts.py module"""

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def testAgeGenderEthnicity(self): 
        # tests if all widgets for ageGenderEthnicity function renders

        Frame = self.main.winfo_children()[-1]
        ageGenderEthnicity(Frame)
        noOfFormElements = len(Frame.winfo_children())
        expected = 9
        self.assertEqual(noOfFormElements, expected)
        
class covidModulesIndex(unittest.TestCase):
    """Contains tests for the covid_charts.py module"""

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def formLength(self, Frame, expected):
        noOfFormElements = len(Frame.winfo_children())
        self.assertEqual(noOfFormElements, expected)
        
    def testViewByMonths(self): 
        # tests if all widgets for viewByMonth function renders
        Frame = self.main.winfo_children()[-1]
        viewByMonths(Frame)
        self.formLength(Frame, 5)
        
    def testCompareTwoRegions(self): 
        # tests if all widgets for compareTwoRegions function renders
        Frame = self.main.winfo_children()[-1]
        compareTwoRegions(Frame)
        self.formLength(Frame, 17)
        
    def testDailyAndCumulativeCases(self): 
        # tests if all widgets for dailyAndCumulativeCases function renders
        Frame = self.main.winfo_children()[-1]
        dailyAndCumulativeCases(Frame)
        self.formLength(Frame, 16)
        
    def testTopFiveRegionWithHighestCases(self): 
        # tests if all widgets for topFiveRegionWithHighestCases function renders
        Frame = self.main.winfo_children()[-1]
        topFiveRegionWithHighestCases(Frame)
        self.formLength(Frame, 13)
        
        
# class stopAndSearchModules(unittest.TestCase):
#     """Contains tests for the covid_charts.py module"""

#     @pytest.mark.asyncio
#     # To start the tkinter window without launching it
#     async def _start_app(self):
#         self.main.mainloop()

#     def setUp(self):
#         warnings.filterwarnings("ignore")
#         self.main = tkinter_app()
#         self._start_app()

#     def tearDown(self):
#         self.main.destroy()
        
#     def testAgeRange(self): 
#         newWindow = stopSearchFunc.ageRange("September", 2020, "Test Police Force")
#         expected = "data"
#         self.assertEqual(newWindow, expected)
        
        
# class chartModules(unittest.TestCase):
#     """Contains tests for the covid_charts.py module"""

#     @pytest.mark.asyncio
#     # To start the tkinter window without launching it
#     async def _start_app(self):
#         self.main.mainloop()

#     def setUp(self):
#         warnings.filterwarnings("ignore")
#         self.main = tkinter_app()
#         self._start_app()

#     def tearDown(self):
#         self.main.destroy()
        
#     def plot_square(x, y):
#         y_squared = np.square(y)
#         return plt.plot(x, y_squared)

#     def testPieChart(self):
#         x, y = [0, 1, 2], [0, 1, 2]
#         line, = self.plot_square(x, y)
#         x_plot, y_plot = line.get_xydata().T
#         np.testing.assert_array_equal(y_plot, np.square(y))
    
        # newWindow = pieChart("title", ["1", "2"], ["18-24", "Over 34"]) 
        # # covid_charts.plot_daily(
        # #     "cases", "1", "June", "2020", "1", "August", "2020", "Hartlepool"
        # # )
        # expected = "renders"
        # self.assertEqual(newWindow, expected)

        # newWindow = covid_charts.plot_daily(
        #     "infection", "1", "June", "2020", "1", "August", "2020", "Hartlepool"
        # )
        # expected = "renders"
        # self.assertEqual(newWindow, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)