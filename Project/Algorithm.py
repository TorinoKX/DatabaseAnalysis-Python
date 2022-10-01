import pandas as pd
import datetime as dt


class Algorithm():

    def __init__(self, df):
        self.df = df
        try:
            self.df['OFFENCE_MONTH'] = pd.to_datetime(
                df['OFFENCE_MONTH'], dayfirst=True).dt.date
        except:
            print("No OFFENCE_CODE column")

    def allOffence(self, startDate, endDate, isMobile):
        # """
        # It returns a dataframe of all offences between the start and end date, and if isMobile is true,
        # it will only return offences where the mobile phone indicator is true

        # :param startDate: The start date of the period you want to look at
        # :param endDate: The end date of the period you want to look at
        # :param isMobile: boolean
        # :return: A dataframe
        # """
        try:
            if (isMobile):
                return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
            else:
                return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate)]
        except:
            print("Invalid Inputs")
            return pd.DataFrame([])

    def distribution(self, startDate, endDate, isMobile):
        """
        It takes in a start date, end date, and a boolean value, and returns a dictionary of offence
        codes and their respective counts

        :param startDate: The start date of the period you want to look at
        :param endDate: The end date of the period you want to look at
        :param isMobile: boolean
        :return: A dictionary of offence codes and the number of times they occur in the dataframe.
        """
        distDict = {}

        try:
            if (isMobile):
                offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                    self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
            else:
                offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (
                    self.df["OFFENCE_MONTH"] <= endDate)]
        except:
            print("Invalid Inputs")
            return {}

        for index, row in offenceSet.iterrows():
            if row["OFFENCE_CODE"] not in distDict:
                distDict[row["OFFENCE_CODE"]] = 0
            distDict[row["OFFENCE_CODE"]] += 1

        return distDict

    def involveRadCam(self, startDate, endDate, isMobile):
        """
        It returns a dataframe of all the offences involving radar/camera that occurred between the start and end date, 
        and if the isMobile parameter is true, it will only return the offences that involved a mobile phone

        :param startDate: The start date of the period you want to look at
        :param endDate: The end date of the period you want to look at
        :param isMobile: boolean
        :return: A dataframe
        """
        try:
            if (isMobile):
                return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["CAMERA_IND"] == "Y") & (self.df["MOBILE_PHONE_IND"] == "Y")]
            else:
                return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["CAMERA_IND"] == "Y")]
        except:
            print("Invalid Inputs")
            return pd.DataFrame([])

    def singleOffenceTrend(self, startDate, endDate, isMobile, offenceCode):
        """
        It takes a start date, end date, a boolean value for whether the offence is mobile or not, and
        an offence code (which can be null) and returns a dictionary of the number of offences per month

        :param startDate: The start date of the period you want to look at
        :param endDate: The end date of the period you want to look at
        :param isMobile: boolean
        :param offenceCode: The offence code to filter by
        :return: A dictionary of the number of offences per month.
        """
        reportData = {}
        datePosition = startDate
        delta = dt.timedelta(days=1)

        try:
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
        except:
            print("Invalid Inputs")
            return {}

        for index, row in offenceSet.iterrows():
            reportData[row["OFFENCE_MONTH"].strftime("%b, %y")] += 1

        return reportData
