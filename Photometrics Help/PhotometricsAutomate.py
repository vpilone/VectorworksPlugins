import vs
import Vectorworks_Photometrics as VPDialog

# area height in feet
areaHeight = 6
isToplight = False


def _setVariables():
    areaHeight = vs.IntDialog("Please enter the height of your area in feet", "6")
    isToplight = vs.YNDialog("Is this toplight?")


def _SetupPhotometrics(line):
    def _DrawPhotometrics(pt1, pt2):
        vs.MoveTo(pt1)
        upperPt = pt1
        upperPt.y += 6
        vs.LineTo(upperPt)
        vs.MoveTo(upperPt)
        vs.LineTo(pt2)
        drawnLine1 = vs.LNewObj()
        if pt1.x == vs.GetSegPt1(line).x:
            vs.MoveTo(vs.GetSegPt2(line))
        else:
            vs.MoveTo(vs.GetSegPt1(line))
        vs.LineTo(pt2)
        drawnLine2 = vs.LNewObj()

    vs.SetSelect(line)
    vs.GetLine(_DrawPhotometrics)


_setVariables()
vs.ForEachObject(_SetupPhotometrics, ("(SEL = True)"))
