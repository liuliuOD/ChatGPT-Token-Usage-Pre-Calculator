import os
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

def rows_from_csv():
  path = input('Input your CSV file path:') or 'demo.csv'
  if not (os.path.exists(path) and os.path.isfile(path)):
    raise Exception('Filepath not exists.')

  df = pandas.read_csv(path)
  return df.iterrows()

def process_token_amount_to(rows, type, is_model = False):
  result = {'Prompt': [], 'Amount Of Tokens': []}
  for _, row in rows:
    prompt = str(row['Prompt'])

    if len(prompt) == 0:
      continue

    result['Prompt'].append(prompt)

    if is_model:
      result['Amount Of Tokens'].append(completion_for_model(type, prompt))
    else:
      result['Amount Of Tokens'].append(completion_for_encoding(type, prompt))

  return result

def write_to_csv(result):
  pandas.DataFrame(data=result).to_csv('demo_result.csv')

if __name__ == '__main__':
  types = ['1. model', '2. encoding']
  print('Which type of tokens calculator you want to use?')
  type_index = TerminalMenu(types).show()

  print(types[type_index])

  prompt = 'This is an apple. That is a banana.'

  if type_index == 0:
    print('Which model you want to use?')
    MODEL_TYPES = [
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

    type_index = TerminalMenu(MODEL_TYPES).show()

    print(MODEL_TYPES[type_index])

    result = process_token_amount_to(rows_from_csv(), type=MODEL_TYPES[type_index], is_model=True)
    
  elif type_index == 1:
    print('Which encoding method you want to use?')
    ENCODING_TYPES = ['cl100k_base', 'p50k_base', 'r50k_base', 'gpt2']
    type_index = TerminalMenu(ENCODING_TYPES).show()

    print(ENCODING_TYPES[type_index])

    result = process_token_amount_to(rows_from_csv(), type=ENCODING_TYPES[type_index], is_model=False)

  write_to_csv(result)
