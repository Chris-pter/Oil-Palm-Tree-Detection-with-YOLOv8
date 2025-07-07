## **YOLOv8n Fine-tuned Model Performance**

This reporsitory section details the enhanced performance of the fine-tuned YOLOv8n model on the custom Oil Palm and VOPs dataset. This fine tuning process aimed to adapt the model's generalized knowledge to the specific characteristics of our target objects, building upon the baseline established by the pretrained model.

### **Insights from Fine-Tuning**
While exploring YOLOv8n fine-tuning, I noticed encouraging improvements compared to the base pretrained model. One of the most interesting results was the better performance on the 'VOPs' class, which initially lagged behind 'Oil Palm'. After a few training rounds, the model seems to reduce false positives for VOPs, making the detection more consistent.

The overall mAP@0.5 dropped just slightly from 0.972 to 0.9689, something I'm still trying to understand fully but it seems like this trade-off actually helped the model become more balanced between both class. Aso, the F1 score stayed strong at 0.92, but now peaks at a slightly lower confidence threshold (0.397 vs 0.459), which might suggest the model is becoming better calibrated in this dataset.

* Overall, this was a valueable learnining experience in how fine-tuning affects precision, recall, and confidence calibration, especially in real-world image conditions and class imbalance. There's still room to improve, but this step showed me how subtle changes during training can shift model behavior in meaningful ways.

---

## **Performance Analysis & Comparison**

<h4 align="center">Precision-Confidence Curves: Pretrained vs. Fine-tuned</h4>
<p align="center">
<img src="../pretrained/P_curve.png" alt="Pretrained YOLOv8n Precision-Confidence Curve" width="48%">
<img src="P_curve.png" alt="Fine-tuned YOLOv8n Precision-Confidence Curve" width="48%">
</p>
<p align="center">
<em>Figure 1: Side-by-side comparison of Precision-Confidence curves. The fine-tuned model (right) demonstrates a marked improvement in 'VOPs' precision, closing the performance gap with 'Oil Palm' compared to the pretrained model (left).</em>
</p>

---

<h4 align="center">F1-Confidence Curves: Pretrained vs. Fine-tuned</h4>
<p align="center">
<img src="../pretrained/F1_curve.png" alt="Pretrained YOLOv8n F1-Confidence Curve" width="48%">
&nbsp; &nbsp; &nbsp; &nbsp;
<img src="F1_curve.png" alt="Fine-tuned YOLOv8n F1-Confidence Curve" width="48%">
</p>
<p align="center">
<em>Figure 2: Side-by-side comparison of F1-Confidence curves. In the fine-tuned model (right), the F1 score for 'VOPs' seems much closer to 'Oil Palm', which I think suggests a more balanced precision-recall relationship. Interestingly, the optimal confidence threshold also shifted slightly to 0.397, but it looks like the model might be calibrating better after training on more specific examples.</em>
</p>

---

<h4 align="center">Precision-Recall Curves: Pretrained vs. Fine-tuned</h4> 
<p align="center"> 
  <img src="../pretrained/PR_curve.png" alt="Pretrained YOLOv8n Precision-Recall Curve" width="48%">
  <img src="PR_curve.png" alt="Fine-tuned YOLOv8n Precision-Recall Curve" width="48%"> 
</p> 
<p align="center"> <em>Figure 3: Side-by-side Precision-Recall comparison. The fine-tuned model (right) appears to maintain a more balanced relationship between precision and recall for both 'Oil Palm' and 'VOPs'. Although there's a small dip in overall mAP@0.5 (from 0.972 to 0.968), the curve shape feels more stable especially for VOPs which could mean the model is gaining better confidence in handling both classes. Still learning how to interpret these details, but the improvement looks promising.</em> 
</p>

---

<h4 align="center">Normalized Confusion Matrix: Pretrained vs. Fine-tuned</h4> 
<p align="center"> 
  <img src="../pretrained/confusion_matrix_normalized.png" alt="Pretrained YOLOv8n Confusion Matrix" width="48%">
  <img src="confusion_matrix_normalized.png" alt="Fine-tuned YOLOv8n Confusion Matrix" width="48%"> 
</p> 
<p align="center"> <em>Figure 4: Comparison of normalized confusion matrices. After fine-tuning (right), the class separation between 'Oil Palm' and 'VOPs' looks more distinct, with noticeably fewer misclassifications. It seems that the model is now doing a better job at correctly identifying VOPs which was the weaker class during initial training though I'm still exploring how to interpret these improvements more deeply</em> </p>

---

<h4 align="center">Training and validation Progress: Pretrained vs. Fine-tuned</h4> 
<p align="center"> 
  <img src="../pretrained/pretrained_result.png" alt="Pretrained YOLOv8n Training Progress" width="48%">
  <img src="Fine-tuned results.png" alt="Fine-tuned YOLOv8n Training Progress" width="48%"> 
</p> 
<p align="center"> <em>Figure 5: A visual comparison of how training and validation metrics evolved over time. While I'm still learning how to interpret these curves fully, the fine-tuned model (right) seems to show a more stable trend in precision, recall, and mAP across epochs. Compared to the initial pretrained run (left), this suggests that the model might be adapting more effectively to my dataset as training progresses. It's been interesting to see how each training round shapes the learning behavior..</em> </p>



