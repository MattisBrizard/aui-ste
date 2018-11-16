import config

# This is a temporary mapping waiting for the smartlights
def emotion_to_color(emotion):
    if (emotion == 'fear'):
        return config.FEAR_COLOR
    elif (emotion == 'anger'):
        return config.ANGER_COLOR
    elif (emotion == 'joy'):
        return config.JOY_COLOR
    elif (emotion == 'sadness'):
        return config.SADNESS_COLOR