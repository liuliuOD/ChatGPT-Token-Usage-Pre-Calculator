# ChatGPT CSV Prompt Token Calculator

This tool is designed to quickly and accurately calculate the token amounts in prompts using CSV structure files. By analyzing the CSV files, this tool can provide a precise token count, saving you time and improving accuracy.

## Installation

To use this tool, you will need to install the following dependencies:

- Python 3

## Support models and encoding methods:

- models

  > - gpt-3.5-turbo-0301
  > - gpt-3.5-turbo
  > - text-davinci-003
  > - text-davinci-002
  > - text-davinci-001
  > - davinci-instruct-beta
  > - davinci
  > - text-curie-001
  > - curie-instruct-beta
  > - curie
  > - text-babbage-001
  > - babbage
  > - text-embedding-ada-002
  > - text-ada-001
  > - ada
  > - code-davinci-002
  > - code-cushman-001

- encoding methods

  > - cl100k_base
  > - p50k_base
  > - r50k_base
  > - gpt2

## Usage:

### Docker:
> Just in 1 step.
1. Run in docker. *Don't forget to mount your csv file folder into container.*
```bash
$ docker run --rm -itv ${PWD}:/app dockliu/chatgpt-token-calculator:latest
```

### Download project:
> Just in 5 steps.

1. Run in virtual environment.
```bash
$ poetry install
$ poetry shell
```

2. Execute tool of this calculator.
```bash
$ python3 main.py
```

3. Choose which type want to use.
   <br>
   ![type](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/type.png)

4. Depending on the previous selection, choose which model or encoding method you want to use.
   <br>
   ![model](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/model.png)

5. Type the CSV file path you want to calculate then press 'ENTER'. The data format can refer to [the following link](https://docs.google.com/spreadsheets/d/13JRhLYTo0JahoCw-U2Q46GoFuZT9Fnjq4lYiKvKzKE8/edit?usp=sharing).
   <br>
   ![filepath](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/filepath.png)

## Actual:

- set up environment
  <br>
  ![set up environment](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/setup_environment.gif)
- demo
  <br>
  ![demo](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/demo.gif)
- demo result csv
  <br>
  ![demo result](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/demo_result.png)

## Contributing

If you encounter any issues or have suggestions for how to improve this tool, please submit an issue or pull request. We welcome contributions from the community and appreciate your feedback.
