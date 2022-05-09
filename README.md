# PerkLab bootcamp

## Logistics

- Date:	2022 May 24-26
- Location: Zoom + SpatialChat.
- Application: send your application before May 18
- Any questions? Send an email to [Andras Lasso](mailto:lasso@queensu.ca).

## Pre-requisites
- Install [3D Slicer](http://download.slicer.org/) latest stable version (4.11.20210226) -> nightly 64-bit installer. After you installed Slicer, start it, open the Extension manager, and install these extensions: SlicerIGT, SlicerOpenIGTLink, DebuggingTools, SlicerElastix, SegmentRegistration, TCIABrowser, SlicerDMRI, SlicerJupyter.
- Install [Git for Windows](https://git-scm.com/download/win) and [TortoiseGit](https://tortoisegit.org/) if you have a Windows computer. On macOS and Linux, Git client is usually already installed by default. If you are not comfortable with using softare via the terminal then install a Git client with a graphical user interface, such as [GitHub Desktop](https://desktop.github.com/).
- [VisualStudio Code](https://code.visualstudio.com/). Install the Python extension from Microsoft (ms-python.python).
- Register a user at www.github.com
- If you want to effectively participate in day 3: get familiar with Python and numpy syntax; spend some time to get to know VTK (read as much of the [VTK textbook](https://vtk.org/vtk-textbook/) as you can, try to run some of the [VTK examples](https://kitware.github.io/vtk-examples/site/) in Python) and learn about [Qt for Python](https://www.qt.io/qt-for-python) (for example, complete a few basic tutorials).
- Only for students at Queen's: Prepare with a short introduction about yourself (2-3 minutes, supported by 1-2 slides): experience, research interests, something personal
- Install zoom and familiarize yourself with [SpatialChat](https://spatial.chat/s/TryMe) (we will use it for hands-on sessions so that multiple participant can share screen and ask questions from instructors when they get stuck)
- Windows users: Download and install latest stable 64-Bit Plus (2.8.0.20191105-Win64) from [here](http://perk-software.cs.queensu.ca/plus/packages/stable/).
- Windows users: Print a set of ArUco markers from [here](https://github.com/PlusToolkit/PlusLibData/raw/master/ConfigFiles/OpticalMarkerTracker/marker_sheet_36h12.pdf) at 100% scale.
- Download NeuroNav tutorial data from [here](https://queensuca-my.sharepoint.com/:f:/g/personal/krs2_queensu_ca/Eieoe4639BJFjzVTUM5w6LcBLn5SwE3qJH7WskaNolC32A?e=j99GwT).

## Program

The program may slightly change at any time before and during the event, so please check this page regularly.
Time zone: UTC-4.

### May 24, Tuesday: Introduction, 3D Slicer basics, Project management
- 9:00 Introduction, learning spatialchat (Andras) `zoom+spatialchat`
- 9:15 3D Slicer basics (Andras) `zoom`
  - Overview: core features, community, major extensions (30 min)
- 9:45 3D Slicer basics 1/2 (Csaba/David hands-on, help: Andras, Kyle, Tamas, Csaba, David, Monica, in French: Marie) `zoom+spatialchat`
  - Visualization: load/save, sample data, viewers, models, volume rendering (30 min)
  - DICOM (15 min)
- 10:30 Break 
- 10:45 3D Slicer basics 2/2 (Andras hands-on, help: Andras, Kyle, Tamas, Csaba, David, Monica, in French: Marie)
  - Segmentation (60 min)
  - Registration: Elastix, landmark registration, SegmentRegistration, transforms, transform visualization (30 min)
- 12:15 Lunch break
- 13:00	Lab policies, available services, and guides (Tamas, Laura) _– only for students at Queen's_ `zoom`
- 13:30	Introduction of participants and instructors (all) _– only for students at Queen's_ `zoom`
- 14:15	Coffee break - bring your own beverage, get to know all the participants `zoom+spatialchat`
- 14:30	Software platform, open-source, reproducible science (Andras) `zoom`
- 15:00 Project management (Andras; hands-on, help: Kyle) `zoom+spatialchat`
- 16:00	Adjourn

### May 25, Wednesday: AI for image-guided interventions
- 9:00 AI: `zoom+spatialchat`
  - Overview (nomenclature, libraries - Tensorflow, Pytorch, MONAI, complete system) (15 min, Tamas)
  - Ultrasound training data generation (Single-slice segmentation module, 20 min, Tamas, hands-on, helpers: TBD)
  - Ultrasound AI segmentation (20 min, Tamas, hands-on, helpers: TBD)
  - Tracking data evaluation (20 min, Matthew TBD)
  - MONAILabel (15 min, Andras, hands-on, helpers: TBD)
- 10:30	Break
- 10:45 Prototyping image-guided therapy applications (Csaba, David, Monica)
- 12:15	Lunch break
- 13:00 Sequences, SlicerIGT modules (Kyle) `zoom`
- 14:30 Break
- 14:45 Neuronavigation tutorial (Kyle; hands-on, help: Andras) `zoom+spatialchat`
- 16:00	Adjourn

### May 26, Thursday: Slicer module development
- 9:00	Writing correct and understandable code (Andras) `zoom`
- 9:30	Programming Slicer - part 1: 3D Slicer programming overview (Andras) `zoom`
- 10:00 Programming Slicer - part 2: Python basics and developing simple example Python module Center of Masses (Csaba, hands-on, help: Kyle, Andras, Tamas, David, Monica, in French: Marie) `zoom+spatialchat`
- 12:15	Lunch break
- 13:00	Programming Slicer - part 3: Individual work to develop a more advanced module (hands-on, help: Kyle, Andras, Tamas) `zoom+spatialchat`
- 16:00	Adjourn

Presentation slides and additional files will be available in this repository.
