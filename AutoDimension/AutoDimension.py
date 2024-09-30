import vs

lightHandles = []
vs.ForEachObject(lightHandles.append, ("(SEL = True) & (PON = 'Lighting Device')"))

for i in range(len(lightHandles) - 1):
    pt1 = vs.GetSymLoc(lightHandles[i])
    pt2 = vs.GetSymLoc(lightHandles[i + 1])
    vs.LinearDim(pt1, pt2, 1.5 * 12, 0, 0, 1, 0)
