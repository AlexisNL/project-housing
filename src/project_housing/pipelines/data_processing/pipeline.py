# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:25:22 2022

@author: Alexis
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import dummies, scaler


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=dummies,
                inputs="housing",
                outputs="preprocessed_housing",
                name="preprocess_housing_node",
            ),
            node(
                func=scaler,
                inputs="preprocessed_housing",
                outputs="model_input_table",
                name="model_input_table_node",
            ),
        ],
        namespace="data_processing",
        inputs=["housing"],
        outputs="model_input_table",
    )