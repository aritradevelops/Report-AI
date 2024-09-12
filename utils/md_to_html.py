from markdown2 import Markdown

client = Markdown()
def convert(md_text):
  return client.convert(md_text)