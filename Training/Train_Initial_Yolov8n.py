#Import the YOLO class from the Ultralytics package
from ultralytics import YOLO

#Load a pretrained YOLOv8 model
#Options include: 'Yolov8n.pt', 'Yolov8s.pt', 'Yolov8m.pt', etc.
model=YOLO("yolov8n.pt") #path/to/your/checkpoint/best.pt 
#Replace with your own .pt file if resuming training

#Start training the model
model.train(
  data="path/to/your/data.yaml",      #Path to your data config YAML file
  epochs=50,                          #Number of training epochs
  imgsz=640,                          #Image size (Input resolution)
  project="path/to/save/the/project", #Output directory for training results
  name="your_folder_name",            #Folder name inside the project
  exist_ok=True                       #Overwrite folder if it exist
)
