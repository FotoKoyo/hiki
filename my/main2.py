#import pixellib
from pixellib.instance import instance_segmentation
#import tensorflow


segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")
#target_classes = segment_image.select_target_classes(person=True)
segment_image.segmentImage("city_person2.jpeg", show_bboxes = True, output_image_name = "image_new.jpg")