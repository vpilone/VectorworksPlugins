import vs

lightPtrs = []


def main():
    vs.ForEachObject(lightPtrs.append, ("(SEL = True) & (PON = 'Lighting Device')"))
    vs.ForEachObject(copyLightToFocus, ("(SEL = True) & (PON = 'Focus Point Object')"))


def copyLightToFocus(ptr):
    for light in lightPtrs:
        focus = vs.LDevice_GetParamStr(light, 0, -2, "Focus")
        focusPt, focusZ = vs.Get3DCntr(vs.GetObject(focus))
        newFocus, newFocusZ = vs.Get3DCntr(ptr)
        newRes = tuple(map(lambda i, j: i - j, focusPt, newFocus))
        newLight = vs.HDuplicate(light, 0, 0)
        vs.Move3DObj(newLight, -newRes[0], -newRes[1], -(focusZ - newFocusZ))
        vs.LDevice_SetParamStr(newLight, 0, -2, "Focus", vs.GetName(ptr))
        vs.AlertCritical(str(newRes), "")


main()
