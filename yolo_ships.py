'''
Train the model. Output is saved in the created runs directory.
Finished model is saved there under weights/best.pt, you can move 
it to ready_models folder to use it in the live scan.
'''

from ultralytics import YOLO
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace placeholders in config.yaml with environment variables
def preprocess_config(input_path, output_path):
    with open(input_path, "r") as file:
        config = file.read()
    # Replace placeholders with actual values from the environment
    config = config.replace("${DATASET_PATH}", os.getenv("DATASET_PATH"))
    config = config.replace("${TRAIN_PATH}", os.getenv("TRAIN_PATH"))
    config = config.replace("${VAL_PATH}", os.getenv("VAL_PATH"))
    # Write the updated config to a temporary file
    with open(output_path, "w") as file:
        file.write(config)

if __name__ == '__main__':
    # Preprocess the config file
    preprocess_config("config.yaml", "processed_config.yaml")

    # Load pretrained YOLOv8n model
    model = YOLO('ready_models/yolov8n.pt')

    # Train on the custom dataset (YOLO format required)
    model.train(
        data='processed_config.yaml',  # Use the preprocessed config file
        epochs=15,           # Number of training epochs
        imgsz=640,           # Image size for training
        batch=8,             # Batch size
        weight_decay=0.0005, # Weight decay for regularization
        project='runs',      # Directory to save training results
        name='yolo_ships',   # Name of the training run
        workers=4,           # Number of workers for data loading
        device=0             # Use GPU (0) or CPU ('cpu')
    )