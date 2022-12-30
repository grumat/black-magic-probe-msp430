# Fabrication Hints (V2)

## JLCPCB Order

For the fabrication of samples, use the [output\BlackPill-BMP-grumat.zip](output\BlackPill-BMP-grumat.zip) 
file. This can be sent directly to JLCPCB, as designed was once approved 
and produced in 08-Dec-2022.

These are the order details:

| Property                | Value                                 |
|:------------------------|:--------------------------------------|
| Base Material           | FR-4                                  |
| Layers                  | 2                                     |
| Dimension               | 72.5 mm * 59.7 mm                     |
| PCB Thickness           | 1.6                                   |
| Impedance Control       | No                                    |
| PCB Qty                 | 5 (min)                               |
| PCB Color               | Green (option for fastest production) |
| Silkscreen              | White                                 |
| Via Covering            | Tented                                |
| Surface Finish          | HASL(with lead)                       |
| Deburring/Edge rounding | No                                    |
| Outer Copper Weight     | 1                                     |
| Gold Fingers            | No                                    |
| Flying Probe Test       | Fully Test                            |
| Castellated Holes       | No                                    |
| Remove Order Number     | No                                    |
| 4-Wire Kelvin Test      | No                                    |
| Material Type           | FR4-Standard TG 135-140               |
| Paper between PCBs      | No                                    |
| Appearance Quality      | IPC Class 2 Standard                  |
| Confirm Production file | No                                    |
| Silkscreen Technology   | Ink-jet/Screen Printing Silkscreen    |
| Cost                    | �3.80 for 5 pcs                       |

