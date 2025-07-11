# Oil-Palm-Tree-Detection-with-YOLOv8
**This is an exploratory project** created while learning Python and Computer Vision. It aims to apply YOLOv8 to drone imagery for oil palm detection as part of a personal geospatial and machine learning journey.

This project demonstrates a custom-trained YOLOv8 model to detect **Oil Palm Trees** and **VOPs** (Voluntereed Oil Palms) from drone imagery.

---

## The Downside of Volunteered Oil Palms (VOPs)
**Please note:** As the project creator, I am not an agriculture professional nor do I have a background in agricultural education. This information is provided to help general audiences understand why detecting VOPs is so important in the oil palm industry.

While the model successfully detects "VOPs", their presence is generally a significant problem in commercial oil palm plantations for several key reasons, impacting efficiency and profitablility:
  
**Here's why:**
1.  **Reduced Oil Palm Yield:** Imagine you carefully plants a field with a high-yielding variety of oil palm. VOPs are like "wild" oil palm trees that sprout randomly from dropped seed. They grow from random seeds and dont't produce nearly as much valuable palm oil as the good, planned trees. This means the farm makes less oil overall.
2.  **Steaking Resources:** Every VOP growing on the farm fights the "good" oil palm trees for sunlight, water, and even food(fertilizer). This competition makes the healty, productive trees struggle, taking away resources they need to make more oil. This leads to lower harvests for the whole farm.
3.  **More Work, More Cost:** Oil palm plantations are set up with neat rows for easy harvesting and care. But VOPs sprout randomly, messing up these neat lines. This make it harder and slower for workers to harvest the fruit or take care of the trees, which drives up the plantation's cost.
4.  **Possibile Diesease Risk:** Sometimes, these unmanaged VOPs might carry pest or diseases that could then spread to the main crop, putting all the healthy oil palm trees at risk.

So, even though VOPs are technically oil palm trees, they're really like **unwanted guests** that cause problems on the plantation. 

---

## Sample Detection
<p align="center">
  <img src="Images/tile_161.jpg" width= "300"/>
  <img src="Images/tile_134.jpg" width= "300 "/>
  <img src="Images/tile_144.jpg" width= "300 "/>
  <img src="Images/tile_177.jpg" width= "300 "/>
  <img src="Images/tile_217.jpg" width= "300 "/>
  <img src="Images/tile_225.jpg" width= "300 "/>
<p/>

---

## Project Overview

### Task: Detect Oil Palm Trees Using Aerial Drone Imagery

* **Model:** YOLOv8n (Ultralytics)
* **Class:** "Oil Palm" , "VOPs"
* **Tools:** Label Studio, YOLOv8, Python, Jupyter Notebook (VS Code)

---

## Image Source & Preprocessing
The original images were captured at approximately **200 meter altitude**, where trees were too small to detect accurately.

**To address this:**
* Images were **tiled into 640*640 pixel patch**
* Only tiles representing a **visual zoom of 30-50 meters** were used for annotation
* Tiles were then used for training the YOLOv8 model.

---

