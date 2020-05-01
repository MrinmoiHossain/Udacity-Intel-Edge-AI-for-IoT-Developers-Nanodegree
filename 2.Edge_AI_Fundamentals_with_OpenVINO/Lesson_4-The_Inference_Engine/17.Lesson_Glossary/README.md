## Inference Engine

Provides a library of computer vision functions, supports calls to other computer vision libraries such as OpenCV, and performs optimized inference on Intermediate Representation models. Works with various plugins specific to different hardware to support even further optimizations.

## Synchronous

Such requests wait for a given request to be fulfilled prior to continuing on to the next request.

## Asynchronous

Such requests can happen simultaneously, so that the start of the next request does not need to wait on the completion of the previous.

## IECore

The main Python wrapper for working with the Inference Engine. Also used to load an IENetwork, check the supported layers of a given network, as well as add any necessary CPU extensions (CPU extensions were removed in versions from 2020R1 onward).

## IENetwork

A class to hold a model loaded from an Intermediate Representation (IR). This can then be loaded into an IECore and returned as an Executable Network.

## ExecutableNetwork

An instance of a network loaded into an IECore and ready for inference. It is capable of both synchronous and asynchronous requests, and holds a tuple of InferRequest objects.

## InferRequest

Individual inference requests, such as image by image, to the Inference Engine. Each of these contain their inputs as well as the outputs of the inference request once complete.
