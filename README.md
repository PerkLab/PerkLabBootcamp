# PerkLab bootcamp

## Logistics

- Date:	2021 May 3-5.
- Location: online.
- Application: Apply using [this form](https://forms.gle/SCY3oxFrmDd7VVM86) by April 27, 2021. Application is open to everyone but if there are more interested people than we can accommodate then we will have to prioritize accepting applications from our collaborators. We will notify each applicant by April 28.
- Any questions? Send an email to [Andras Lasso](mailto:lasso@queensu.ca).

## Pre-requisites
- Install [3D Slicer](http://download.slicer.org/) latest stable version (4.11.20210226) -> nightly 64-bit installer. After you installed Slicer, start it, open the Extension manager, and install these extensions: SlicerIGT, SlicerOpenIGTLink, DebuggingTools, SlicerElastix, SegmentRegistration, TCIABrowser, SlicerDMRI, SlicerJupyter.
- Install [Git for Windows](https://git-scm.com/download/win) and [TortoiseGit](https://tortoisegit.org/) if you have a Windows computer. On macOS and Linux, Git client is usually already installed by default. If you are not comfortable with using softare via the terminal then install a Git client with a graphical user interface, such as [GitHub Desktop](https://desktop.github.com/).
- [VisualStudio Code](https://code.visualstudio.com/). Install the Python extension from Microsoft (ms-python.python).
- Register a user at www.github.com
- If you want to effectively participate in day 3: get familiar with Python and numpy syntax; spend some time to get to know VTK (read as much of the [VTK textbook](https://vtk.org/vtk-textbook/) as you can, try to run some of the [VTK examples](https://kitware.github.io/vtk-examples/site/) in Python) and learn about [Qt for Python](https://www.qt.io/qt-for-python) (for example, complete a few basic tutorials).
- Only for PerkLab members: Prepare with a short introduction about yourself (2-3 minutes, supported by 1-2 slides): experience, research interests, something personal

## Preliminary program (subject to change)

### May 3, Monday: Introduction
- 9:30	Lab policies, available services, and guides (Tamas) _– only for PerkLab members_
- 10:00	Introduction of participants and instructors (all) _– only for PerkLab members_
- 11:00	Software platform, open-source, reproducible science (Andras)
- 11:30 Project management (Andras, Kyle)
- 12:30	Break
- 13:30	3D Slicer basics (Andras, Kyle)
  - Overview: core features, community, major extensions (30 min)
  - Visualization: load/save, sample data, viewers, models, volume rendering (hands-on, 30 min)
  - Segmentation (hands-on, 30 min)
  - Registration: Elastix, landmark registration, SegmentRegistration, transforms, transform visualization (hands-on, 30 min)
  - Other: DICOM, SlicerJupyter (15 min)
- 16:00	Adjourn

Dinner 6.30pm at [Red House](http://www.redhousedowntown.ca/) ($)

### May 4, Thursday: Tracking and imaging
- 9:30	Tracking basics, Coordinate systems and transforms (Tamas)
- 10:30	PLUS toolkit main features, writing Plus config files for tracking and image acquisition (Kyle)
- 11:00	Sequences, SlicerIGT modules: neuronavigation - calibrations, visualization (hands-on, Kyle, Andras)
- 12:30	Break
- 13:30 Deep learning introduction (Tamas)
- 14:00	Create training data (hands-on, Tamas)
- 15:00	Train networks (Tamas)
- 15:30	Use networks in 3D Slicer (hands-on, Tamas)
- 16:30	Adjourn


### May 5, Friday: Slicer module development
- 9:30	Writing correct and understandable code (Andras)
- 10:30	3D Slicer module types and programming Slicer - part 1 (Kyle, Andras, Tamas): Python basics and developing simple example Python module Center of Masses
- 12:30	Break
- 13:00	3D Slicer module types and programming Slicer - part 2 (Kyle, Andras, Tamas): Individual work to develop a more advanced module
- 16:00	Adjourn

Presentation slides and additional files will be available in this repository.