## Data Annotation
A total of **387 images** were annotated using [Label-Studio](https://labelstud.io/)

Bounding boxes manually drawn for:
  * **Oil Palm** (Class 0)
  * **VOPs** (Class 1)

Images were selected under **different lighting conditions** (sunlight, shadows, varying exposures) to introduces **visually diversity** and simulate real-world drone capture scenarios.

Labels were exported in **YOLO Format**, compatible with Ultralytics training.

The final model was trained using these 387 annotated images, yielding the results you can see in the detection preview and performance charts.

### Key Consideration
While this variation in lighting helps the model to generalize slightly better, it was not aggressively optimized for light exposures. This project remains a testing and learning experiment, built for exploration and fun.

<p align="center">
  <img src="Images/Label-studio.jpg" width="600"/>
</p>

---

## Model Training

Training was performed across **five iterative batches** to progressively improve model performance.In stage 1, I used default yolov8n.pt model. Then, in stage 2-5, I fine-tuned the model using the best.pt file from the previous round. To keep things fair and consistent, I used the same training settings for all fine-tuning stages, each one was trained for 50 epochs.

## Stage 1: Initial Training from Pretrained YOLOv8n
Train using the default 'yolov8n.pt' weights and your custom data.

  [View Code: Train_Initial_YOLOv8n.py](Training/Train_Initial_Yolov8n.py)

### Stage 2-5: Fine-Tuning from previous Best Checkpoints
Each stage uses 'best.pt' model from the previous batch for further training and refinement.

  [View Code: Finetune.py](Training/Finetune.py)

### Inference (Prediction)
Run object detection on images, folders or videos using the final trained model.

  [View Code: Predict.py](Training/Predict.py)

---

## Key Results & Takeaways

* **Elevated 'VOPs' Precision:** Fine-tuning efforts yielded positive steps forward in identifying "VOPs" more accurately, and encouraging sign for this more challenging class.
* **Solid "Oil Palm" Foundations:** The model largely  retained its strong ability to detect "Oil Palm", indicating that its core capabilities were well-preserved during adaption.
* **A More Balanced Approach:** This iteration of the model demonstrates a more balanced performance across both categories, providing a more consistent detection experiences as i continue the investigation.

### Model Performance
**For a comprehensive look at the detection capabilities**

* **[Explore Pretrained Model results Here](Results/Pretrained/README_PRETRAINED.md)**
* **[Discover Fine-tuned Model & Comparision Performance Here](Results/Finetuned_model/README_FINETUNED.md)**

### Important
* **CONTEXTUAL DETECTION RANGE:** It's important to note that this model was primarily trained on imagery captured within a **30-50 meter range**. Its detection capabilities may therefore be limited or less reliable when applied to significantly higher zoom-out level images.

---

## Model in Action
Below is a sample of the model detecting Oil Palm and VOPs in actual drone-captured video:

<p align="center">
  <img src="Images/Detection.gif" width="500"/>
</p>

---

## Downloads
* [best.pt](https://github.com/Chris-pter/Oil-Palm-Tree-Detection-with-YOLOv8/raw/main/Weights/best.pt)  -Final fine-tuned model based on best validation score.
* [last.pt](https://github.com/Chris-pter/Oil-Palm-Tree-Detection-with-YOLOv8/raw/main/Weights/last.pt)  -Final checkpoint from the last training epoch.

---

## Project Scope & Learning Intent

This project was created as part of my learning journey in geospatial data, machine learning, and python. It is not intended to be a final or deployable product. but rather a hands-on exploration into how object detection works using drone imagery and YOLOv8n.

### Key Notes:
* The model was trained in a **limited datasets**(387 annotated images) and is best suited for frone imagery captured at approximately 30-50 meters in altitude.
* Annotation was done using **Label-Studio**, focusing on two classes: **Oil Palm** and **VOPs**.
* Images were captured under various lighting conditions to add diversity, but the model was not aggressively optimized for such variation.
* **No further training or model updates** are currently planned, this is intended as a personal exploration.
  
* **I hope this repository can serve as a helpful reference for others who are curious about starting out in machine learning or working with real-world drone and geospatial data.**

---

## What I Learned

<p align="justify">
This project has been a valuable stepping stone in my journey into machine learning, computer vision and Python. While the primarily goal was to try out object detection with YOLOv8, I ended up learning far more than expected, both technically and conceptually.
</p>

### Key Lessons:

* **Understanding YOLOv8 Workflow**
    * I learned how to structure a complete object detection pipeline from dataset preparation and annotation to model training, evaluation, and inference using Ultralytics YOLOv8.
    </p>
      
* **Annotation Challenges**
    * Annotating real-world drone images (especially under different lighting conditions) taught me the importance of image quality, object scale, and class balance when preparing data for training.
      
*  **The Power of Fine-Tuning**
    * I learned that starting with a pretrained model and then training it further with my own data can really help improve results, especially for classes like VOPs that did not work so well at first.

*  **Learning by Doing**
    * I found that the best way to learn machine learning is by actually doing it. Trying things out, making mistakes, and fixing them helped me understand more than just watching videos or reading. Most                         importantly, working on this project helped things make more sense.

---

## Potential Applications & Future Direction

While this project is intended as a self-exploration into computer vision and geospatial workflows, and there are no plans for further training, the current model and its development process still sugest several exciting directions this work could be extended to:

* **Crop Health monitoring**
    - Integrate NDVI or RGB-based sensors to classify tree health based on leaf color, canopy density, or even signs of pest/disease stress.
* **Mature/Immature Tree Classification**
    - Expand class labels to detect between mature palms, young palms, or recently planted areas.
* **Spatial Mapping & Yield Estimation**
    - Combine detection result with GPS/Coordinate data and plantation metadata to estimate tree counts per block or per hectare, aiding in yield planning or       auditing.
 
**This ideas are not implemented in this project but represented valuable extensions for those interested in combining machine learning with agriculture, GIS, remote sensing, particularly from a learning and experimentation perspective.**

---

## References

* [Ultralytics YOLO Docs](https://docs.ultralytics.com/)-For model training, inference, and export workflows.
* [Label Studio](https://labelstud.io/)-For flexible image annotation and YOLO-format export.

You are welcome to **explore**, **modify the base code**, and reuse it for **non-commercial learning**, **testing, and experimentation.**


















