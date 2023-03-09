import pandas
import tiktoken
from simple_term_menu import TerminalMenu

"""
Document: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
"""

def encode(encoding, prompt):
  encode_tokens = encoding.encode(prompt)

  return len(encode_tokens)

def completion_for_encoding(encoding_method, prompt):
  encoding = tiktoken.get_encoding(encoding_method)

  return encode(encoding, prompt)

def completion_for_model(model, prompt):
  encoding = tiktoken.encoding_for_model(model)

  return encode(encoding, prompt)

def calculate_from_csv():
  path = input('Input your CSV file path:') or 'demo.csv'
  df = pandas.read_csv(path)
  return df.iterrows()

def write_to_csv(result):
  pandas.DataFrame(data=result).to_csv('demo_result.csv')

if __name__ == '__main__':
  types = ['1. model', '2. encoding']
  print('Which type of tokens calculator you want to use?')
  type_index = TerminalMenu(types).show()
  result = {'Prompt': [], 'Amount Of Tokens': []}

  print(types[type_index])

  prompt = 'This is an apple. That is a banana.'

  if type_index == 0:
    print('Which model you want to use?')
    model_types = [
      'gpt-3.5-turbo-0301',
      'gpt-3.5-turbo',
      'text-davinci-003',
      'text-davinci-002',
      'text-davinci-001',
      'davinci-instruct-beta',
      'davinci',
      'text-curie-001',
      'curie-instruct-beta',
      'curie',
      'text-babbage-001',
      'babbage',
      'text-embedding-ada-002',
      'text-ada-001',
      'ada',
      'code-davinci-002',
      'code-cushman-001'
    ]

    type_index = TerminalMenu(model_types).show()

    print(model_types[type_index])

    for index, row in calculate_from_csv():
      result['Prompt'].append(row['Prompt'])
      result['Amount Of Tokens'].append(completion_for_model(model_types[type_index], row['Prompt']))
    
  elif type_index == 1:
    print('Which encoding method you want to use?')
    encoding_types = ['cl100k_base', 'p50k_base', 'r50k_base', 'gpt2']
    type_index = TerminalMenu(encoding_types).show()

    print(encoding_types[type_index])

    for index, row in calculate_from_csv():
      result['Prompt'].append(row['Prompt'])
      result['Amount Of Tokens'].append(completion_for_encoding(encoding_types[type_index], row['Prompt']))

  write_to_csv(result)

