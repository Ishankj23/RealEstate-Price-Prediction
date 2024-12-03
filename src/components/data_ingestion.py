# Importing Packages/Libraries.
import os
import sys
import pandas as pd
from dataclasses import dataclass
# Importing Logging and Exception.
from src.exception import CustomException
from src.logger import logging
# Importing train test split to split data 80/20.
from sklearn.model_selection import train_test_split

# Securing the path for saving the train, test, and raw data, it will create a folder called artifacts and save the data there.
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

# Initializing the class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

# Reading data from the CSV file and running a train test split on it.
# logging.info will keep track of every job or process that runs.
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\Dubai edited.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            logging.info(f'Train set shape: {train_set.shape}')
            logging.info(f'Test set shape: {test_set.shape}')

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()