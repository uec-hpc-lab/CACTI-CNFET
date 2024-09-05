# CACTI-CNFET
The CACTI-CNFET project is to develop open source toolsets for estimating the timing, power, and area of SRAMs designed with predictive sub-10nm carbon nanotube field effect transistor (CNFET) technology. The source code for SRAMs with the 5nm CNFET technology used in the state-of-the-art research work that designs the OpenSPARC T2 processor with CNFETs is now open and helps to analyze the timing, power, and area of SRAMs manufactured with this technology. Our CACTI-CNFET was developed on top of CACTI6.5, which is a widely used tool to estimate the timing, power, and area of silicon-based SRAMs. For more details on CACTI-CNFET, see our ASP-DAC'25 paper.

## Prerequisites
- Python: 3.8 or later
- gcc/g++: 4.8.5 or later

## Build
Clone this repository and then execute *make*.

## Usage
The usage of CACTI-CNFET is almost the same as that of CACTI. If you use the 5nm CNFET technology we newly defined, please set '0.005' to the technology node.

To assess the timing, power, and area of subarrays, we added *test mode* into our CACTI-CNFET. If you would like to use the test mode, please use the option "-test 1." 

To reproduce the results of our ASP-DAC'25 paper, please execute the following command, making the directory *cacti_result_raw*, which includes the CSV files of the timing, power, and area data of the 49 SRAMs used in our paper.

```
python autocacti.py
```

## Related publication
If you use our CACTI-CNFET in any published work, we would appreciate a citation for the following paper.

S. Miwa, E. Sekikawa, T. Yang, R. Shioya, H. Yamaki, and H. Honda, CACTI-CNFET: an Analytical Tool for Timing, Power, and Area of SRAMs with Carbon Nanotube Field Effect Transistors, In Proceedings of the 30th Asia and South Pacific Design Automation Conference (ASP-DAC), 2025.

## License
Our CACTI-CNFET has a BSD 3-Clause license.

## Contact
If you have any questions or problems, please contact cnfet@hpc.is.uec.ac.jp.
