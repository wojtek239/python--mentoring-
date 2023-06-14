import datetime


class Note:
    def __init__(self, author_: str, content_: str):
        self.author = author_
        self.content = content_
        self.creation_time = datetime.datetime.now()


class Notepad:
    def __init__(self):
        self.notes = []

    def add_note(self, note_: str):
        self.notes.append(note_)

    def add_existing_note(self, author_: str, content_: str):
        note = Note(author_, content_)
        self.notes.append(note)

    def notes_number(self):
        return len(self.notes)

    def show_notes(self):
        if self.notes_number() == 0:    # czy tutaj walrus ?
            print("notepad is empty")
        else:
            for i, note in enumerate(self.notes):
                print(f'Note {i}:')
                print(f'Author: {note.author}')
                print(f'Content: {note.content}')
                print(f'Creation time: {note.creation_time}')

notepad = Notepad()

note1 = Note("Wojtek", "blablabla")
notepad.add_note(note1)

notepad.add_existing_note("Adam", "abcdefghijkl")

print("notes number:", notepad.notes_number())

notepad.show_notes()