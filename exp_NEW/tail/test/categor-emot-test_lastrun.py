#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on 2018_05_23_1511
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Dense-direct'  # from the Builder filename that created this script
expInfo = {u'age': u'', u'session': u'22', u'participant': u'', u'name': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\1\\Dropbox\\Termpapers\\2017-Lykyanov Evgeny\\exp_NEW\\tail\\test\\categor-emot-test.psyexp',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1536, 864), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
Instr = visual.TextStim(win=win, name='Instr',
    text=u'\u041f\u0440\u043e\u0447\u0442\u0438\u0442\u0435 \u0432\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e!\n\n\u0421\u0435\u0439\u0447\u0430\u0441 \u043d\u0430 \u044d\u043a\u0440\u0430\u043d\u0435 \u0432\u0430\u043c \u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0435\u0434\u044a\u044f\u0432\u043b\u044f\u0442\u044c\u0441\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0443\u0449\u0435\u0441\u0442\u0432. \u0412\u0430\u043c \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0442\u043d\u0435\u0441\u0442\u0438 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a \u043e\u0434\u043d\u043e\u0439 \u0438\u0437 \u0434\u0432\u0443\u0445 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439. \u0415\u0441\u043b\u0438 \u0432\u044b \u0441\u0447\u0438\u0442\u0430\u0435\u0442\u0435, \u0447\u0442\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442 \u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0410, \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u041d\u0430\u043b\u0435\u0432\u043e. \u0415\u0441\u043b\u0438 \u0432\u044b \u0441\u0447\u0438\u0442\u0430\u0435\u0442\u0435, \u0447\u0442\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442 \u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0411, \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u041d\u0430\u043f\u0440\u0430\u0432\u043e. \u041a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442 \u043b\u0438\u0431\u043e \u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0410, \u043b\u0438\u0431\u043e \u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0411.\n\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0437\u0430\u0434\u0430\u043d\u0438\u0438 \u043d\u0435 \u0431\u0443\u0434\u0435\u0442 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438. \u0412\u043e \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u0441\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439 \u0432 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438, \u043e\u0441\u043d\u043e\u0432\u044b\u0432\u0430\u044f\u0441\u044c \u043d\u0430 \u0432\u0430\u0448\u0435\u043c \u043e\u043f\u044b\u0442\u0435 \u0438\u0437 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0433\u043e \u0437\u0430\u0434\u0430\u043d\u0438\u044f.\n\n\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b, \u0437\u0430\u0434\u0430\u0439\u0442\u0435 \u0438\u0445 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430\u0442\u043e\u0440\u0443 \u043f\u0440\u044f\u043c\u043e \u0441\u0435\u0439\u0447\u0430\u0441. \u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u041f\u0420\u041e\u0411\u0415\u041b \n',
    font='Arial',
    units='pix', pos=[0, 0], height=22, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trials"
trialsClock = core.Clock()
imageToCat = visual.ImageStim(
    win=win, name='imageToCat',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1000, 1000],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedback1"
feedback1Clock = core.Clock()


FBforIm = visual.TextStim(win=win, name='FBforIm',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=60.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
toStart = event.BuilderKeyResponse()
# keep track of which components have finished
instructionComponents = [Instr, toStart]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr* updates
    if t >= 0.0 and Instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr.tStart = t
        Instr.frameNStart = frameN  # exact frame index
        Instr.setAutoDraw(True)
    
    # *toStart* updates
    if t >= 0.0 and toStart.status == NOT_STARTED:
        # keep track of start time/frame for later
        toStart.tStart = t
        toStart.frameNStart = frameN  # exact frame index
        toStart.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(toStart.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if toStart.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            toStart.keys = theseKeys[-1]  # just the last key pressed
            toStart.rt = toStart.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if toStart.keys in ['', [], None]:  # No response was made
    toStart.keys=None
thisExp.addData('toStart.keys',toStart.keys)
if toStart.keys != None:  # we had a response
    thisExp.addData('toStart.rt', toStart.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsLoop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xls'),
    seed=None, name='trialsLoop')
thisExp.addLoop(trialsLoop)  # add the loop to the experiment
thisTrialsLoop = trialsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
if thisTrialsLoop != None:
    for paramName in thisTrialsLoop.keys():
        exec(paramName + '= thisTrialsLoop.' + paramName)

for thisTrialsLoop in trialsLoop:
    currentLoop = trialsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
    if thisTrialsLoop != None:
        for paramName in thisTrialsLoop.keys():
            exec(paramName + '= thisTrialsLoop.' + paramName)
    
    # ------Prepare to start Routine "trials"-------
    t = 0
    trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    imageToCat.setImage(categMember)
    answerForImage = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialsComponents = [imageToCat, answerForImage]
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageToCat* updates
        if t >= 0 and imageToCat.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageToCat.tStart = t
            imageToCat.frameNStart = frameN  # exact frame index
            imageToCat.setAutoDraw(True)
        frameRemains = 0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageToCat.status == STARTED and t >= frameRemains:
            imageToCat.setAutoDraw(False)
        
        # *answerForImage* updates
        if t >= 0 and answerForImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            answerForImage.tStart = t
            answerForImage.frameNStart = frameN  # exact frame index
            answerForImage.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(answerForImage.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if answerForImage.status == STARTED and t >= frameRemains:
            answerForImage.status = STOPPED
        if answerForImage.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                answerForImage.keys = theseKeys[-1]  # just the last key pressed
                answerForImage.rt = answerForImage.clock.getTime()
                # was this 'correct'?
                if (answerForImage.keys == str(corrRespIm)) or (answerForImage.keys == corrRespIm):
                    answerForImage.corr = 1
                else:
                    answerForImage.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if answerForImage.keys in ['', [], None]:  # No response was made
        answerForImage.keys=None
        # was no response the correct answer?!
        if str(corrRespIm).lower() == 'none':
           answerForImage.corr = 1  # correct non-response
        else:
           answerForImage.corr = 0  # failed to respond (incorrectly)
    # store data for trialsLoop (TrialHandler)
    trialsLoop.addData('answerForImage.keys',answerForImage.keys)
    trialsLoop.addData('answerForImage.corr', answerForImage.corr)
    if answerForImage.keys != None:  # we had a response
        trialsLoop.addData('answerForImage.rt', answerForImage.rt)
    
    # ------Prepare to start Routine "feedback1"-------
    t = 0
    feedback1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    
    FBforIm.setText('')
    # keep track of which components have finished
    feedback1Components = [FBforIm]
    for thisComponent in feedback1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *FBforIm* updates
        if t >= 0.0 and FBforIm.status == NOT_STARTED:
            # keep track of start time/frame for later
            FBforIm.tStart = t
            FBforIm.frameNStart = frameN  # exact frame index
            FBforIm.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if FBforIm.status == STARTED and t >= frameRemains:
            FBforIm.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback1"-------
    for thisComponent in feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'trialsLoop'

# get names of stimulus parameters
if trialsLoop.trialList in ([], [None], None):
    params = []
else:
    params = trialsLoop.trialList[0].keys()
# save data for this loop
trialsLoop.saveAsExcel(filename + '.xlsx', sheetName='trialsLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
