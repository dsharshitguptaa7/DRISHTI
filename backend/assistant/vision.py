import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from detector import detect_objects, summarize_objects
from speech import speak

def run_vision():

    objects = detect_objects("test.jpeg")

    summary = summarize_objects(objects)

    speak(summary)

    return summary