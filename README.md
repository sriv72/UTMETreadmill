# UTMETreadmill
Control systems developed for functionality of an oscillatory treadmill platform. Part of the requirements for Senior Design (ME 266K) for Mechanical Engineering at the University of Texas at Austin, Fall 2023.

## Requirements
- Windows PC
- LabVIEW 2019 with MyRIO Software Bundle (download [here](https://www.ni.com/en/support/downloads/software-products/download.labview-myrio-software-bundle.html#305936))
- Optional: Git (download [here](https://git-scm.com/downloads)) if you want version control, otherwise downloading as a .zip should also work
- Optional: Drive CM Configuration Software (download [here](https://www.automationdirect.com/support/software-downloads?itemcode=Drive%20CM%20Configuration#))
- Optional: Python 3.6 or later for running script to modify acceleration values

## How to Use
After installing the required softwares and cloning the repository to your local machine, open the UTME_Treadmill.lvproj project file in LabVIEW. From there, open Main.vi to view the GUI for the software. To run the software, make sure that the Servo Drive is powered by turning on the surge protector before clicking the run button in LabVIEW. The computer must be connected to the MyRIO using the provided USB cable. If the program asks whether to save changes to certain files or not, click save as this may occur when connecting for the first time. Once the code is written to the MyRIO hardware and the completion message is closed, the Servo Drive should read P-run to indicate that the servor is on and ready to run.

### Homing
Prior to turning the software switch on, the treadmill platform should be homed by pressing the HOME button while still in the off state. This will initiate the homing procedure in which the platform will use the 3 limit switches to reset the platform to the origin point.

### Operation Modes
The treadmill has two operation modes: Single and Continuous. In Single mode, the user can specify the location, acceleration, and direction for the platform to travel, with a GO button to initiate the movement. In Continuous mode, the treadmill will continuously oscillate between the leftmost and rightmost positions for a given displacement at the provided acceleration.

To activate both modes, the OFF/ON switch must be turned to ON. When the switch is turned off, the treadmill will return to the origin. There is also a stop button that serves as an emergency stop for both the treadmill and the software. Keep in mind that when this button is pressed while the system is moving, the treadmill will stop as quickly as possible regardless of its position, meaning that it must be reset when the software is turned on again.

### Outputs
The outputs for the software include both encoder output in terms of analog voltage output as well as error out in the case of communication errors with the hardware. The encoder output was originally meant to display positional data, but couldn't be properly implemented due to time constraints. 

### Using DriveCM
If desired, the DriveCM software can be used to manually jog/send inputs to the motor and/or update motor/index configurations. To communicate with the Servo Drive using DriveCM, the computer must be plugged into the Servo Drive using the provided USB cable. The motor configuration and index preset files used for setting up the motor system are provided in this repository. For more information on how to use DriveCM, [here](https://www.youtube.com/watch?v=_frHrodUB5I&list=PLPdypWXY_ROrmv1rvx_KLrxFEm1wZPbL2) is a helpful video playlist provided by AutomationDirect.

### Changing Acceleration Settings
By default, there are 5 acceleration options of 1, 2, 3, 4, and 5 m/s^2, however these values can easily be changed using the following procedure:

1. Edit the acceleration values in the Accelerations.txt file to desired decimal acceleration values in terms of m/s^2 and save the file.
2. Run the AccToPresets.py file to generate the index configuration file UTME_Treadmill_Index_Presets.txt.
3. Load the new index configuration file into DriveCM and save to the servo drive's non-volatile memory.

There are provided default files which can be used if you want to reset to the original provided acceleration values. Please do not delete these files as the script relies on the default files to create the new index configuration.
