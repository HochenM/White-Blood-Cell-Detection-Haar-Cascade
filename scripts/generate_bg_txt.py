import os

NEG_FOLDER = "data/neg"

with open("bg.txt", "w") as f:

    for filename in os.listdir(NEG_FOLDER):

        path = os.path.join(
            NEG_FOLDER,
            filename
        )

        f.write(path + "\n")

print("bg.txt generated successfully")
