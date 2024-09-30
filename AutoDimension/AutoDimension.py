import vs

axis = vs.IntDialog(
    "Enter 0 for horizontal measurements, 1 for vertical measurements.", 0
)

lightHandles = []
vs.ForEachObject(lightHandles.append, ("(SEL = True) & (PON = 'Lighting Device')"))
vs.DSelectAll()
lightHandles = sorted(lightHandles, key=lambda x: vs.GetSymLoc(x)[axis])
for i in range(len(lightHandles) - 1):
    pt1 = vs.GetSymLoc(lightHandles[i])
    pt2 = vs.GetSymLoc(lightHandles[i + 1])
    vs.LinearDim(pt1, pt2, 1.5 * 12, axis, 0, 1, 0)
