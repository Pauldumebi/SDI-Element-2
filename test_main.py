from main import tkinter_app
from utils import monthList, widgets, filterParams, validateForm
from modules.stopSearch.index import stopAndSearchForm
from modules.covid.index import dailyAndCumulativeCasesForm, topFiveRegionWithHighestCasesForm, compareTwoRegionsForm, viewByMonthsForm
from modules.covid.covidFunc import plotDailyCases, plotTopFiveRegionWithHighestCases, plotTwoRegions, plotByMonths
from modules.stopSearch import requests as req
from modules.stopSearch.stopSearchFunc import validateDate, ageRange, searchPurpose, ethnicity, outcome, gender
import numpy as np
import pandas as pd
import unittest
import pytest
import warnings
import requests

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
    
    # tests if a label from tkinter is returned
    def testTkLabel(self):
        label = widgets.tkLabel(self.main, "Test Label", 0, 0).winfo_class()
        expected = "Label"
        self.assertEqual(label, expected)
    
    def testOptionMenu(self):
        dropDownMenu = widgets.optionMenu(self.main, 10, ["One", "Two"], 0, 0).winfo_class()
        expected = "Menubutton"
        self.assertEqual(dropDownMenu, expected)
        
    # tests that a dictionary is returned with a length of 12 items
    def testMonthDictionary(self):
        isMonthDict = monthList.monthsDict()
        self.assertIsInstance(isMonthDict, dict)
        
        message = "You cannot have more than 12 months in a calendar year as at the time of this code"
        isMonthDict = len(monthList.monthsDict())
        expected = 12
        self.assertLessEqual(isMonthDict, expected, message)
        
    # tests if region is a list of items
    def testRegionList(self):
        regions = filterParams.regionList()
        self.assertIsInstance(regions, list)
        
    # tests year is a list
    def testYearList(self):
        year = filterParams.monthList()
        self.assertIsInstance(year, list)
        
    # tests if day is a list of all days
    def testDayList(self):
        days = filterParams.dayList()
        self.assertIsInstance(days, list)
    
    # tests if this function returns a tuple
    def testValidateForm(self):
        date = validateForm.validateForm("1", "2", "January", "April", "2020", "2020", "Hartlepool", "Middlesbrough")
        self.assertIsInstance(date, tuple)
        
        message = "You cannot have more than 2 dates, start and end"
        dateLength = len(date)
        expected = 2
        
        self.assertEqual(dateLength, expected, message)
        

