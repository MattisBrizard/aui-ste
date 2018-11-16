import config
from threading import Thread
import time
from colored import fg, bg, attr
from termcolor import colored
import speech_recognition as sr
from stt import gg_stt
from emotion import emotion_from_text
from translate import translate_to_en
from color_mapping import emotion_to_color


# Function executed by the threads
def emotion_retrieve_process(r, audio):
    # Processing time computation start time
    start = time.time()

    # Google cloud Speech to text function from stt.py
    text = gg_stt(r, audio)
    
    # If no error occured during speech to text
    if (text != '[STT_ERROR]'):

        # Google cloud translation function from translation.py
        translated_text = translate_to_en(text)

        # If no error occured during translation
        if (translated_text != '[TRANSLATION_ERROR]'):

            # IBM Watson Tone Analyzer function from emotion.py
            emotion_id = emotion_from_text(translated_text)

            # If no error occured during emotion analysis
            if (emotion_id != '[EMOTION_ERROR]'):
                    
                # If we found an emotion
                if (emotion_id):

                    # Emotion to color mapping from color_mapping.py (temporary mapping)
                    color = emotion_to_color(emotion_id)

                    # Processing time computation end time
                    print("Process time: " + str(time.time() - start))

                    # Display emotion and associated color
                    print("------------- " + emotion_id + " : " + "%s%s        %s" % (fg('black'), bg(color), attr('reset')))

                else:
                    print("------------- Thread : No emotion found" )
                return True
             
            else:
                print('------------- Thread : Emotion analyzer not working')
                return True
   
        else:
            print('------------- Thread : Translation not working')
            return True

    else:
        print('------------- Thread : Speech to text not working')
        return True


if __name__ == "__main__":
    
    with sr.Microphone() as source:

        # Initialization of the recording process
        r = sr.Recognizer()
        
        # Minimum energy for speech. Noises and words below this level will not be recognised
        r.energy_threshold = config.ENERGY_THRESHOLD
        # Prevent from dynamically change the limit
        r.dynamic_energy_threshold = False 
        # Maximum pause time. After this time the sentence will be parsed.
        r.pause_threshold = config.PAUSE_THRESHOLD
        # Minimum seconds of speaking audio before we consider the speaking audio a phrase
        r.phrase_threshold = config.PHRASE_TRESHOLD

        while True:
            
            print(colored("Say something!",'blue'))

            try:
                # Listen for audio when conditions 
                audio = r.listen(source, timeout=None, phrase_time_limit=10)

                # Audio recorded
                print(colored("Got it! Now it's time to extract emotion...",'blue'))

                # Run a Thread that will execute the emotion extraction function
                t = Thread(target = lambda: emotion_retrieve_process(r, audio))
                t.daemon = True
                t.start()

            except sr.WaitTimeoutError:
                pass
                # print (colored('*** WAIT TIMEOUT ERROR ***', 'blue'))
            
            # Ctrl + c to exit the program
            except KeyboardInterrupt:
                break

            except:
                print (colored('*** MAIN ERROR ***', 'blue'))