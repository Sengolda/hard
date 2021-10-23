import sys

if len(sys.argv) == 2:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
        if lines[-1:] == ["---end---"]:
            for x, y in enumerate(lines, start=1):
                if x == 1 and y == "---start---":
                    for line in lines:
                        if line.startswith("output"):
                            l = line.split(" ")
                            print(l[1])
