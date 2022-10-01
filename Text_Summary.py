import argparse
from transformers import pipeline

def textSummary(info):
  summarize = pipeline("summarization")
  original_text = info
  summary = summarize(info)[0]['summary_text']
  print("Summary:", summary)

if _name_ == "_main_":
    parser = argparse.ArgumentParser()
    parser.add_argument("text",type = str)
    argument = parser.parse_args()
    textSummary(argument.text)
