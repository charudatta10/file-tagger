import argparse
from src.file_tag import FileTag

def main():
    # Create an instance of FileTag
    t = FileTag()
    
    # Load the file containing tags
    t.load_file()
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="File tagger")
    parser.add_argument('command', choices=['add', 'remove'], help='Command to run')
    parser.add_argument('filename', help='Name of the file to tag')
    parser.add_argument('tags', nargs='+', help='Tags to add or remove')
    args = parser.parse_args()
    
    if args.command == 'add':
        # Add tags to the specified file
        t.add_tags(args.filename, args.tags)
    elif args.command == 'remove':
        # Remove tags from the specified file
        for tag in args.tags:
            t.remove_tag(args.filename, tag)
    
    # Save the file with updated tags
    t.save_file()



if __name__ == "__main__":
    main()
