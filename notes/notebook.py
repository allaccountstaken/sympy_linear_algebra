import datetime
# Store the next available id for all new notes
last_id = 0

class Note:
    """Represents a note in the notebook. Match against a string in searches and stores 
    tags for each note"""
    def __init__(self, memo, tags=""):
        """Initialize a note with memo and optional space-separated tags. Automatically set a note's
        creating date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, target):
        """Determine if this note matches the filter text. Return True if matches, False otherwise.
        Search is case sensitive and matches both text and tags."""
        return target in self.memo or target in self.tags

class Notebook:
    """Represnets a collection of notes that can be tagged, modified, and searched."""
    def __init__(self):
        """Initializes a notebook as an empty list of notes."""
        self.notes = []
        
    def new_note(self, memo, tags=""):
        """Creates a new note and add it to the list."""
        self.notes.append(Note(memo, tags))
    
    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
                
    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its tags to the given value."""
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
                
    def search(self, target):
        """Find all notes that match teh given target (filter) string"""
        return [note for note in self.notes if note.match(target)]
    
    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
