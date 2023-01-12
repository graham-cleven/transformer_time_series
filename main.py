#!/usr/bin/env python3


import pandas as pd
from datasets import load_dataset
from datasets import Dataset, DatasetDict
import matplotlib.pyplot as plt
from functools import partial
from brownian_motion import geometric_brownian_motion
import datetime

# dataset = load_dataset("monash_tsf", "tourism_monthly")
# print(dataset)


# Generate a list of 100 values
sample_data = geometric_brownian_motion(1, 252, 0.15, 0.2, 100)
prediction_len = 20
train_dataset = Dataset.from_dict({"target": sample_data[0 : -prediction_len * 2]})
test_dataset = Dataset.from_dict({"target": sample_data[0:-prediction_len]})
validation_dataset = Dataset.from_dict({"target": sample_data[0::]})

dataset = DatasetDict(
    {"train": train_dataset, "test": test_dataset, "validation": validation_dataset}
)

figure, axes = plt.subplots()
axes.plot(train_dataset["target"], color="blue")
axes.plot(validation_dataset["target"], color="red", alpha=0.5)
plt.show()

freq = "1D"
now = datetime.datetime.now()
start = now - datetime.timedelta(days=100)
start = pd.Period(start, freq)
print(start)
