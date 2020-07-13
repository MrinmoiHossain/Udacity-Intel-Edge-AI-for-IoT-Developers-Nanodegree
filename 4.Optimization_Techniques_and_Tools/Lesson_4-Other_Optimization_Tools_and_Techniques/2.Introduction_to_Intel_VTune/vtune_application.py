from openvino.inference_engine import IENetwork
from openvino.inference_engine import IEPlugin
import numpy as np

import time
import os
import cv2
import argparse
import sys

def main(args):
    model=args.model
    device=args.device
    image_path=args.image

    # Loading model
    model_weights=model+'.bin'
    model_structure=model+'.xml'
    
    model=IENetwork(model_structure, model_weights)
    plugin = IEPlugin(device=device)

    # Loading network to device
    net = plugin.load(network=model, num_requests=1)

    # Get the name of the input node
    input_name=next(iter(model.inputs))

    # Reading and Preprocessing Image
    image=cv2.imread(image_path)
    resized_img = cv2.resize(image, (544, 320))
    input_img = np.moveaxis(resized_img, -1, 0)

    # Running Inference in a loop on the same image
    for _ in range(int(args.iterations)):
        net.infer({input_name:input_img})

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    parser.add_argument('--device', default='CPU')
    parser.add_argument('--image', default=None)
    parser.add_argument('--iterations', default=10)
    
    
    args=parser.parse_args()
    sys.exit(main(args) or 0)
