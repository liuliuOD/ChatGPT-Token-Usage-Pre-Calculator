import os
import pandas
import tiktoken
from simple_term_menu import TerminalMenu

from SettingLoader import CONFIG

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

def select_from_terminal(types):
  index = TerminalMenu(types).show()

  selected_type = types[index]
  print(selected_type)

  return selected_type

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
  TYPES = CONFIG['MENU']['CALCULATOR_TYPES']
  print('Which type of tokens calculator you want to use?')
  type = select_from_terminal(TYPES)

  if type == TYPES[0]:
    print('Which model you want to use?')
    MODEL_TYPES = CONFIG['MENU']['MODEL_TYPES']
    type = select_from_terminal(MODEL_TYPES)

    result = process_token_amount_to(rows_from_csv(), type=type, is_model=True)
    
  elif type == TYPES[1]:
    print('Which encoding method you want to use?')
    ENCODING_TYPES = CONFIG['MENU']['ENCODING_TYPES']
    type = select_from_terminal(ENCODING_TYPES)

    result = process_token_amount_to(rows_from_csv(), type=type, is_model=False)

  write_to_csv(result)
