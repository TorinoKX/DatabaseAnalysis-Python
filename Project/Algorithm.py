import pandas as pd

class Algorithm():

  def __init__(self, df):
    self.df = df


  def allOffence(self, startDate, endDate, isMobile):
    return self.df[self.df["OFFENCE_MONTH"] >= startDate and self.df["OFFENCE_MONTH"] <= endDate and self.df["MOBILE_PHONE_IND"] == isMobile]


  def distribution(self, startDate, endDate, isMobile):
    distDict = {}

    offenceSet = self.df[self.df["OFFENCE_MONTH"] >= startDate and self.df["OFFENCE_MONTH"] <= endDate and self.df["MOBILE_PHONE_IND"] == isMobile]

    for offence in offenceSet:
      if offence.OFFENCE_CODE not in distDict:
        distDict[offence.OFFENCE_CODE] = 0
      distDict[offence.OFFENCE_CODE] += 1

    return distDict


  def involveRadCam(self, startDate, endDate, isMobile):
    return self.df[self.df["OFFENCE_MONTH"] >= startDate and self.df["OFFENCE_MONTH"] <= endDate and self.df["MOBILE_PHONE_IND"] == isMobile and self.df["CAMERA_IND"] == True]


  def singleOffenceTrend(self, startDate, endDate, offenceCode, isMobile):
    reportData = {}


    if offenceCode:
      offenceSet = self.df[self.df["OFFENCE_MONTH"] >= startDate and self.df["OFFENCE_MONTH"] <= endDate and self.df["MOBILE_PHONE_IND"] == isMobile and self.df["OFFENCE_CODE"] == offenceCode]
    else:
      offenceSet = self.df[self.df["OFFENCE_MONTH"] >= startDate and self.df["OFFENCE_MONTH"] <= endDate and self.df["MOBILE_PHONE_IND"] == isMobile]


    for offence in offenceSet:
      if offence.OFFENCE_MONTH not in reportData:
        reportData[offence.OFFENCE_MONTH] = 0
      reportData[offence.OFFENCE_MONTH] += 1

    return reportData