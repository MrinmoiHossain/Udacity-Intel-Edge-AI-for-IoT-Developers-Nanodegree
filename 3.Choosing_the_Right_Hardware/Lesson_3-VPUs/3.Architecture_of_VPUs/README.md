# Architecture of VPUs

## Interface Unit
The interface unit is the part of the VPU that interacts with the host device. This host device could be a CPU or any other processing device. We would train our machine learning models on the host device and then run the inference on the VPU. VPUs are available with a variety of connection types (such as USB 3.1 and Gigabyte Ethernet), making it possible to add a VPU to many different types of pre-existing systems.

## Imaging Accelerators
As we said earlier, VPUs are specialized for image processing. One example of this specialization is found in the imaging accelerators, which have specific kernels that are used for image processing operations. These operations range from simple techniques for denoising an image, to algorithms for edge detection.

## Neural Compute Engine
Modern Intel VPUs, such as the Myriad X, feature a neural compute engine, which is a dedicated hardware accelerator optimized for running deep learning neural networks at low power without any loss in accuracy.

## Vector processors
Vector processors, as the name suggests, are processors that work on a vector or an array of 1D data. They can be contrasted with scalar processors, which often work on single data items. In general, with single data items, instructions are executed in a sequential manner, which increases the time required for execution. In contrast, the vector processors in a VPU can break up a complex instruction and then execute many tasks in a parallel manner.

## On-chip CPUs
VPUs have specialized on-chip CPUs. The Myriad X VPU has two: one used to run the host interface and the other is used for on-chip coordination between the Neural Compute Engine (NCE), the vector processor, and the imaging accelerators.
