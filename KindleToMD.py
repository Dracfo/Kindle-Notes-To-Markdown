# Import libraries
from sys import argv

# Establish Global Variables - Change these if your device uses a syntax
notes_file_name = 'My Clippings.txt'


# Check if the usage is right 'python KindleToMD.py {TITLE OF BOOK}', else exit with error message
if len(argv) < 2:
    print("\nERROR: No Book Title Entered. \nUsage: 'python KindleToMD.py {TITLE OF BOOK}'\n")
    exit()

# Create a string from the system varibales
text_name = " ".join(argv[1:])

# Check if there is a notes file, if yes open it, if no print error and exit
try:
    kindle_notes = open(notes_file_name, "r", encoding='utf-8')
except FileNotFoundError:
    print("\nNotes file not accessible.\n - Is it in the same folder as the python program?\n - Is the file named 'My Clippings.txt'?\n")
    exit()

# Create a notes markdown file to write to
try:
    markdown_notes = open(f"{text_name} Notes.md", "x", encoding='utf-8')
except:
    markdown_notes = open(f"{text_name} Notes.md", "a", encoding='utf-8')

# Iterate through the file to find notes for the book
line_count = 0
note_type = None
for line in kindle_notes:
    # If we are inside of a note
    if line_count > 0:
        # If this is the meta data line
        if line_count == 3:
            #check if this is a highlight or a note
            if line[7] == 'H':
                note_type = 'highlight'
            else:
                note_type = 'note'

        # If this is the actual highlight/note
        elif line_count == 1:
            if note_type == 'highlight':
                markdown_notes.write(f'Highlight: {line}')
                print(f'Highlight: {line}')
            else:
                markdown_notes.write(f'- Note: {line}')
                print(f'- Note: {line}')
            
        # Subtract 1 from the line count
        line_count -= 1

    elif text_name in line: # If you find the book name in the notes file
        line_count = 3



# Close the kindle notes file
kindle_notes.close()