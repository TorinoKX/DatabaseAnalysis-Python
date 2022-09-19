import dataset as Dataset
from Algorithm import Algorithm
import datetime


dataset = Dataset.Dataset()

# algorithm = Algorithm(dataset)
result = Algorithm(dataset.getData()).allOffence(datetime.datetime(2012, 1, 1), datetime.datetime(2014, 1, 1), "Y")
# print(result)

result2 = Algorithm(dataset.getData()).distribution(datetime.datetime(2012, 1, 1), datetime.datetime(2014, 1, 1), "Y")
# print(result2)
result3 = Algorithm(dataset.getData()).involveRadCam(datetime.datetime(2012, 1, 1), datetime.datetime(2014, 1, 1), "Y")
print(result3)