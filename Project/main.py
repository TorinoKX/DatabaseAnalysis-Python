import dataset as Dataset
from Algorithm import Algorithm
import datetime


dataset = Dataset.Dataset()

# algorithm = Algorithm(dataset)
result = Algorithm(dataset.getData()).allOffence(datetime.datetime(2012, 1, 1), datetime.datetime(2014, 1, 1), True)

#result2 = Algorithm(dataset.getData()).distribution(datetime.datetime(2012, 1, 1), datetime.datetime(2014, 1, 1), "Y")
# print(result2)
# result3 = Algorithm(dataset.getData()).involveRadCam(datetime.datetime(2012, 1, 1), datetime.datetime(2014, 1, 1), False)
# print(result3)
result4 = Algorithm(dataset.getData()).singleOffenceTrend(datetime.datetime(2012, 1, 1), datetime.datetime(2020, 1, 1), False, 82950)
print(result4)