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

    vs.SetSelect(line)
    vs.GetLine(_DrawPhotometrics)


_setVariables()
vs.ForEachObject(_SetupPhotometrics, ("(SEL = True)"))


# vs.ForEachObject(channelLights, ("(SEL = True) & (PON = 'Lighting Device')"))
