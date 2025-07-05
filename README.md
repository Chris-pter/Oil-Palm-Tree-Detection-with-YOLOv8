# Oil-Palm-Tree-Detection-with-YOLOv8

**This is ab exploratory project88 created while learning Python and Computer Vision. It aims to apply YOLOv8 to drone imagery for oil palm detection as part of a personal geospatial and machine learning journey.

This project demonstrates a custom-trained YOLOv8 model to detect **Oil Palm Trees** and **VOPs** (Voluntereed Oil Palms) from drone imagery.

---

## Sample Detection
<p align="center">
  <img src=" " width= " "/>
  <img src=" " width= " "/>
  <img src=" " width= " "/>
  <img src=" " width= " "/>
  <img src=" " width= " "/>
  <img src=" " width= " "/>
<p/>

---

## Project Overview

### Task: Detect Oil Palm Trees Using Aerial Drone Imagery

* **Model:** YOLOv8n (Ultralytics)
* **Class:** "Oil Palm" , "VOPs"
* **Tools:** Label Studio, YOLOv8, Python, Jupyter Notebook (VS Code)

---

## Image Source & Preprocessing
The original images were captured at approximately *200 meter altitude**, where trees were too small to detect accurately.

**To address this:**
* Images were **tiled into 640*640 pixel patch**
* Only tiles representing a **visual zoom of 30-50 meters** were used for annotation
* Tiles were then used for training the YOLOv8 model.

---

## Data Annotation
A total of **387 images** were annotated using [Label-Studio](https://labelstud.io/)

Bouning boxes manually drawn for:
  * **Oil Palm** (Class 0)
  *  **VOPs** (Class 1)

Images were selected under **different lighting conditions** (sunlight, shadows, varying exposures) to introduces **visually diversity** and simulate real-world drone capture scenarios.

Labels were exported in **YOLO Format**, compatible with Ultralytics training.

The final model was trained using these 387 annotated images, yielding the results you can see in the detection preview and performance charts.

### Key Consideration
While this variation in lighting helps the model to generalize slightly better, it was not aggressively optimized for light exposures. This project remains a testing and learning experiment, built for exploration and fun.

<p align="center">
  <img src=" " width=" "/>
</p>

---


