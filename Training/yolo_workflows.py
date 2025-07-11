from ultralytics import YOLO

def train_initial():
  model=YOLO("yolov8n.pt)
  model.train(
    data="path/to/data.yaml",
    epochs= ,
    imgsz= ,
    project= ,
    name= ,
    exist_ok=True/False
)

#----------Fine-Tune from previous Checkpoint-----------

def finetune_model():
  model=YOLO("path/to/previous batch/weights/best.pt")
    model.train(
    data="path/to/data.yaml",
    epochs= ,
    imgsz= ,
    project= ,
    name= ,
    exist_ok=True/False
)

#----------Inference-----------

def run_inference():
  model=YOLO("path/to/final_model.pt")
  results=model.predict(
    source="path/to/image_or_folder/video",
    conf=0.5,
    save=True,
    imgsz=640
  )

#----Main Execution Section----

if _name_=="_main_":
  #Choose one to run:
    #Train_initial()
    #fFineTune()
    #Predict_inference()
  #run_inference()-----Un-comment the one you want to run
