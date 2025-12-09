import argparse

parser = argparse.ArgumentParser(description="Anti-awkwardness bot for chat screenshots")

# Accept one or more image paths
parser.add_argument(
    "images",
    nargs="+",    # <-- IMPORTANT: allows multiple images
    help="Paths to one or more image files"
)

args = parser.parse_args()

# args.images is now a list of file paths
print("Images received:", args.images)
