from ultralytics import YOLO

#Load the best weights from a previous batch
model=YOLO("yolov8n.pt")

#Fine-tuned using new data or more epochs
model.train(
  data="path/to/your/data.yaml",      #Same or updated dataset
  epochs=50,                          
  imgsz=640,                          
  project="path/to/save/the/project", 
  name="your_folder_name",            
  exist_ok=True                       
)
