import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "data/test/BloodImage_00296.jpeg"
CASCADE_PATH = "result/cascade.xml"

cascade = cv2.CascadeClassifier(
    CASCADE_PATH
)

image = cv2.imread(IMAGE_PATH)

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

detections = cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

print(
    f"Detected {len(detections)} White Blood Cells"
)

for (x, y, w, h) in detections:

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 0, 255),
        2
    )

image_rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(8, 6))
plt.imshow(image_rgb)
plt.axis("off")
plt.show()
