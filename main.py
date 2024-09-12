import os
from utils import task, ai, cover, md_to_html, html_to_doc,doc_to_pdf
from colorama import init, Fore, Style
from docx2pdf import convert as docx_to_pdf

# Initialize colorama for colored logs
init(autoreset=True)

def read_tasks(file_path):
    """Read and parse the tasks from the specified JSON file."""
    print(f"{Fore.CYAN}Reading {file_path}...")
    data = task.parse(file_path)
    print(f"{Fore.GREEN}Tasks found: {len(data)}")
    return data

def generate_report(t, topic, gap, cache_dir):
    """Generate or fetch the report for the given task."""
    filepath = os.path.join(cache_dir, f"{t['Subject Code']}.md")

    if os.path.exists(filepath):
        print(f"{Fore.YELLOW}Reading cached markdown content for {t['Subject']}...")
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        print(f"{Fore.BLUE}Generating markdown content from AI for {topic} in {t['Subject']}...")
        res = ai.prompt(f'Please generate a long report for topic {topic} in context of {t["Subject"]}')
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(res)
        return res

def generate_cover_doc(topic, t, gap):
    """Generate the cover page for the report."""
    print(f"{Fore.MAGENTA}Generating cover for labels:\n{', '.join([f'{key}: {value}' for key, value in t.items()])}")
    doc = cover.generate_doc_with_intro(topic, t, gap)
    doc.add_page_break()
    return doc

def convert_to_doc(res, doc):
    """Convert AI-provided markdown content to docx format."""
    print(f"{Fore.CYAN}Converting AI-provided data to docx format...")
    html = md_to_html.convert(res)
    html_to_doc.convert_and_add(html, doc)

def save_doc(doc, doc_dir, t):
    """Save the generated docx to the specified directory."""
    output_file = os.path.join(doc_dir, f"{t['Subject']}_{t['Name']}.docx")
    doc.save(output_file)
    print(f"{Fore.GREEN}Doc File generated successfully for {t['Name']}\n\n")

def process_task(t, cache_dir, doc_dir):
    """Process a single task to generate the report."""
    topic = t['topic']
    gap = t.get('gap', 5)
    
    # Clean up unnecessary fields
    del t['topic']
    t.pop('gap', None)

    print(f"{Fore.BLUE}{Style.BRIGHT}Generating report for topic: {topic}...")
    
    # Generate or fetch report content
    res = generate_report(t, topic, gap, cache_dir)
    
    # Generate the cover page
    doc = generate_cover_doc(topic, t, gap)
    
    # Convert markdown content to docx format
    convert_to_doc(res, doc)
    
    # Save the generated doc
    save_doc(doc, doc_dir, t)

def generate_pdfs(task_file='task.json', cache_dir='./cache', doc_dir='./docs'):
    """Main function to generate PDFs for all tasks."""
    tasks = read_tasks(task_file)
    
    for i, t in enumerate(tasks):
        print(f"{Fore.YELLOW}Processing task {i+1}/{len(tasks)}...")
        process_task(t, cache_dir, doc_dir)



if __name__ == '__main__':
    generate_pdfs()
    doc_to_pdf.convert_docs_to_pdfs()
