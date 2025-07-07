#predict.py
#Run ibject detection on images, videos, or folders using a trained YOLO model

from ultralytics import YOLO

#Load the pretrained model (.pt)
model=YOLO("path/to/your/final_model.pt")

#Run prediction
results=model.predict(  
  source="path/to/your/image_or_folder",  #e.g., "test.jpg", "images/"
  conf=0.5,                               #Confidence treshold (adjust as needed)
  save=True/False,                        #Save the output images with bounding boxes
  save_txt=True/False,                    #Save True if you want YOLO-format .txt files
  imgsz=640                               #Images siuze (should match your training size)
)
