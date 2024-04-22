import vs


def main():
    vs.ForEachObject(channelLights, ("(SEL = True) & (PON = 'Lighting Device')"))


def channelLights(ptr):
    focus = vs.LDevice_GetParamStr(ptr, 0, -2, "Focus").strip()
    if focus.__len__() > 0:
        chan = 0
        if focus.__len__() > 1:
            for i in range(focus.__len__()):
                chan += (ord(focus[i - 1].lower()) - 96) * (26 ** ((i)))
        else:
            chan = ord(focus.lower()) - 96
        vs.LDevice_SetParamStr(ptr, 0, -2, "Channel", chan + offset)


offset = vs.IntDialog("Enter the offset for this system.", 0)
main()
