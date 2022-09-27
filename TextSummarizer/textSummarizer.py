from transformers import pipeline
import argparse

def textSummarizer(text):
  summarization = pipeline("summarization")
  original_text = text
  summary_text = summarization(original_text)[0]['summary_text']
  print("Summary:", summary_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text",type = str)

    args = parser.parse_args()
    textSummarizer(args.text)
