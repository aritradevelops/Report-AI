from utils import task,ai,cover,md_to_html,html_to_doc
import os
def generate_pdfs():
  print("Reading tasks.json...")
  data = task.parse('task.json')
  print("tasks found: %s" % len(data))
  for i in range(len(data)):
    t = data[i]
    topic = t['topic']
    gap = t['gap']
    del t['topic']
    del t['gap']
    print("Generating report for topic %s..." % topic)
  filepath = f"./cache/{t['Subject Code']}.md"
  if os.path.exists(filepath):
    print("Reading cached markdown content...")
    # Read the content of the file and set it to res
    with open(filepath, 'r', encoding='utf-8') as file:
      res = file.read()
  else:
    print("Generating markdown content from AI...")
    res = ai.prompt(f'Please generate a long report for topic {topic} in context of {t['Subject']}' )
    with open(filepath, 'w', encoding='utf-8') as file:
      file.write(res)
  print(f'Generating cover for labels: %s' % ', '.join([f'{key}: {value}' for key, value in t.items()]))
  doc = cover.generate_doc_with_intro(topic,t, gap)
  doc.add_page_break()
  print("Converting ai provided data to docs format...")
  html = md_to_html.convert(res)
  html_to_doc.convert_and_add(html,doc)
  doc.save(f'./docs/{t['Name']}_CA2.docx')
  print("Doc File generated successfully for task %s" % (i+1))

if(__name__ == '__main__'):
  generate_pdfs()