from time import strftime
import pandas as pd
import datetime as dt


class Algorithm():

    def __init__(self, df):
        self.df = df
        self.df['OFFENCE_MONTH'] = pd.to_datetime(
            df['OFFENCE_MONTH'], dayfirst=True).dt.date

    # Returns a dataframe of all offences within a selected date-range, limited to offences involving mobile phone usage if selected.

    def allOffence(self, startDate, endDate, isMobile):
        if (isMobile):
            return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
        else:
            return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate)]

    # Returns a dictionary with a count of how many of each offence code is recorded within a selected date-range, limited to offences involving mobile phone usage if selected
    def distribution(self, startDate, endDate, isMobile):
        distDict = {}

        if (isMobile):
            offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
        else:
            offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                self.df["OFFENCE_MONTH"] <= endDate)]

        for index, row in offenceSet.iterrows():
            if row["OFFENCE_CODE"] not in distDict:
                distDict[row["OFFENCE_CODE"]] = 0
            distDict[row["OFFENCE_CODE"]] += 1

        # print(distDict)
        return distDict

    # Similar to allOffence but only returns offences involving radar or camera, can also be limited to offences involving mobile phone usage (Doesn't return anything if limited to mobile phone usage as there are no phone detection cameras during the reporting period of the dataset)
    def involveRadCam(self, startDate, endDate, isMobile):
        if (isMobile):
            return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["CAMERA_IND"] == "Y") & (self.df["MOBILE_PHONE_IND"] == "Y")]
        else:
            return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["CAMERA_IND"] == "Y")]

    # Returns a dictionary of the count of offences per month within a selected date range, can be limited to a selected offenceCode and/or offences involving mobile phone usage
    def singleOffenceTrend(self, startDate, endDate, isMobile, offenceCode):
        reportData = {}
        datePosition = startDate
        delta = dt.timedelta(days=1)
        while datePosition <= endDate:
            if (datePosition.day == 1):
                reportData[datePosition.strftime("%b, %y")] = 0
            datePosition += delta

        if (isMobile):
            if (offenceCode != None):
                offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (
                    self.df["OFFENCE_CODE"] == offenceCode) & (self.df["MOBILE_PHONE_IND"] == "Y")]
            else:
                offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                    self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
        else:
            if (offenceCode != None):
                offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                    self.df["OFFENCE_MONTH"] <= endDate) & (self.df["OFFENCE_CODE"] == offenceCode)]
            else:
                offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                    self.df["OFFENCE_MONTH"] <= endDate)]

        for index, row in offenceSet.iterrows():
            reportData[row["OFFENCE_MONTH"].strftime("%b, %y")] += 1

        return reportData
