import os
import json
import argparse
import sys

class FileTag:

    def __init__(self) -> None:
        self.file_tags = {}

    def load_file(self, tags_file='file_tags.json'):
        if os.path.exists(tags_file):
            with open(tags_file, 'r') as f:
                self.file_tags = json.load(f)

    def save_file(self, tags_file='file_tags.json'):
        with open(tags_file, 'w') as f:
            json.dump(self.file_tags, f, indent=4)

    def add_tags(self, file_path: str, tags) -> None:
        if isinstance(tags, str):
            tags = [tags]
        
        if file_path in self.file_tags:
            self.file_tags[file_path] = list(set(self.file_tags[file_path] + tags))
        else:
            self.file_tags[file_path] = tags

    def show_tags(self) -> None:
        if not self.file_tags:
            print("No tags found.")
            return
        max_file_len = max(len(file_path) for file_path in self.file_tags)
        max_tag_len = max((len(', '.join(tags)) for tags in self.file_tags.values()), default=0)
        header = f"{'File Path'.ljust(max_file_len)} | {'Tags'.ljust(max_tag_len)}"
        print(header)
        print('-' * len(header))
        for file_path, tags in self.file_tags.items():
            print(f"{file_path.ljust(max_file_len)} | {', '.join(tags).ljust(max_tag_len)}")

    def remove_tag(self, file_path: str, tag: str) -> None:
        if file_path in self.file_tags and tag in self.file_tags[file_path]:
            self.file_tags[file_path].remove(tag)
            if not self.file_tags[file_path]:
                del self.file_tags[file_path]

    def sort_tags(self):
        sorted_files = sorted(self.file_tags.items(), key=lambda item: item[1][0] if item[1] else '')
        for file_path, tags in sorted_files:
            print(f"{file_path}: {', '.join(tags)}")

def main():
    parser = argparse.ArgumentParser(description="File Tagger CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add tags
    add_parser = subparsers.add_parser("add", help="Add tags to a file")
    add_parser.add_argument("file", help="File path")
    add_parser.add_argument("tags", nargs="+", help="Tags to add")

    # Remove tag
    remove_parser = subparsers.add_parser("remove", help="Remove a tag from a file")
    remove_parser.add_argument("file", help="File path")
    remove_parser.add_argument("tag", help="Tag to remove")

    # Show tags
    show_parser = subparsers.add_parser("show", help="Show all file tags")

    # Sort tags
    sort_parser = subparsers.add_parser("sort", help="Show all file tags sorted by first tag")

    parser.add_argument("--tags-file", default="file_tags.json", help="Path to tags file (default: file_tags.json)")

    args = parser.parse_args()

    t = FileTag()
    t.load_file(args.tags_file)

    if args.command == "add":
        t.add_tags(args.file, args.tags)
        t.save_file(args.tags_file)
    elif args.command == "remove":
        t.remove_tag(args.file, args.tag)
        t.save_file(args.tags_file)
    elif args.command == "show":
        t.show_tags()
    elif args.command == "sort":
        t.sort_tags()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()

