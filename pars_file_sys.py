import os
import shutil
import argparse


def copy_and_sort(source_dir, destination_dir):
    try:
        os.makedirs(destination_dir, exist_ok=True)
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                extension = file.split(".")[-1]
                destination_subdir = os.path.join(destination_dir, extension)

                # Create a subdirectory for the extension if it doesn't exist
                os.makedirs(destination_subdir, exist_ok=True)

                # Copy the file to the corresponding subdirectory
                shutil.copy(file_path, os.path.join(destination_subdir, file))

            for subdir in dirs:
                # Check if the element is a directory
                subdirectory_path = os.path.join(root, subdir)
                if os.path.isdir(subdirectory_path):
                    # Call the function recursively for the subdirectory
                    copy_and_sort(subdirectory_path, destination_dir)

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Copy and sort files based on their extensions."
    )
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument(
        "destination_dir",
        nargs="?",
        default="dist",
        help="Path to the destination directory (default: dist)",
    )

    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    copy_and_sort(source_dir, destination_dir)


if __name__ == "__main__":
    main()
