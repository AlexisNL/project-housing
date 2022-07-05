"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from project_housing.pipelines import data_processing as dp
from project_housing.pipelines import data_science as ds

def register_pipelines() -> Dict[str, Pipeline]:
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
