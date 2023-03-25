# ChatGPT CSV Prompt Token Calculator

This tool is designed to quickly and accurately calculate the token amounts in prompts using CSV structure files. By analyzing the CSV files, this tool can provide a precise token count, saving you time and improving accuracy.

## Installation

To use this tool, you will need to install the following dependencies:

- Python 3
- Docker (only if you run by [Docker](https://www.docker.com) version of [this tool](https://hub.docker.com/r/dockliu/chatgpt-token-calculator))

## Support models and encoding methods

| Models | Encoding Methods |
| :- | :- |
| gpt-3.5-turbo-0301 | cl100k_base
| gpt-3.5-turbo | p50k_base
| text-davinci-003 | r50k_base
| text-davinci-002 | gpt2
| text-davinci-001 |
| davinci-instruct-beta |
| davinci |
| text-curie-001 |
| curie-instruct-beta |
| curie |
| text-babbage-001 |
| babbage |
| text-embedding-ada-002 |
| text-ada-001 |
| ada |
| code-davinci-002 |
| code-cushman-001 |

## Docker usage

> Just in 1 step.

1. Run the [Docker](https://www.docker.com) image on [this repository of Docker hub](https://hub.docker.com/r/dockliu/chatgpt-token-calculator). _Don't forget to mount your csv file folder into container._

```bash
$ docker run --rm -itv ${PWD}:/app_temp dockliu/chatgpt-token-calculator:latest
```

## Command-line usage

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

## Actual execution

- set up environment
  <br>
  ![set up environment](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/setup_environment.gif)
- demo
  <br>
  ![demo](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/demo.gif)
- demo result csv. The data format can refer to [the following link](https://docs.google.com/spreadsheets/d/1OPRv5q2yWLO2i4EsHTaK3SyxQjMqq8QguD9MERBv_Rk/edit?usp=sharing).
  <br>
  ![demo result](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/demo_result.png)

## Contributing

If you encounter any issues or have suggestions for how to improve this tool, please submit an issue or pull request. We welcome contributions from the community and appreciate your feedback.
