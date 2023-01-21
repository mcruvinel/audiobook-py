from gtts import gTTS
import PyPDF2

# Open the PDF file and read its text
with open('documentname.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    pdf_text = ""
    for page in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page].extract_text()

# Convert the text to speech
tts = gTTS(text=pdf_text, lang='en')

# Save the audio file
tts.save("output.mp3")
print("Audio file saved as output.mp3")