class stopAndSearchModulesIndex(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def testStopAndSearchForm(self): 
        # tests if all widgets for stopAndSearchForm function renders

        Frame = self.main.winfo_children()[-1]
        stopAndSearchForm(Frame)
        noOfFormElements = len(Frame.winfo_children())
        expected = 11
        self.assertEqual(noOfFormElements, expected)
        
class stopAndSearchRequestModules(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    # tests if stop & search police force list request returns a dictionary
    def testPoliceForceDictionary(self):
        policeDict = req.fetchPoliceForce()
        self.assertIsInstance(policeDict, dict)
        
    # tests if stop & search api returns a status code of 200
    def testFetchCasesRequestStatusCodeEquals200(self):
        response = requests.get("https://data.police.uk/api/stops-force?force=cleveland&date=2021-06")
        self.assertEqual(response.status_code, 200)
    
    # tests if stop & search api content-type returns application/json
    def testFetchCasesRequestContentType(self):
        response = requests.get("https://data.police.uk/api/stops-force?force=cleveland&date=2021-06")
        self.assertEqual(response.headers["Content-Type"] , "application/json")
     
    # tests this returns a tuple 
    def testFetchCasesRequest(self):
        cases = req.fetchCasesRequest("Avon and Somerset Constabulary", "2021-06")
        self.assertIsInstance(cases, tuple)
        
        
class covidFuncModules(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    # test that the plotByMonths function returns a pd series, object and string
    def testPlotByMonths(self):
        data, groupLabel, title = plotByMonths("January", "2021")
        dataType = isinstance(data, pd.Series)
        groupLabelType = isinstance(groupLabel, object)
        titleType = isinstance(title, str)
        
        expected = True
        self.assertEqual([dataType, groupLabelType, titleType], [expected, expected, expected])

    def testPlotDailyCases(self):
        # test that the plotDailyCases function returns a pd DataFrame, and string a string
        data, title = plotDailyCases("Daily infection rate", "1", "2", "January", "April", "2020", "2020", "Hartlepool")
        dataType = isinstance(data, pd.DataFrame)
        titleType = isinstance(title, str)
        expected = True
        self.assertEqual([dataType, titleType], [expected, expected])
        
    def testPlotTopFiveRegionWithHighestCases(self):
        # test that the plotTopFiveRegionWithHighestCases function returns a list, string, and a pd series
        title, size, labels = plotTopFiveRegionWithHighestCases("1", "2", "January", "March", "2020", "2020")
        titleType = isinstance(title, str)
        sizeType = isinstance(size, list)
        labelsType = isinstance(labels, pd.Series)
        expected = True
        self.assertEqual([titleType, sizeType, labelsType], [expected, expected, expected])
        
    def testPlotTwoRegions(self):
        # test that the plotTwoRegions function returns a pd DataFrame, and string
        data, title = plotTwoRegions("1", "2", "March", "April", "2020", "2020", "Hartlepool", "Middlesbrough")
        dataType = isinstance(data, pd.DataFrame)
        titleType = isinstance(title, str)
        expected = True
        self.assertEqual([dataType, titleType], [expected, expected])
        
class covidModulesIndex(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def formLength(self, function, expected):
        frame = self.main.winfo_children()[-1]
        function(frame)
        noOfFormElements = len(frame.winfo_children())
        self.assertEqual(noOfFormElements, expected)
        
    # tests if all widgets for viewByMonth function renders
    def testViewByMonthsForm(self): 
        self.formLength(viewByMonthsForm, 5)
        
    # tests if all widgets for compareTwoRegionsForm function renders
    def testCompareTwoRegionsForm(self): 
        self.formLength(compareTwoRegionsForm, 17)
        
    # tests if all widgets for dailyAndCumulativeCasesForm function renders
    def testDailyAndCumulativeCasesForm(self): 
        self.formLength(dailyAndCumulativeCasesForm, 16)
        
    def testTopFiveRegionWithHighestCasesForm(self): 
        # tests if all widgets for topFiveRegionWithHighestCasesForm function renders
        self.formLength(topFiveRegionWithHighestCasesForm, 13)
  
class stopAndSearchFuncModules(unittest.TestCase):

    @pytest.mark.asyncio
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = tkinter_app()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
        
    def testValidateDate(self):
        date = validateDate("2021", "March")
        dateType = isinstance(date, str)
        expected = True
        self.assertEqual(dateType, expected)

    def testAgeRange(self):
        data, title = ageRange("January", "2021", "Avon and Somerset Constabulary")
        dataType = isinstance(data, pd.DataFrame)
        titleType = isinstance(title, str)
        expected = True
        self.assertEqual([dataType, titleType], [expected, expected])
        
    def testSearchPurpose(self):
        data, max, ylabel, title = searchPurpose("January", "2021", "Avon and Somerset Constabulary")
        
        dataType = isinstance(data, pd.DataFrame)
        maxType = isinstance(max, np.int64)
        ylabelType = isinstance(ylabel, str)
        titleType = isinstance(title, str)
        expected = True
        self.assertEqual([dataType, maxType, ylabelType, titleType], [expected, expected, expected, expected])
        
    def testEthnicity(self):
        data, max, ylabel, title = ethnicity("January", "2021", "Avon and Somerset Constabulary")
        dataType = isinstance(data, pd.DataFrame)
        maxType = isinstance(max, np.int64)
        ylabelType = isinstance(ylabel, str)
        titleType = isinstance(title, str)
        expected = True
        self.assertEqual([dataType, maxType, ylabelType, titleType], [expected, expected, expected, expected])
        
    def testOutcome(self):
        data, title = outcome("January", "2021", "Avon and Somerset Constabulary")
        dataType = isinstance(data, pd.DataFrame)
        titleType = isinstance(title, str)
        expected = True
        self.assertEqual([dataType, titleType], [expected, expected])
        
    def testGender(self):
        data, title, explode = gender("January", "2021", "Avon and Somerset Constabulary")
        dataType = isinstance(data, pd.DataFrame)
        titleType = isinstance(title, str)
        explodeType = isinstance(explode, tuple)
        expected = True
        self.assertEqual([dataType, titleType, explodeType], [expected, expected, expected])

if __name__ == "__main__":
    unittest.main(verbosity=2)