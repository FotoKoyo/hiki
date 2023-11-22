import cv2
import numpy as np
import tensorflow as tf

# Загрузка модели
model = tf.saved_model.load("mask_rcnn_coco.h5")

# Загрузка классов
with open("path/to/your/label_map.pbtxt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Загрузка изображения
image = cv2.imread("path/to/your/image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_expanded = np.expand_dims(image_rgb, axis=0)

# Передача изображения через модель
detections = model(image_expanded)

# Обработка результатов обнаружения
boxes = detections['detection_boxes'][0].numpy()
scores = detections['detection_scores'][0].numpy()
classes = detections['detection_classes'][0].numpy().astype(int)

for i in range(len(boxes)):
    if scores[i] > 0.5:  # Фильтр по порогу уверенности
        box = boxes[i]
        class_name = classes[i]
        y_min, x_min, y_max, x_max = box
        h, w, _ = image.shape
        x_min = int(x_min * w)
        x_max = int(x_max * w)
        y_min = int(y_min * h)
        y_max = int(y_max * h)

        # Рисование прямоугольника и подпись класса
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, classes[class_name], (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Отображение результата
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()