import vs


def main():
    vs.ForEachObject(channelLights, ("(SEL = True) & (PON = 'Lighting Device')"))


def channelLights(ptr):
    focus = vs.LDevice_GetParamStr(ptr, 0, -2, "Focus")
    chan = ord(focus.lower()) - 96
    vs.LDevice_SetParamStr(ptr, 0, -2, "Channel", chan + offset)


offset = vs.IntDialog("Enter the offset for this system.", 0)
main()
