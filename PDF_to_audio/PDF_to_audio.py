import pyttsx3
import PyPDF2

language = 'ru'

pdf_speaker = pyttsx3.init()

pdf_book = open('Доверенность.pdf', 'rb')
reading_pdf = PyPDF2.PdfFileReader(pdf_book)
text = ""
for page_number in range(reading_pdf.numPages):
    text += reading_pdf.getPage(page_number).extract_text()
    pdf_speaker.say(text)
    pdf_speaker.runAndWait()
    print(page_number)
pdf_speaker.stop()

pdf_speaker.save_to_file(text, 'Доверенность.mp3')
pdf_speaker.runAndWait()


print('конец')

print(input('Напишите новый файл '))
