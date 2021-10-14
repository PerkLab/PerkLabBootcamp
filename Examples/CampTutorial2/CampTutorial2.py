import os
import logging
import vtk, qt, ctk, slicer
import numpy as np
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# CampTutorial2
#

class CampTutorial2(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "CampTutorial2"  # TODO: make this more human readable by adding spaces
    self.parent.categories = ["Examples"]  # TODO: set categories (folders where the module shows up in the module selector)
    self.parent.dependencies = []  # TODO: add here list of module names that this module requires
    self.parent.contributors = ["Perk Lab (Queen's University)"]  # TODO: replace with "Firstname Lastname (Organization)"
    # TODO: update with short description of the module and a link to online module documentation
    self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
See more information in <a href="https://github.com/organization/projectname#CampTutorial2">module documentation</a>.
"""
    # TODO: replace with organization, grant and thanks
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""

    # Additional initialization step after application startup is complete
    slicer.app.connect("startupCompleted()", registerSampleData)

#
# Register sample data sets in Sample Data module
#

def registerSampleData():
  """
  Add data sets to Sample Data module.
  """
  # It is always recommended to provide sample data for users to make it easy to try the module,
  # but if no sample data is available then this method (and associated startupCompeted signal connection) can be removed.

  import SampleData
  iconsPath = os.path.join(os.path.dirname(__file__), 'Resources/Icons')

  # To ensure that the source code repository remains small (can be downloaded and installed quickly)
  # it is recommended to store data sets that are larger than a few MB in a Github release.

  # CampTutorial21
  SampleData.SampleDataLogic.registerCustomSampleDataSource(
    # Category and sample name displayed in Sample Data module
    category='CampTutorial2',
    sampleName='CampTutorial21',
    # Thumbnail should have size of approximately 260x280 pixels and stored in Resources/Icons folder.
    # It can be created by Screen Capture module, "Capture all views" option enabled, "Number of images" set to "Single".
    thumbnailFileName=os.path.join(iconsPath, 'CampTutorial2.png'),
    # Download URL and target file name
    uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95",
    fileNames='CampTutorial2.nrrd',
    # Checksum to ensure file integrity. Can be computed by this command:
    #  import hashlib; print(hashlib.sha256(open(filename, "rb").read()).hexdigest())
    checksums = 'SHA256:998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95',
    # This node name will be used when the data set is loaded
    nodeNames='CampTutorial2'
  )

  # CampTutorial2
  SampleData.SampleDataLogic.registerCustomSampleDataSource(
    # Category and sample name displayed in Sample Data module
    category='CampTutorial2',
    sampleName='CampTutorial2',
    thumbnailFileName=os.path.join(iconsPath, 'CampTutorial2.png'),
    # Download URL and target file name
    uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97",
    fileNames='CampTutorial2.nrrd',
    checksums = 'SHA256:1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97',
    # This node name will be used when the data set is loaded
    nodeNames='CampTutorial2'
  )

#
# CampTutorialWidget
#

class CampTutorial2Widget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

  def setup(self):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer).
    # Additional widgets can be instantiated manually and added to self.layout.
    uiWidget = slicer.util.loadUI(self.resourcePath('UI/CampTutorial2.ui'))
    self.layout.addWidget(uiWidget)
    self.ui = slicer.util.childWidgetVariables(uiWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    uiWidget.setMRMLScene(slicer.mrmlScene)

    # Create logic class. Logic implements all computations that should be possible to run
    # in batch mode, without a graphical user interface.
    self.logic = CampTutorial2Logic()
    self.logic.setupScene()

    # Connections

    # These connections ensure that we update parameter node when scene is closed

    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)

    # These connections ensure that whenever user changes some settings on the GUI, that is saved

    self.ui.inputMarkupSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onInputMarkupSelected)
    self.ui.opacitySliderWidget.connect("valueChanged(double)", self.onOpacitySliderChanged)
    self.ui.autoUpdateCheckBox.connect("clicked(bool)", self.onAutoUpdateClicked)
    self.ui.outputLineEdit.connect("currentPathChanged(QString)", self.onOutputPathChanged)

    self.ui.applyButton.connect('clicked(bool)', self.onApplyButton)
    self.ui.exportDataButton.connect('clicked(bool)', self.onExportButtonClicked)

    # Make sure parameter node is initialized (needed for module reload)

    self.initializeParameterNode()

    # Restore settings values on GUI

    pathValue = self.logic.getExportPath()
    if pathValue is not None and len(pathValue) > 1:
      self.ui.outputLineEdit.setCurrentPath(pathValue)

  def onExportButtonClicked(self):
    self.logic.exportSphereModel()

  def onOutputPathChanged(self, newPath):
    self.logic.setExportPath(newPath)

  def onOpacitySliderChanged(self, newValue):
    if slicer.mrmlScene.IsImporting():
      return
    logging.info("Opacity slider set to {}".format(newValue))
    self.logic.setOpacity(newValue)
    if self.ui.autoUpdateCheckBox.checked == True:
      self.onApplyButton()

  def onAutoUpdateClicked(self, checked):
    if slicer.mrmlScene.IsImporting():
      return
    self.onApplyButton()
    self.logic.setAutoUpdate(checked)

  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    self.removeObservers()

  def enter(self):
    """
    Called each time the user opens this module.
    """
    # Make sure parameter node exists and observed
    self.initializeParameterNode()

  def exit(self):
    """
    Called each time the user opens a different module.
    """
    # Do not react to parameter node changes (GUI wlil be updated when the user enters into the module)
    self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

  def onSceneStartClose(self, caller, event):
    """
    Called just before the scene is closed.
    """
    # Parameter node will be reset, do not use it anymore
    self.setParameterNode(None)

  def onSceneEndClose(self, caller, event):
    """
    Called just after the scene is closed.
    """
    # If this module is shown while the scene is closed then recreate a new parameter node immediately
    if self.parent.isEntered:
      self.initializeParameterNode()

  def initializeParameterNode(self):
    """
    Ensure parameter node exists and observed.
    """
    # Parameter node stores all user choices in parameter values, node selections, etc.
    # so that when the scene is saved and reloaded, these settings are restored.

    self.setParameterNode(self.logic.getParameterNode())

    # Select default input nodes if nothing is selected yet to save a few clicks for the user

    if not self._parameterNode.GetNodeReference(self.logic.INPUT_MARKUP):
      firstMarkupNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsFiducialNode")
      if firstMarkupNode:
        self._parameterNode.SetNodeReferenceID(self.logic.INPUT_MARKUP, firstMarkupNode.GetID())

  def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """

    # if inputParameterNode:
    #   self.logic.setDefaultParameters(inputParameterNode)

    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    # Initial GUI update
    self.updateGUIFromParameterNode()

  def updateGUIFromParameterNode(self, caller=None, event=None):
    """
    This method is called whenever parameter node is changed.
    The module GUI is updated to show the current state of the parameter node.
    """

    if slicer.mrmlScene.IsImporting() or self.logic.isImporting:
      return

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    # Make sure GUI changes do not call updateParameterNodeFromGUI (it could cause infinite loop)

    self._updatingGUIFromParameterNode = True

    # Update node selectors and sliders

    inputNode = self._parameterNode.GetNodeReference(self.logic.INPUT_MARKUP)
    self.ui.inputMarkupSelector.setCurrentNode(inputNode)
    self.ui.opacitySliderWidget.value = self.logic.getOpacity()
    self.ui.autoUpdateCheckBox.setChecked(self.logic.getAutoUpdate())

    # Update buttons states and tooltips

    if self._parameterNode.GetNodeReference(self.logic.INPUT_MARKUP) is not None:
      self.ui.applyButton.toolTip = "Compute output volume"
      self.ui.autoUpdateCheckBox.enabled = True
      self.ui.applyButton.enabled = True
    else:
      self.ui.applyButton.toolTip = "Select input and output volume nodes"
      self.ui.autoUpdateCheckBox.enabled = False
      self.ui.applyButton.enabled = False

    self._updatingGUIFromParameterNode = False  # All the GUI updates are done

  def onInputMarkupSelected(self, newNode):
    """
    This method is called when the user makes any change in the GUI.
    The changes are saved into the parameter node (so that they are restored when the scene is saved and loaded).
    """
    if slicer.mrmlScene.IsImporting() or self.logic.isImporting:
      return

    logging.info("onInputMarkupSelected")

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    if newNode is None:
      self.ui.autoUpdateCheckBox.setChecked(False)
      self.logic.setAutoUpdate(False)
      self._parameterNode.SetNodeReferenceID(self.logic.INPUT_MARKUP, None)
      logging.info("Set input markup ID: None")
    else:
      self._parameterNode.SetNodeReferenceID(self.logic.INPUT_MARKUP, newNode.GetID())
      logging.info("Set input markup ID: {}".format(newNode.GetID()))

  def onApplyButton(self):
    """
    Run processing when user clicks "Apply" button.
    """
    try:
      self.logic.updateSphere(self.ui.inputMarkupSelector.currentNode(), self.ui.opacitySliderWidget.value)

    except Exception as e:
      slicer.util.errorDisplay("Failed to compute results: "+str(e))
      import traceback
      traceback.print_exc()


#
# CampTutorial2Logic
#

class CampTutorial2Logic(ScriptedLoadableModuleLogic, VTKObservationMixin):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  # Adding member variables for names to avoid typos

  OUTPUT_PATH_SETTING = "CampTutorial2/OutputPath"

  INPUT_MARKUP = "InputMarkup"
  SPHERE_MODEL = "SphereModel"
  OPACITY = "Opacity"
  OPACITY_DEFAULT = 0.8
  AUTOUPDATE = "AutoUpdate"
  AUTOUPDATE_DEFAULT = False

  def __init__(self):
    """
    Called when the logic class is instantiated. Can be used for initializing member variables.
    """
    ScriptedLoadableModuleLogic.__init__(self)
    VTKObservationMixin.__init__(self)  # needed for scene import observation

    self.fiducialNode = None
    self.sphereNode = None

    self.observedMarkupNode = None
    self.isImporting = False

  def setupScene(self):
    """
    Creates utility nodes and adds observers
    """
    parameterNode = self.getParameterNode()
    sphereModel = parameterNode.GetNodeReference(self.SPHERE_MODEL)
    if sphereModel is None:
      sphereModel = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", self.SPHERE_MODEL)
      sphereModel.CreateDefaultDisplayNodes()
      parameterNode.SetNodeReferenceID(self.SPHERE_MODEL, sphereModel.GetID())

    self.addObserver(slicer.mrmlScene, slicer.vtkMRMLScene.StartImportEvent, self.onSceneImportStart)
    self.addObserver(slicer.mrmlScene, slicer.vtkMRMLScene.EndImportEvent, self.onSceneImportEnd)

    self.setAutoUpdate(self.getAutoUpdate())

  def exportSphereModel(self):
    """
    Saves current sphere model in the export folder as a file.
    """
    parameterNode = self.getParameterNode()
    sphereNode = parameterNode.GetNodeReference(self.SPHERE_MODEL)
    if sphereNode is None:
      logging.info("Cannot export sphere model, not created yet")
      return
    exportPath = slicer.util.settingsValue(self.OUTPUT_PATH_SETTING, "")
    fileName = sphereNode.GetName() + ".stl"
    fileFullName = os.path.join(exportPath, fileName)
    logging.info("Exporting sphere model to: {}".format(fileFullName))
    slicer.util.saveNode(sphereNode, fileFullName)

  def onSceneImportStart(self, event, caller):
    """
    Saves existing nodes in member variables to be able to compare them with new nodes about to be loaded.
    """
    logging.info("onSceneImportStart")
    self.isImporting = True
    parameterNode = self.getParameterNode()
    self.sphereNode = parameterNode.GetNodeReference(self.SPHERE_MODEL)
    self.fiducialNode = parameterNode.GetNodeReference(self.INPUT_MARKUP)

  def onSceneImportEnd(self, event, caller):
    """
    When loading a saved scene ends, this function cleans up orphan nodes.
    """
    logging.info("onSceneImportEnd")
    parameterNode = self.getParameterNode()
    currentSphereNode = parameterNode.GetNodeReference(self.SPHERE_MODEL)

    # Discard the sphere loaded, in case we set up better properties (e.g. color) for illustration

    if self.sphereNode != currentSphereNode:
      parameterNode.SetNodeReferenceID(self.SPHERE_MODEL, self.sphereNode.GetID())
      self.removeNode(currentSphereNode)

    # Use the markup loaded, because that data belongs to the "case" (e.g. patient) loaded

    currentMarkup = parameterNode.GetNodeReference(self.INPUT_MARKUP)

    if self.fiducialNode != currentMarkup:
      self.removeNode(self.fiducialNode)
      self.fiducialNode = currentMarkup

    self.isImporting = False

    # Restore module state

    self.setAutoUpdate(self.getAutoUpdate())
    self.updateSphere()

    parameterNode.Modified()  # Trigger GUI update

  def removeNode(self, node):
    """
    Removes node and its display and storage nodes from the scene.
    """
    if node is None:
      return

    for i in range(node.GetNumberOfDisplayNodes()):
      slicer.mrmlScene.RemoveNode(node.GetNthDisplayNode(i))

    for i in range(node.GetNumberOfStorageNodes()):
      slicer.mrmlScene.RemoveNode(node.GetNthStorageNode(i))

    slicer.mrmlScene.RemoveNode(node)

  def setDefaultParameters(self, parameterNode):
    """
    Initialize parameter node with default settings.
    """
    parameterNode.SetParameter(self.OPACITY, str(self.OPACITY_DEFAULT))
    parameterNode.SetParameter(self.AUTOUPDATE, "true" if self.AUTOUPDATE_DEFAULT else "false")

  def setOpacity(self, newValue):
    parameterNode = self.getParameterNode()
    parameterNode.SetParameter(self.OPACITY, str(newValue))

  def getOpacity(self):
    parameterNode = self.getParameterNode()
    opacityStr = parameterNode.GetParameter(self.OPACITY)
    if opacityStr is None or len(opacityStr) < 1:
      return self.OPACITY_DEFAULT
    else:
      return float(opacityStr)

  def setAutoUpdate(self, autoUpdate):
    parameterNode = self.getParameterNode()
    parameterNode.SetParameter(self.AUTOUPDATE, "true" if autoUpdate else "false")
    markupNode = parameterNode.GetNodeReference(self.INPUT_MARKUP)

    if self.observedMarkupNode is not None:
      self.removeObserver(self.observedMarkupNode, slicer.vtkMRMLMarkupsNode.PointModifiedEvent, self.onMarkupsUpdated)
      self.observedMarkupNode = None

    if autoUpdate and markupNode:
      self.observedMarkupNode = markupNode
      self.addObserver(self.observedMarkupNode, slicer.vtkMRMLMarkupsNode.PointModifiedEvent, self.onMarkupsUpdated)

  def getAutoUpdate(self):
    parameterNode = self.getParameterNode()
    autoUpdate = parameterNode.GetParameter(self.AUTOUPDATE)
    if autoUpdate is None or autoUpdate == '':
      return self.AUTOUPDATE_DEFAULT
    elif autoUpdate.lower() == "false":
      return False
    else:
      return True

  def setExportPath(self, newPath):
    settings = qt.QSettings()
    settings.setValue(self.OUTPUT_PATH_SETTING, newPath)

  def getExportPath(self):
    return slicer.util.settingsValue(self.OUTPUT_PATH_SETTING, None)

  def onMarkupsUpdated(self, caller, event):
    parameterNode = self.getParameterNode()
    markupNode = parameterNode.GetNodeReference(self.INPUT_MARKUP)
    opacity = self.getOpacity()
    self.updateSphere(markupNode, opacity)

  def updateSphere(self, inputMarkup, opacity):
    """
    Run the processing algorithm.
    Can be used without GUI widget.
    :param inputMarkup: vtkMRMLMarkupsFiducialNode, first two points will be used
    :param opacity: float, for output model
    """
    parameterNode = self.getParameterNode()
    outputModel = parameterNode.GetNodeReference(self.SPHERE_MODEL)

    if not inputMarkup or not outputModel:
      raise ValueError("Input or sphere model is invalid")

    if inputMarkup.GetNumberOfFiducials() < 2:
      raise Error("Too few markup points")

    import time
    startTime = time.time()
    # logging.info('Processing started')

    p0 = np.zeros(3)
    inputMarkup.GetNthFiducialPosition(0, p0)
    p1 = np.zeros(3)
    inputMarkup.GetNthFiducialPosition(1, p1)

    c = (p0 + p1) / 2.0
    r = np.linalg.norm(p1 - p0) / 2.0

    source = vtk.vtkSphereSource()
    source.SetRadius(r)
    source.SetCenter(c[0], c[1], c[2])
    source.Update()

    if outputModel.GetNumberOfDisplayNodes() < 1:
      outputModel.CreateDefaultDisplayNodes()
    outputModel.SetAndObservePolyData(source.GetOutput())
    displayNode = outputModel.GetDisplayNode()
    displayNode.SetOpacity(opacity)

    stopTime = time.time()
    # logging.info(f'Processing completed in {stopTime-startTime:.2f} seconds')

#
# CampTutorial2Test
#

class CampTutorial2Test(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear()

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_CampTutorial21()

  def test_CampTutorial21(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")

    # Get/create input data

    import SampleData
    registerSampleData()
    inputVolume = SampleData.downloadSample('CampTutorial21')
    self.delayDisplay('Loaded test data set')

    inputScalarRange = inputVolume.GetImageData().GetScalarRange()
    self.assertEqual(inputScalarRange[0], 0)
    self.assertEqual(inputScalarRange[1], 695)

    outputVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
    threshold = 100

    # Test the module logic

    logic = CampTutorial2Logic()

    # Test algorithm with non-inverted threshold
    logic.updateSphere(inputVolume, outputVolume, threshold, True)
    outputScalarRange = outputVolume.GetImageData().GetScalarRange()
    self.assertEqual(outputScalarRange[0], inputScalarRange[0])
    self.assertEqual(outputScalarRange[1], threshold)

    # Test algorithm with inverted threshold
    logic.updateSphere(inputVolume, outputVolume, threshold, False)
    outputScalarRange = outputVolume.GetImageData().GetScalarRange()
    self.assertEqual(outputScalarRange[0], inputScalarRange[0])
    self.assertEqual(outputScalarRange[1], inputScalarRange[1])

    self.delayDisplay('Test passed')
