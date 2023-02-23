# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Automation and Machine Learning for Robust   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Self-Tuning of Magneto-Optical Traps

## Abstract  
In recent years the Magneto-Optical Trap (MOT) has become a standard technology used in almost every AMO laboratory (Atomic, Molecular, and Optical Physics). While technology of individual components has improved over time, the alignment of the trap still requires tedious maintenance performed hands-on by skilled experimentalists. The project focuses on developing a custom control system for piezoelectric mirror mounts responsible for the position adjustment of the lasers beams in the experimental setup. The implementation consists of LabVIEW interface and python algorithms, supported by rotary encoders to correct for hysteresis of the devices. The control system’s efficiency is tested through fiber coupling, typically performed manually.  
  
The feedback from the LabVIEW controllers is used in the Python program to determine the position of the center of the fiber cable and aim the laser. After successful coupling, machine learning models are used to evaluate the outputs of the entire experiment and determine the optimal experimental inputs. These models also help reveal any correlations between the mirror position, laser and fiber coupling, the rate of successful cloud creation, and the characterisitics of any resulting atom clouds. By implementing these controllers and evaluation systems, the overall goal is to fully automate this process and the experiment as a whole.

## Introduction  
Magneto-optical traps (MOTs) use lasers and magnetic fields to cool and slow down atoms. Atoms are cooled down to temperatures as low as ~15 uK, which is almost absolute zero. Atoms are fed into the experiment where they collide with lasers on the x,y, and z axes. The photons in the laser collide with the atoms and cancel out some of their momentum and push them towards the laser source. This causes friction on the atoms, slowing them further with the Doppler cooling effect. Magnetic fields in a vaccuum chamber are used to pull cooled atoms towards the center and create a "trap". Atoms in the experiment are run through the phases of this trap system multiple times, with the goal of creating a cloud of atoms that is as dense and as cold as possible.

[momentum pic], [experiment pic]
  
Slowing down the atoms makes it significantly easier to study the atom's quantum characteristics. For example, if you are trying to read the license plate on a car, the slower the car the easier it is to read. The same concept applies to quantum properties of atoms. There are many parameters that must be controlled to run this experiment, typically requiring multiple skilled experimentalists and a huge time investment just to set up. It is very sensitive to environmental variables like ambient temperature and light, making it difficult to maintain experimental conditions. Very small changes such as microscropic drift over time in parts of the experimental setup can be the difference between a successful run and no atom cloud output at all.  

## Motivation
- experimental setup  
- tedious
- safety concerns
- commercial slns and limits  
- repeatability trade-off

## Methods  
- traducer setup design
- LV controller
- python controls of controller  
- homing
- message queuer setup
- feedback details  
- python optimizer

## Results  
- system response
- testing and optimization

## Discussion

## Summary and Outlook
