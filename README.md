# White Blood Cell Detection using OpenCV Haar Cascade

## Overview

This project implements a custom White Blood Cell (WBC) detector using OpenCV's Haar Cascade framework. The detector was trained on annotated microscopic blood smear images and is capable of identifying White Blood Cells in unseen images.

The project demonstrates the complete classical object detection pipeline, including annotation processing, dataset preparation, model training, and inference.

---

## Project Objectives

* Detect White Blood Cells from blood smear images.
* Learn the Viola–Jones object detection framework.
* Understand Haar Features and AdaBoost.
* Build a complete training pipeline using OpenCV.
* Practice working with annotation data stored in JSON format.

---

## Dataset Preparation

### Positive Samples

Images containing White Blood Cells were collected and annotated.

Annotations were stored in JSON format and contained bounding box coordinates for each cell.

### Negative Samples

Images without White Blood Cells were collected and used as background samples during training.

---

## JSON Annotation Processing

A custom Python script was developed to:

* Read annotation JSON files.
* Extract White Blood Cell bounding boxes.
* Convert coordinates into OpenCV training format.
* Generate the `pos.txt` file required by OpenCV.

Example workflow:

JSON Annotation → Bounding Box Extraction → pos.txt

---

## Training Pipeline

### Step 1: Generate Positive Sample Information

* Parse annotation JSON files.
* Extract bounding box coordinates.
* Create `pos.txt`.

### Step 2: Generate Background File

* Collect negative images.
* Create `bg.txt`.

### Step 3: Create Vector Samples

```bash
opencv_createsamples -info pos.txt -num 408 -w 24 -h 24 -vec pos.vec
```

### Step 4: Train Haar Cascade

```bash
opencv_traincascade \
-data result/ \
-vec pos.vec \
-bg bg.txt \
-numPos 380 \
-numNeg 350 \
-numStages 10 \
-w 24 \
-h 24
```

---

## Technologies Used

* Python
* OpenCV
* Haar Features
* AdaBoost
* Haar Cascade Classifier
* JSON
* Matplotlib

---

## Detection Results

The trained classifier successfully detected White Blood Cells in unseen blood smear images.

Example output:

* Input: Blood smear image
* Output: Bounding boxes around detected White Blood Cells

---

## Skills Demonstrated

* Computer Vision
* Object Detection
* Data Preprocessing
* JSON Parsing
* Annotation Processing
* Bounding Box Extraction
* OpenCV
* Haar Cascade Training
* AdaBoost
* Biomedical Image Analysis

---

## Future Improvements

* Increase dataset size.
* Add evaluation metrics (Precision, Recall, F1-score).
* Compare performance with modern deep learning models.
* Implement YOLO-based White Blood Cell detection.
* Deploy as a web application.

---

## Author

Moein

Computer Vision | Machine Learning | Biomedical Data Science
