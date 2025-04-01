import os

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}
IMAGE_DIR = "fractals"
README_FILE = "README.md"
MARKER = "<!-- IMAGES -->"

def generate_readme():
    existing_content = []
    has_marker = False

    if os.path.exists(README_FILE):
        with open(README_FILE, "r") as f:
            for line in f:
                existing_content.append(line)
                if MARKER in line:
                    has_marker = True
                    break

    if not has_marker:
        print(f"marker '{MARKER}' not found in {README_FILE}")
        return

    images = [f for f in sorted(os.listdir(IMAGE_DIR)) if os.path.splitext(f)[1].lower() in IMAGE_EXTENSIONS]

    if not images:
        print("no image found")
        return

    image_section = "\n".join(f"![{img}](./{IMAGE_DIR}/{img})" for img in images)

    with open(README_FILE, "w") as f:
        f.writelines(existing_content)
        f.write("\n" + image_section + "\n")

    print(f"{README_FILE} updated successfully")

if __name__ == "__main__":
    generate_readme()
