from htmldocx import HtmlToDocx

parser = HtmlToDocx()
def convert_and_add(html,doc):
  return parser.add_html_to_document(html,doc)