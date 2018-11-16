from py_translator import Translator


def translate_to_en(text):
    
    try : 
        # Google cloud translation service
        translated_text = Translator().translate(text=text, dest='en').text
        return translated_text

    except:
        print("------------- *** ERROR : Unable to translate text ***")
        return '[TRANSLATION_ERROR]'
