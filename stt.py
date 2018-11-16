import config

def gg_stt(r, audio):
    try:
        # Google cloud STT service
        transcript = r.recognize_google(audio, language=config.SPEECH_LANG)
        return transcript

    # except sr.RequestError:
    #     # API was unreachable or unresponsive
    #     print("------------- *** ERROR : API unavailable ***")
    #     return '[STT_ERROR]'

    # except sr.UnknownValueError:
    #     # Speech was unintelligible
    #     print("------------- *** ERROR : Unable to recognize speech ***")
    #     return '[STT_ERROR]'
    
    except:
        print("------------- *** ERROR : Unable to recognize speech ***")
        return '[STT_ERROR]'