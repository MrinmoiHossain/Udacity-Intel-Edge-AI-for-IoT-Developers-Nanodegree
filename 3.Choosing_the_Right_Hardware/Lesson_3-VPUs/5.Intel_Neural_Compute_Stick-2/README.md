The key features of the Intel NCS2:
* **VPU** The processor in the NCS2 is the Myriad X VPU.
* **Software development kit** With the integration of OpenVino Toolkit the Intel NCS2 offers pre-trained models to be run on the stick. This allows ease in the use of the hardware.
* **Operating System** The NCS2 supports all of the same operating systems as OpenVINO, including Ubuntu, Windows 10, and MacOS.
* **Precision** The NCS2 only supports FP16 model precision.
* **Interface** The NCS2 has a convenient USB3.1 plug and play interface. Note that the NCS2 can be used on systems with only a USB2 port, but the inference will run slower due to I/O throttling.
* **Cost** Compared to other AI accelerators, the NCS2 is an inexpensive option, typically costing around $70 to $100.
* **Scalability** Adding multiple NCS2s (or other Myriad X devices) will allow multiple inferences to run in parallel.
* **Size** All of these features come in a small size of 72.5mm X 27mm X 14mm, with the looks of a standard thumb drive.


## FPS vs. Power Tradeoff

One other characteristic that is important to note about the NCS2 is that it is meant to be a low-power device so that it can be easily deployed at the edge; however, one drawback of this is that it cannot process as many frames per second (FPS) as some other devices and thus it has a higher inference time.

For example, if we compare the NCS2 with an Atom E3950 processor, we can see that the Atom will have better FPS, but higher power requirements. The Atom processor (even though it is a relatively low-power processor) has about 12 times the power requirements of the NCS2. Thus, there is a tradeoff between power requirements and performance; the NCS2 is extremely low power, but this can come at some cost to performance as compared to the Atom.

