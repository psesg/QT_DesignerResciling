old_file = "GetDoublesGUIOld.ui"  #"SoundAlphaOld.ui"
new_file = "GetDoublesGUINew.ui"  #"SoundAlphaNew.ui"

# Old resolution
oldx = 1920.0
oldy = 1080.0
# New resolution for MBP
newx = 2560.0
newy = 1600.0

ratiox = newx / oldx
ratioy = newy / oldy


def find_between(s, first, last):
    start = s.index(first) + len(first)
    end = s.index(last, start)
    return s[start:end]


with open(old_file, 'r', encoding='utf-8') as f:
    for line in f:
        if "<width>" in line:
            num = float(find_between(line, "<width>", "</width>"))
            # Fix resolution
            old_size = str(int(num))
            new_size = str(int(num * ratiox))
            w = line.replace(old_size, new_size)
        elif "<height>" in line:
            num = float(find_between(line, "<height>", "</height>"))
            # Fix resolution
            old_size = str(int(num))
            new_size = str(int(num * ratioy))
            w = line.replace(old_size, new_size)
        elif "<x>" in line:
            num = float(find_between(line, "<x>", "</x>"))
            # Fix resolution
            old_size = str(int(num))
            new_size = str(int(num * ratiox))
            w = line.replace(old_size, new_size)
        elif "<y>" in line:
            num = float(find_between(line, "<y>", "</y>"))
            # Fix resolution
            old_size = str(int(num))
            new_size = str(int(num * ratioy))
            w = line.replace(old_size, new_size)
        else:
            w = line
        with open(new_file, 'a', encoding='utf-8') as g:
            g.write(w)
