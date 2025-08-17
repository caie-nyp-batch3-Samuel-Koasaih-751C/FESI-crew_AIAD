"""Project pipelines."""
from kedro.pipeline import Pipeline
import fesi_crew_aiad.pipelines.data_ingestion as data_ingestion
import fesi_crew_aiad.pipelines.data_preprocessing as data_preprocessing
import fesi_crew_aiad.pipelines.data_split as data_split 
import fesi_crew_aiad.pipelines.mask_merge as mask_merge
import fesi_crew_aiad.pipelines.training as training

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": data_ingestion.create_pipeline()+ data_preprocessing.create_pipeline() + mask_merge.create_pipeline() + data_split.create_pipeline() + training.create_pipeline() ,
        
        "data_ingestion": data_ingestion.create_pipeline(),
        "data_preprocessing": data_preprocessing.create_pipeline(),
        "mask_merge" : mask_merge.create_pipeline(),
        "data_split": data_split.create_pipeline(),
        "training" : training.create_pipeline(),
    }