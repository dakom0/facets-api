import vaex

import core

import pandas as pd

import base64

import json

# Load UCI census train and test data into dataframes.

from facets_overview.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator

csv = "SampleCSVFile"

train_data = pd.read_csv(
    f'{csv}.csv')

# Create the feature stats for the datasets and stringify it.
# Display the facets overview visualization for this data

gfsg = GenericFeatureStatisticsGenerator()
proto = gfsg.ProtoFromDataFrames([{'name': 'train', 'table': train_data}])
protostr = base64.b64encode(proto.SerializeToString()).decode("utf-8")

def vaex_data():
    data = train_data.to_json(orient='records')
    return data

def vaex_proto():
    proto = protostr
    return proto