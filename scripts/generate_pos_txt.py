import os
import json

JSON_FOLDER = "data/ann"
IMAGE_FOLDER = "data/pos"
OUTPUT_FILE = "pos.txt"

with open(OUTPUT_FILE, "w") as f_out:

    for filename in os.listdir(JSON_FOLDER):

        if not filename.endswith(".json"):
            continue

        json_path = os.path.join(JSON_FOLDER, filename)

        with open(json_path, "r") as f:
            data = json.load(f)

        img_name = filename.replace(".json", "")
        img_path = os.path.join(IMAGE_FOLDER, img_name)

        boxes = []

        for obj in data.get("objects", []):

            if obj.get("classTitle") == "WBC":

                exterior = obj["points"]["exterior"]

                xmin, ymin = exterior[0]
                xmax, ymax = exterior[1]

                width = xmax - xmin
                height = ymax - ymin

                boxes.append(
                    f"{xmin} {ymin} {width} {height}"
                )

        if boxes:

            box_str = " ".join(boxes)

            line = (
                f"{img_path} "
                f"{len(boxes)} "
                f"{box_str}\n"
            )

            f_out.write(line)

print("pos.txt generated successfully")
