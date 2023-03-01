from sales.entity.config_entity import DataIngestionconfig,DataValidationconfig,DataTransformationConfig,ModelTrainerConfig,\
ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig

from sales.logger import logging

from sales.util.util import read_yaml_file

from sales.constant import * 
import os ,sys

from sales.exception import SalesException


class configuration:

    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise SalesException(e,sys) from e 

    def get_data_ingestion_config() -> DataIngestionconfig: 
        pass

    def get_data_validation_config() -> DataValidationconfig:
        pass


    def get_data_transformation_config() -> DataTransformationConfig:
        pass

    def get_model_trainer_config() -> ModelTrainerConfig:
        pass

    def get_model_evaluation_config() -> ModelEvaluationConfig:
        pass


    def get_model_pusher_config() -> ModelPusherConfig:
        pass


    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
            

        except Exception as e:
            raise SalesException(e,sys) from  e 
            
        