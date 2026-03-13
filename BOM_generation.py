bom = {}

with open("pcb_components.txt") as f:
    for line in f:
        line = line.strip()
        parts = line.split(",")

        ref = parts[0]
        comp_type = parts[1]
        value = parts[2]
        footprint = parts[3]

        key = comp_type + " " + value + " (" + footprint + ")"

        bom[key] = bom.get(key, 0) + 1

print("BOM Summary:")
for component, count in bom.items():
    print(component, "→", count)