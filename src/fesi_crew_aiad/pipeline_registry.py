"""Project pipelines."""
from kedro.pipeline import Pipeline
import fesi_crew_aiad.pipelines.data_ingestion as data_ingestion
import fesi_crew_aiad.pipelines.data_preprocessing as data_preprocessing
import fesi_crew_aiad.pipelines.data_split as data_split 

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": data_ingestion.create_pipeline()+ data_preprocessing.create_pipeline(),
        "data_ingestion": data_ingestion.create_pipeline(),
        "data_preprocessing": data_preprocessing.create_pipeline(),
        #put mask merge here
        "data_split": data_split.create_pipeline(),
    }