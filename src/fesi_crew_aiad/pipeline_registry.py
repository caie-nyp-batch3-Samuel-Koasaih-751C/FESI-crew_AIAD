"""Project pipelines."""
from kedro.pipeline import Pipeline
import fesi_crew_aiad.pipelines.data_ingestion as data_ingestion

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": data_ingestion.create_pipeline(),
        "data_ingestion": data_ingestion.create_pipeline(),
    }