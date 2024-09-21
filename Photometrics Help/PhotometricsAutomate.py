import vs

# import Vectorworks_Photometrics as VPDialog

# area height in feet
areaHeight = 6
isToplight = False
lineHandles = []
global activehandle

userPt1 = vs.GetMouse()
userPt2 = vs.GetMouse()


def _setVariables():
    areaHeight = vs.IntDialog("Please enter the height of your area in feet", "6")
    # isToplight = vs.YNDialog("Is this toplight?")


# called by getline
def _SavePts(LinePt1, LinePt2):
    global userPt1
    userPt1 = LinePt1
    global userPt2
    userPt2 = LinePt2
    _SetupPhotometrics()


# called by _savePts
def _SetupPhotometrics():
    vs.MoveTo(userPt1)
    upperPt = (userPt1[0], userPt1[1] + (areaHeight * 12))
    vs.LineTo(upperPt)
    vs.MoveTo(upperPt)
    vs.LineTo(userPt2)
    endPt = vs.GetMouse()
    if userPt1[0] == vs.GetSegPt1(activehandle)[0]:
        endPt = vs.GetSegPt2(activehandle)

    else:
        endPt = vs.GetSegPt1(activehandle)
    vs.MoveTo(endPt)
    vs.LineTo(userPt2)
    vs.AngularDim(upperPt, endPt, userPt2, 48, 771, 770, 0)


_setVariables()
vs.ForEachObject(lineHandles.append, "(SEL = True)")
# Because Get Line cannot be used inside of a function and does not stop exectuion it is basically main()
for handle in lineHandles:
    activehandle = handle
    vs.GetLine(_SavePts)
