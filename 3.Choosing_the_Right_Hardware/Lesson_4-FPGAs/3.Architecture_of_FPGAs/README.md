One small component of an FPGA: A tile or Adaptive Logic Module (ALM). A tile consists of three major blocks:

1. **Configurable Logic Blocks (CLBs)** form the core of the FPGA and there are typically thousands of these per FPGA. Each block can implement its own function using look up tables. These functions, for example, could be Boolean Operations like AND, OR and NOT. The logic blocks also contain flip flops, transistor pairs, and multiplexers.

2. **Programmable Interconnects**, which are made up of Connection Blocks (CBs) and Switch Block (SBs), steer the input and outputs of the CLBs. Notice how each Configurable Logic Block is interconnected in four directions—and we achieve the ability to program the logic through the ability to switch these connections on and off.

3. **Programmable I/O Blocks** connect the tile to an external circuit for input and output. These external circuits are external to the current tile, but still internal to the overall FPGA. They can be other tiles, Digital Signal Processing blocks (DSPs), memory blocks, or even more I/O blocks.
