
# for giving statistics to https://github.com/DarkPlacesEngine/darkplaces/issues/49
# feed CJK translation files (as argv) to see how that bug sucks resources
# Also see a solution: https://github.com/DarkPlacesEngine/darkplaces/pull/67

import sys

chars_per_map = 256

files = sys.argv[1:]

bigblocks = (
    range(0x3400, 0x4DC0),     #   6592  CJK Unified Ideographs Extension A
    range(0x4E00, 0xA000),     #  20992  CJK Unified Ideographs
    range(0xAC00, 0xD7B0),     #  11184  Hangul Syllables
    range(0xE000, 0xF900),     #   6400  Private Use Area
    range(0x10000, 0x110000)   #         Everything above
)

for path in files:
    with open(path, 'r', encoding='utf-8') as file:
        chars = set()
        while buffer := file.read(64 << 10):
            for c in buffer:
                for block in bigblocks:
                    if ord(c) > 0xff and ord(c) in block:
                        chars.add(c)
        maps = {}
        for c in chars:
            mapstart = ord(c) - (ord(c) % chars_per_map)
            maps[mapstart] = maps.get(mapstart, 0) + 1

        all_chars_on_map = len(maps) * chars_per_map
        
        print("""
            Unique bigblock characters: %i
                  Maps needed for them: %i
             Total rendered characters: %i
                Wasted/Saved resources: %f%%
        """ % (len(chars), len(maps), all_chars_on_map, 100.0 - len(chars) / all_chars_on_map * 100))
