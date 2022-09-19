import pandas as pd
import datetime

class Algorithm():

  def __init__(self, df):
    self.df = df
    self.df['OFFENCE_MONTH']= pd.to_datetime(df['OFFENCE_MONTH'])


  def allOffence(self, startDate, endDate, isMobile):
    return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == isMobile)]


  def distribution(self, startDate, endDate, isMobile):
    distDict = {}

    offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == isMobile)]

    for index, row in offenceSet.iterrows():
      if row["OFFENCE_CODE"] not in distDict:
        distDict[row["OFFENCE_CODE"]] = 0
      distDict[row["OFFENCE_CODE"]] += 1

    return distDict


  def involveRadCam(self, startDate, endDate, isMobile):
    # print((self.df[self.df["CAMERA_IND"] == "Y"]))
    return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == isMobile) & (self.df["CAMERA_IND"] == "Y")]


  def singleOffenceTrend(self, startDate, endDate, offenceCode, isMobile):
    reportData = {}


    if offenceCode:
      offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == isMobile) & (self.df["OFFENCE_CODE"] == offenceCode)]
    else:
      offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == isMobile)]


    for index, row in offenceSet.iterrows():
      if row["OFFENCE_MONTH"] not in reportData:
        reportData[row["OFFENCE_MONTH"]] = 0
      reportData[row["OFFENCE_MONTH"]] += 1

    return reportData