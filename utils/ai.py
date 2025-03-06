import ollama

def prompt(text, model="llama3.2"):
  res = ollama.chat(model, messages=[
    {
      'role': 'user',
      'content': text,
    },
  ])
  return res['message']['content']