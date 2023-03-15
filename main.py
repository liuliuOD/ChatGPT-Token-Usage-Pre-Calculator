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

def csv_to_dataframe():
  path = input('Input your CSV file path:') or 'demo.csv'
  if not (os.path.exists(path) and os.path.isfile(path)):
    raise Exception('Filepath not exists.')

  return pandas.read_csv(path)

def dataframe_to_token_amounts(dataframe, type, is_model = False):
  columns = dataframe.columns.tolist()
  result = {}
  for col in columns:
    if not result.get(col):
      result[col] = []

  for _, row in dataframe.iterrows():
    for col in columns:
      value = str(row[col])

      if len(value) == 0:
        continue

      result[col].append(value)

      amount_of_value = '[{}] token amount'.format(col)

      if not result.get(amount_of_value):
        result[amount_of_value] = []

      if is_model:
        result[amount_of_value].append(completion_for_model(type, value))
      else:
        result[amount_of_value].append(completion_for_encoding(type, value))

  return result

def dictionary_to_csv(result):
  pandas.DataFrame(data=result).to_csv('demo_result.csv')

if __name__ == '__main__':
  TYPES = CONFIG['MENU']['CALCULATOR_TYPES']
  print('Which type of tokens calculator you want to use?')
  type = select_from_terminal(TYPES)

  if type == TYPES[0]:
    print('Which model you want to use?')
    MODEL_TYPES = CONFIG['MENU']['MODEL_TYPES']
    type = select_from_terminal(MODEL_TYPES)

    result = dataframe_to_token_amounts(csv_to_dataframe(), type=type, is_model=True)
    
  elif type == TYPES[1]:
    print('Which encoding method you want to use?')
    ENCODING_TYPES = CONFIG['MENU']['ENCODING_TYPES']
    type = select_from_terminal(ENCODING_TYPES)

    result = dataframe_to_token_amounts(csv_to_dataframe(), type=type, is_model=False)

  dictionary_to_csv(result)
