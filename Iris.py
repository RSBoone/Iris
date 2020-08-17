# I will need to make a lot of these if statements into Loops...

import os
import spacy
import speech_recognition as sr

from gtts import gTTS

nlp = spacy.load('en_core_web_lg')

os.chdir('C:\\Users\\rboon\\Desktop')

response = ''  # Empty response string


# Recording speech and returning a string.
def record_audio():
    # Recording thee audio
    r = sr.Recognizer()

    # Assigning mic to 'm'
    m = sr.Microphone()

    with m as source:
        r.pause_threshold = 1
        print('!')
        audio = r.listen(source)

    # Speech recognition using Google's Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
    except sr.RequestError as e:
        print('Request error from Google Speech Recognition')

    return data


# Function to get the virtual assistant response
def assistant_response(response_text):
    print(response_text)

    # Convert the text to speech
    myobj = gTTS(text=response_text, lang='en', slow=False)

    # Save the converted audio to a file
    myobj.save('assistant_response.mp3')

    # Play the converted file
    os.system('start assistant_response.mp3')


# A function to check for wake word
def wake_word(text):
    name = 'Iris'
    passed_input = text.lower()  # Convert the text to all lower case wordsd

    # Check to see if the user command/text contains a wake word
    for phrase in name:
        if phrase in passed_input:
            return True

    # If the wake word was not found return false
    return False


# Function for recognizing intent
def get_intent(input):

    spoken_text = input
    # Extracting Intent
    verb = ''
    dir_obj = ''

    for token in spoken_text:
        if token.dep_ == 'dobj':
            verb = token.head.text
            dir_obj = token.text.capitalize()

    intention = verb + dir_obj
    if intention == '':
        assistant_response('Come again?')
        get_intent(input)

    if intention == 'makeRepository':
        print(intent)
    create_repository(spoken_text)

    if intention == 'makeNote':
        print('makeNote')
        create_note(spoken_text)

    if intention == 'readNote':
        print('readNote')
        read_note(spoken_text)

    if intention == 'deleteNote':
        print('deleteNote')
        delete_note(spoken_text)

    if intention == 'editNote':
        print('editNote')
        edit_note(spoken_text)

    return True


# Function for creating a data repository.
def create_repository():
    assistant_response('What do you want it to be called?')
    print('!')
    repo_title = record_audio()
    if repo_title != '':
        globals()[repo_title] = {}
        assistant_response('Alright, ' + repo_title + '  it is.')
    else:
        assistant_response("I didn't hear that. What do you want it to be called?")
        print('!')
        repo_title = record_audio()
        if repo_title == '':
            assistant_response("Maybe later then.")
            pass
    return repo_title


# Function for creating a note
def create_note(spoken_text, notes):
    # Check for Title and Content
    # Loop through each token and check for an acl
    # (Adjectival Clause (AC): Indicating a title),
    # relcl (Relative Clause (RC): Indicating Content), and the period.
    for token in spoken_text:
        # Checking for the existence of an AC and RC
        if token.dep_ == 'acl':
            adj_cl = token.i
            ntsp = adj_cl + 1
        else:
            adj_cl = 0

        if token.dep_ == 'relcl':
            rel_cl = token.i
            ntep = token.i - 1
            nb = token.i + 1
        else:
            rel_cl = 0

        if token.text =='.':
            ne = token.text

    # 1) Title and Note.
    if adj_cl != 0 and rel_cl != 0:
        note_title = spoken_text[ntsp: ntep].text
        note_content = spoken_text[nb].text.capitalize() + ' ' + spoken_text[nb + 1:ne].text
        notes[note_title] = note_content
        assistant_response('I have created your note.')

    # 2) Title but no note.
    if adj_cl != 0 and rel_cl == 0;
        note_title = spoken_text[ntsp: ne].text
        note_content = ''
        assistant_response('I have created a note called ' + note_title + '. What do you want it to say?')
        note_content = record_audio()
        notes[note_title] = note_content


    # 3) Note, but no title.
    if adjCl == 0 and relCl != 0:
        note_title = ''
        note_content = spoken_text[nb].text.capitalize() + ' ' + spoken_text[nb + 1:ne].text
        assistant_response('What do you want the note to be called?')
        note_title = record_audio()
        assistant_response('I have created ' + note_title + '.')
        notes[note_title] = note_content

    # 4) No title or note.
    if adjCl == 0 and relCl == 0:
        note_title = ''
        note_content = ''
        assistant_response('What do you want the note to be called?')
        note_title = record_audio()
        assistant_response('What do you want it to say?')
        note_content = record_audio()
        notes[note_title] = note_content
        assistant_response('I have created a note ' + note_title + '. It says, ' + note_content + '.')
        # assistant_response('Done.')


# Function for reading a note.
def read_note():
    assistant_response('Which note do you want me to read?')
    note_to_read = record_audio()

    if note_to_read in notes:
        assistant_response(notes[note_to_read])
    else:
        assistant_response('That note does not exist.')

    return


# Function to delete a note.
def delete_note():
    assistant_response('Which note do you want to delete?')
    note_to_delete = record_audio()

    if note_to_delete in notes:
        assistant_response('I will delete that note.')
        notes.pop(note_to_delete)
    else:
        assistant_response('This note does not exist.')

    return


# Function to edit notes.
def edit_note():
    assistant_response('What note should I edit?')
    note_to_edit = record_audio()

    if note_to_edit != '':
        if note_to_edit in notes:
            assistant_response('What do you want the note to say?')
            notes[note_to_edit] = record_audio()
            assistant_response('Your note has been edited.')
        else:
            assistant_response('This note does not exist.')
    else:
        assistant_response('I did not hear you say anything. Come again?')


assistant_response('I am online sir.')

while True:
    # Record the audio
    text = record_audio()
    tokenized_input = nlp(text)

    # Checking for the wake word/phrase
    if wake_word(text):
        intent = get_intent(tokenized_input)