> Note that the file **does not contain** information for pick and place 
> mounting by [JLCPCB](https://jlcpcb.com/). These are just hand soldered. 


## Soldering Tips

These are the most important hints:

- a real game changer for mounting SMD components was the acquisition of 
a magnifying lense, directly coupled to my glasses:  
[Carson 2x Clip and Flip Power Magnifying Lenses](https://amzn.eu/d/3bhR9gK)
- Tweezers and a couple of toothpicks will help handle the tiny parts.
- The recommended mounting order is very important for a good result.
- Start with components based on it's height. This helps soldering.
- Through hole elements are always mounted at the last step.
- Two soldering methods were used;
  - Solder iron, adding sufficient solder flux to avoid short circuits.
  - Hot Air gun, using a 1:1 mix of solder paste and flux.
- Recommended order:
  - Resistor networks:  **RN1**, **RN2**, **RN3**, **RN4** and **RN5**.  
  **Method:** Hot air gun.
  - ICs in the following order: **U3**, **U4**, **U5**.  
  **Method:** Solder iron.
  - SMD 0603 resistors: all of them.  
  **Method:** Solder iron.
  - SMD 0603 fuse (**F1**).  
  **Method:** Solder iron.
  - SMD 0603 capacitors: Thickness will vary on these devices and they 
  are far more trickier than SMD resistors. Solder order will depend on 
  the specific thickness of each value. Usually lower values have also 
  lower body sizes, but that is not always true when mixing brands.  
  **Method:** Solder iron.
  - SOT packaged ICs: **U2**, **U6** and **U7**
  - At this point, perform a shallow clean-up with isopropyl alcohol, a 
  toothbrush and paper towel.
  - Any SMD part not listed before should be soldered before continuing 
  the next step.
  - JTAG 14-pin Connector.  
  **Method:** Solder iron.
  - TRACESWO jumper **J4**.  
  **Method:** Solder iron.
  - BluePill jumpers (20 pin * double row).  
  **Method:** Solder iron.
  - **J7** jumper for a Logic Analyzer, in the case you want to control 
  signals.  
  **Method:** Solder iron.
  - LED **D1** (Green).  
  **Method:** Solder iron.
  - **GDB COMM** 4-pin connector.  
  **Method:** Solder iron.
- Following components are completely optional and can be ignored: 
  - 3 x Jumper set (6-pin, 5-pin and 12-pin) around BluePill.
  - 3-pin **GND** connector.
  - 2-pin **3v3** connector.
  - 2-pin **TVCC** connector.
  


## Alternative Components

### Resettable Fuse (F1)

The recommended resettable fuse is for 100 mA. The OpAmp is designed for 
250 mA, but excessive heat could be produced on that circuit.

This can be replaced by a low value resistor (2R2 to 4R7), as long as 
good practice is maintained and no short circuits are made for long 
periods.


### ESD Protection (U6 and U7)

These chips are dispensable as they have no effect on the device 
function, except for ESD discharging, which could happen when connecting 
or reconnecting cables.

In the case these components are not mounted, take care when handling 
boards, keeping your body discharged (ESD wrist cable or similar 
procedure).


### JTAG 14-pin Connector

This connector has typically a frame with a centered direction guide. You 
can use normal 2.54 mm pin-headers instead, but then you need to take 
care when inserting the JTAG cable that the red line of the flat cable is 
aligned to the pin 1 mark on the silkscreen (a tiny triangle on the 
connector drawing).


### BluePill/BlackPill Connector

Note that support for the BlackPill is currently *frozen*, so it is 
perfectly possible to solder single row socket headers instead of the 
dual row model, since they are more common.

Note at the bottom on the silkscreen the marking for the BluePill variant 
and solder the socket accordingly.

## Final Inspection

### PCB Rinsing

Before using the finalized prototype board, perform a thorough clean-up 
of the PCB removing all paste residue with isopropyl alcohol, toothbrush 
and paper towel.

### Erasing Flash

Before attaching a BluePill board, make sure that it does not contain a 
program. This depends on the programmer used.

In my case, and I highly recommend this option, I have a 
[modified STLink-Clone](https://github.com/grumat/glossy-msp430/wiki/Convert-stlink-to-bmp),
and using it to erase the flash, through the command line:

```
cd /d C:\SysGCC\arm-eabi\bin
C:\SysGCC\arm-eabi\bin>arm-none-eabi-gdb.exe
GNU gdb (GDB) 10.2.90.20210621-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "--host=i686-w64-mingw32 --target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) tar ext com4
Remote debugging using com4
(gdb) mon swdp_scan
Target voltage: 3.31V
Available Targets:
No. Att Driver
 1      STM32F1 medium density M3
(gdb) att 1
Attaching to Remote target
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
0x080005c8 in ?? ()
(gdb) flash-erase
Erasing flash memory region at address 0x08000000, size = 0x20000
(gdb) detach
Detaching from program: , Remote target
[Inferior 1 (Remote target) detached]
(gdb) quit
```

> This assume you have installed the ARM compiler for the VisualGDB tool.

### Installing BluePill onto the Prototype Board

Carefully connect the BluePill board, matching the orientation shown on 
the silkscreen drawing. Check alignment for both pin rows before pushing 
and sitting it onto the socket.

### Electrical Validation

A minimal checkup is required before using this kit:
- Ensure that the JTAG connector has no cable connected.
- Power up the BluePill using an USB cable and connected to your PC.
- Use a voltmeter and control voltages on the terminals of the prototype 
board (all voltages must be in a 5% error range):
  - The black cable of the voltmeter needs to touch the **GND** pad.
  - Use the red cable to read the list of voltage below:
  - 3v3 should produce a 3.3V value.
  - TVCC should also produce a 3.3V value.

If everything is fine, you are ready to go.

If these voltages aren't correct, then your board has some assembly 
problem, that is causing the issue.  
Some general hints are:
  - Avoid to let the board connected for a long period until you fix the 
  issue.
  - Check if the red LED of the BluePill daughter-board is on and stable; 
  you can compare the LED intensity by detaching the daughter-board. The 
  LED intensity cannot vary too much, since no component of the 
  proto-board is power-hungry, specially if no cable is present on the 
  JTAG connector.
  - Control if the U2 is warming up. In a normal operation no significant 
  temperature rise should happen. If this is the case verify U2, U3, U4, 
  U5, U6 and U7 and it's surrounding passive elements
  - Check also the temperature of the voltage regulator of the BluePill, 
  though it sits on the bottom of the board.
  - A thorough visual inspection is required to locate possible shorts.
