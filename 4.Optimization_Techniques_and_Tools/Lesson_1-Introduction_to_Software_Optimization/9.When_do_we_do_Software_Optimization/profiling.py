import line_profiler
profile=line_profiler.LineProfiler()
import atexit
atexit.register(profile.print_stats)
import numpy as np
import cv2
from openvino.inference_engine import IENetwork
from openvino.inference_engine import IEPlugin
import argparse

def preprocess():
    image=cv2.imread('retail_image.png')
    resized_img = cv2.resize(image, (544, 320))
    input_img = np.moveaxis(resized_img, -1, 0)

    return input_img

def load_model(args):
    model=args.model
    model_weights=model+'.bin'
    model_structure=model+'.xml'
    
    model=IENetwork(model_structure, model_weights)

    plugin = IEPlugin(device='CPU')
    
    net = plugin.load(network=model, num_requests=1)

    input_name=next(iter(model.inputs))

    return net, input_name

@profile
def main(args):

    # Loading the Model
    net, input_name=load_model(args)

    # Reading and Preprocessing Image
    input_img=preprocess()

    net.infer({input_name:input_img})

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    
    args=parser.parse_args()
    main(args)

