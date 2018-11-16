import config
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException

## IBM Watson Tone Analyzer credentials (delete the unuseful one)

# For the Identity and Access Management (IAM) authentication
# tone_analyzer = ToneAnalyzerV3(
#     version=config.EMOTION_VERSION,
#     iam_apikey=config.EMOTION_API_KEY,
#     url=config.EMOTION_API_URL
# )

# For the basic authentication
tone_analyzer = ToneAnalyzerV3(
    version=config.EMOTION_VERSION,
    username=config.EMOTION_API_USERNAME,
    password=config.EMOTION_API_PASSWORD,
    url=config.EMOTION_API_URL
)

# Emotions that can be found by Watson :
# - anger
# - fear
# - joy
# - sadness

available_emotions = ['anger', 'fear', 'joy', 'sadness']

def emotion_from_text(text):
    try:
        tone_analysis = tone_analyzer.tone(
            {'text': text},
            'application/json',
        ).get_result()

        emotion_id = main_emotion(tone_analysis["document_tone"]["tones"])
        return emotion_id

    # except WatsonApiException as ex:
    #     print("Method failed with status code " + str(ex.code) + ": " + ex.message)

    except:
        print("------------- *** ERROR : Unable to retrieve emotion ***")
        return '[EMOTION_ERROR]'

# Return the main emotion from the text based on the highest score ('' if not found)
def main_emotion(emotions):
    score = 0.0
    main_emotion_id = ''

    for emotion in emotions:
            if emotion['tone_id'] in available_emotions:
                if emotion['score'] > score:
                    score = emotion['score']
                    main_emotion_id = emotion['tone_id']
    return main_emotion_id