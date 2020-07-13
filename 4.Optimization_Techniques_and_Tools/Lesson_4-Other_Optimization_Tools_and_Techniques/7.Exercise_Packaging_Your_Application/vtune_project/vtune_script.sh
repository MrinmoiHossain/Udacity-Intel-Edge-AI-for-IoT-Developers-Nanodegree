source ~/envs/udacity/bin/activate
source /opt/intel/openvino/bin/setupvars.sh
python vtune_application.py --iterations 1000 --model person-detection-retail-0013/FP32/person-detection-retail-0013 --device CPU --image retail_image.png
