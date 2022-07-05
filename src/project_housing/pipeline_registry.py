"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .pipelines.data_science import pipeline as ds
from .pipelines.data_processing import pipeline as dp


def register_pipelines(**kwargs) -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    
    return {
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,    
        "__default__": data_processing_pipeline + data_science_pipeline
    }
