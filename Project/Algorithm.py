import pandas as pd

class Algorithm():

  def __init__(self, df):
    self.df = df
    self.df['OFFENCE_MONTH']= pd.to_datetime(df['OFFENCE_MONTH'])


  def allOffence(self, startDate, endDate, isMobile):
    if(isMobile):
      return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
    else:
      return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate)]


  def distribution(self, startDate, endDate, isMobile):
    distDict = {}

    if(isMobile):
      offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
    else:
      offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate)]

    for index, row in offenceSet.iterrows():
      if row["OFFENCE_CODE"] not in distDict:
        distDict[row["OFFENCE_CODE"]] = 0
      distDict[row["OFFENCE_CODE"]] += 1

    return distDict


  def involveRadCam(self, startDate, endDate, isMobile): 
    if(isMobile):
      return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["CAMERA_IND"] == "Y") & (self.df["MOBILE_PHONE_IND"] == "Y")]
    else:
      return self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["CAMERA_IND"] == "Y")]


  def singleOffenceTrend(self, startDate, endDate, isMobile, offenceCode = 0):
    reportData = {}

    if(isMobile):
      if offenceCode:
        offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["OFFENCE_CODE"] == offenceCode) & (self.df["MOBILE_PHONE_IND"] == "Y")]
      else:
        offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["MOBILE_PHONE_IND"] == "Y")]
    else:
      if offenceCode:
        offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate) & (self.df["OFFENCE_CODE"] == offenceCode)]
      else:
        offenceSet = self.df.loc[(self.df["OFFENCE_MONTH"] >= startDate) & (self.df["OFFENCE_MONTH"] <= endDate)]

    for index, row in offenceSet.iterrows():
      if row["OFFENCE_MONTH"] not in reportData:
        reportData[row["OFFENCE_MONTH"]] = 0
      reportData[row["OFFENCE_MONTH"]] += 1

    return reportData