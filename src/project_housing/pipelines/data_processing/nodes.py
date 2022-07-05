# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:25:22 2022

@author: Alexis
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
   
def _scale(x: pd.DataFrame) -> pd.DataFrame():
    scaler = StandardScaler()
    char = x.drop('median_house_value', axis=1)
    scaler.fit_transform(char)

def _dummies(housing: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for housing dataframe.

    Args:
        housing: Raw data.
    Returns:
        Preprocessed data, with `ocean_proximity` converted to dummies
    """
    housing = pd.get_dummies(housing, columns = ['ocean_proximity'])
    return housing

def _scaler(housing: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for cancer dataframe.

    Args:
        housing: Raw data.
    Returns:
        Preprocessed data, with characteristics scaled
    """
    model_input_table = _scale(housing)
    return model_input_table