from transformers import pipeline
import argparse

def textSummary(text):
  summarization = pipeline("summarization")
  original_text = text
  summaryText = summarization(original_text)[0]['summary_text']
  print("Summary:", summaryText)

if _name_ == "_main_":
    parser = argparse.ArgumentParser()
    parser.add_argument("text",type = str)

    args = parser.parse_args()
    textSummary(args.text)
