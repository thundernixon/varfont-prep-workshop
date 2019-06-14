# script by @gferreira
# https://forum.robofont.com/topic/591/copying-uppercase-to-lowercase-including-kerning-and-auto-add-unicodes/6

from glyphNameFormatter.reader import N2n, n2u

f = CurrentFont()

for glyphName in f.keys():
    glyphNameLC = N2n(glyphName)

    if glyphName == glyphNameLC:
        continue

    unicodeLC = n2u(glyphNameLC)
    if unicodeLC not in f[glyphName].unicodes:
        f[glyphName].unicodes += (unicodeLC,)

    print(glyphName, f[glyphName].unicodes)