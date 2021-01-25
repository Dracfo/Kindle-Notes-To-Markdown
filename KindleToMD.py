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

# Try to find an existing markdown notes file to read from
try:
    markdown_notes = open(f"{text_name} Notes.md", "r", encoding='utf-8')
except:  # If none exist, create a new file
    markdown_notes = open(f"{text_name} Notes.md", "a+", encoding='utf-8')

# Iterate through the file to find notes for the book
line_count = 0
note_type = None
note_metadata = ''
notes_list = []
for line in kindle_notes:
    # If we are inside of a note
    if line_count > 0:
        # If this is the metadata line
        if line_count == 3:
            #check if this is a highlight or a note
            if line[7] == 'H':
                note['type'] = 'highlight'
                note['page'] = line[26]
            else:
                note['type'] = 'note'

            # Get the page number
            
        
            # Store the note metadata to print after you get the actual quote
            note_metadata = line

        # If this is the actual highlight/note
        elif line_count == 1:

            # Check if this note already exists in the file
            for note_line in markdown_notes:
                if str(line) in str(note_line):
                    print("-----Duplicate note\n")

            if note['type'] == 'highlight':
                note['Highlight'] = f'> {line}>{note_metadata}\n'
            else:
                note['Highlight'] = f'{line}{note_metadata}\n'

            # Add the note to the note_list
            notes_list.append(note)
            
        # Subtract 1 from the line count
        line_count -= 1

    elif text_name in line: # If you find the book name in the notes file
        line_count = 3
        note = {}

# Close the kindle notes file
kindle_notes.close()
print(notes_list)


# Write formatted ntoes to a new file
try:  # Create a notes markdown file to write to
    markdown_notes = open(f"{text_name} Notes.md", "x", encoding='utf-8')
except:  # If a file already exists, open it and apend to it
    markdown_notes = open(f"{text_name} Notes.md", "a", encoding='utf-8')


# markdown_notes.write(f'> {line}>{note_metadata}\n')
# markdown_notes.write(f'{line}{note_metadata}\n')