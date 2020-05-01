import argparse
from helpers import load_to_IE, preprocessing
from inference import perform_inference
from sys import platform

# Get correct CPU extension
if platform == "linux" or platform == "linux2":
    CPU_EXTENSION = "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
elif platform == "darwin":
    CPU_EXTENSION = "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension.dylib"
else:
    print("Unsupported OS.")
    exit(1)

MODEL_PATH = "/home/workspace/models/"

OUTPUT_SHAPES = {
    "POSE": {"Mconv7_stage2_L1": (1, 38, 32, 57),
             "Mconv7_stage2_L2": (1, 19, 32, 57)},
    "TEXT": {"model/link_logits_/add": (1, 16, 192, 320),
             "model/segm_logits/add": (1, 2, 192, 320)},
    "CAR META": {"color": (1, 7, 1, 1),
                 "type": (1, 4, 1, 1)}
}

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Test async and sync inference.")
    # -- Create the descriptions for the commands
    m_desc = "The directory containing the models"

    # -- Create the arguments
    parser.add_argument("-m", help=m_desc, default=MODEL_PATH)
    args = parser.parse_args()

    return args


def pose_test(model_dir):
    counter = 0
    model = model_dir + "human-pose-estimation-0001.xml"
    image = "images/sitting-on-car.jpg"
    counter += test(model, "POSE", image)

    return counter


def text_test(model_dir):
    counter = 0
    model = model_dir+ "text-detection-0004.xml"
    image = "images/sign.jpg"
    counter += test(model, "TEXT", image)

    return counter


def car_test(model_dir):
    counter = 0
    model = model_dir + "vehicle-attributes-recognition-barrier-0039.xml"
    image = "images/blue-car.jpg"
    counter += test(model, "CAR META", image)

    return counter


def test(model, model_type, image):
    # Synchronous Test
    counter = 0
    try:
        # Load IE separately to check InferRequest latency
        exec_net, input_shape = load_to_IE(model, CPU_EXTENSION)
        result = perform_inference(exec_net, "S", image, input_shape)
        output_blob = next(iter(exec_net.outputs))
        # Check for matching output shape to expected
        assert result[output_blob].shape == OUTPUT_SHAPES[model_type][output_blob]
        # Check latency is > 0; i.e. a request occurred
        assert exec_net.requests[0].latency > 0.0
        counter += 1
    except:
        print("Synchronous Inference failed for {} Model.".format(model_type))
    # Asynchronous Test
    try:
        # Load IE separately to check InferRequest latency
        exec_net, input_shape = load_to_IE(model, CPU_EXTENSION)
        exec_net = perform_inference(exec_net, "A", image, input_shape)
        output_blob = next(iter(exec_net.outputs))
        # Check for matching output shape to expected
        assert exec_net.requests[0].outputs[output_blob].shape == OUTPUT_SHAPES[model_type][output_blob]
        # Check latency is > 0; i.e. a request occurred
        assert exec_net.requests[0].latency > 0.0
        counter += 1
    except:
        print("Asynchronous Inference failed for {} Model.".format(model_type))

    return counter


def feedback(tests_passed):
    print("You passed {} of 6 tests.".format(int(tests_passed)))
    if tests_passed == 6:
        print("Congratulations!")
        exit(0)
    else:
        print("See above for additional feedback.")
        exit(1)


def main():
    args = get_args()
    counter = pose_test(args.m) + text_test(args.m) + car_test(args.m)
    feedback(counter)


if __name__ == "__main__":
    main()
