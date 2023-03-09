# ChatGPT Token Calculator

## This is a tool that pre-calculates the amount of tokens you will consume before using ChatGPT.

---

### Support models and encoding methods:

- models

  > - davinci
  > - text-davinci-002
  > - text-davinci-003
  > - text-embedding-ada-002

- encoding methods

  > - cl100k_base
  > - p50k_base
  > - r50k_base
  > - gpt2

---

### Run in terminal:

```bash
$ poetry install
$ poetry shell
$ python3 main.py
```

---

### How to use:

> Just 3 steps.

1. Choose which type want to use.
   <br>
   ![type](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/type.png)
2. Depending on the previous selection, choose which model or encoding method you want to use.
   <br>
   ![model](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/model.png)
3. Type the CSV file path you want to calculate then press 'ENTER'. The data format can refer to [the following link](https://docs.google.com/spreadsheets/d/13JRhLYTo0JahoCw-U2Q46GoFuZT9Fnjq4lYiKvKzKE8/edit?usp=sharing).
   <br>
   ![filepath](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/filepath.png)

---

### Output:

## ![demo result](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/demo_result.png)

### Actual:

- set up environment
  <br>
  ![set up environment](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/setup_environment.gif)
- demo
  <br>
  ![demo](https://github.com/liuliuOD/chatgpt-token-calculator/blob/master/readme/demo.gif)
