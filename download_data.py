#!pip install roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="zA8ErBvsGQPdQxtdNeiW")

project = rf.workspace("yolov8-jfxhg").project("helmet-detection-yolov8")

version = project.version(1)

dataset = version.download("yolov8")