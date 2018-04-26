# PerkLab bootcamp

## Logistics

- Date:	2018 April 30 - May 2.
- Time:	9:30 AM to 4:00 PM every day.
- Location:	Goodwin Hall (25 Union Street, Kingston, ON K7L 3N6), room 524.
- Registration: please fill this [registration form](https://1drv.ms/xs/s!Arm_AFxB9yqHtIIpmmPeoMhEmeYfjw?wdFormId=%7B69951206%2D0309%2D480F%2D83E7%2D5FDA6E07874D%7D). Registration is free.
- You need to arrange travel and accommodation. Most affordable motel at walking distance is [Howard Johnson Kingston](https://www.reservationdesk.com/hotel/612046f/howard-johnson-inn-kingston-kingston-on) or you may find a room near the campus on [AirBnb](https://www.airbnb.ca/).
-	Lunch will be provided (pizza, sandwich, etc.).
- Any questions? Send an email to [Andras Lasso](mailto:lasso@queensu.ca).

## Pre-requisites
-	Prepare with a short introduction about yourself (2-3 minutes, supported by 1-2 slides): experience, research interests, something personal
-	Bring your own laptop. Windows OS is strongly recommended.
-	Install [3D Slicer](http://download.slicer.org/) latest stable version (4.8.1) -> nightly 64-bit installer. After you installed Slicer, start it, open the Extension manager, and install these extensions: SlicerIGT, Sequences, Debugging tools, SlicerElastix, SegmentRegistration
-	Install [Git for Windows](https://git-scm.com/download/win) and [TortoiseGit](https://tortoisegit.org/) if you bring a Windows computer. If you use another operating system, find a git client and get familiar with it (know how to clone a repository and push your changes).
-	[PyCharm](https://www.jetbrains.com/pycharm/) Professional Edition (you can activate it immediately with your university email address), Community version is not suitable (does not support remote debugging) 
-	Install latest version of PLUS from: http://perk-software.cs.queensu.ca/plus/packages/nightly/ -> PlusApp-...-Win32.exe package (the generic version, not Ultrasonix, Telemed, etc.). If you bring a non-Windows computer then you may not be able to follow certain hands-on exercises (less than 2 hours in total).
-	Register a user at www.github.com
- Optionally, install [Autodesk Fusion 360](https://www.autodesk.com/products/fusion-360/overview) CAD software. Register an account with a university email address to get access to Fusion 360 for free. You will be able to follow model design and 3D printing tutorial without Fusion 360, if you laptop does not meet minimum hardware requirements. If you would also print your designed models, download [Makerbot Desktop](https://support.makerbot.com/troubleshooting/makerbot-desktop-software/software-download/download_12190)

## Preliminary program (subject to change)

### April 30, Monday: Introduction

- 9:30	Lab policies, available services, and guides – required only for PerkLab members (Thomas/Tamas)
- 10:00	Introduction of participants and instructors – with tea and cookies.
- 11:00	Software platform, open-source, reproducible science (Andras)
- 11:30 Project management (Andras, Mark)
- 12:30	Lunch break (pizza)
- 13:00	3D Slicer basics (Csaba, Andras, Mark)
  - Overview: core features, community, major extensions (30 min)
  - Visualization: load/save, sample data, viewers, models, volume rendering (30 min)
  - DICOM: tags, where to get them (web, TCIA browser), loading options, plugins, export (15 min)
  - Segmentation: (45 min, Andras)
  - Registration: BRAINS, Elastix, landmark registration, SegmentRegistration, transforms, transform visualization (45 min)
  - Other: Sequences, MatlabBridge, Virtual reality (15 min)
- 16:00	Adjourn

Dinner 6pm at [Brew Pub](https://www.kingstonbrewing.ca/) (optional, $)

### May 1, Tuesday: Tracking and imaging
- 9:30	Tracking basics, Coordinate systems and transforms (Tamas)
- 10:30	PLUS main features (Matthew, Kyle)
- 11:00	Writing Plus config files for tracking and image acquisition (Matthew, Kyle)
- 12:00	Lunch break (sandwich)
- 12:30 Design for 3D printing (Tamas)
- 13:30	SlicerIGT modules: neuronavigation - calibrations, visualization (Matthew, Tamas, Mark)
- 15:30	Perk Tutor (Matthew, Zsuzsanna)
- 16:30	Break
- 17:00 Social (Mario Kart, snacks)

### May 2, Wednesday: Slicer module development
- 9:30	Writing correct and understandable code (Andras)
- 10:30	3D Slicer module types and programming Slicer - part 1 (Csaba, Andras, Matthew): Python basics and developing simple example Python module Center of Masses
- 12:30	Lunch break (sushi)
- 13:00	3D Slicer module types and programming Slicer - part 2 (Csaba, Andras, Kyle): Individual work to develop a more advanced module
- 16:00	Adjourn

Presentation slides and additional files will be available in this repository.
