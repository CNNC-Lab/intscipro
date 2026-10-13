# Part 0 exercises: answer notes

**0.1** Commands differ by system: `pwd`/`cd` (current folder), `ls`/`dir`, `cd`, `mkdir`, `which python`/`where python`. The `.py` files in `setup/` are `hello.py`, `check_python.py` and `broken_1.py` to `broken_4.py` (six in total).

**0.2** The environment is active when its name appears in brackets at the start of the prompt. In the interactive prompt, plain `python` shows `>>>`, while `ipython` shows numbered `In [1]:` prompts, colours, tab completion and history. Running `python hello.py` from the course folder fails with `can't open file ... No such file or directory`: Python looks in the *current* folder, and `hello.py` lives in `day02-fundamentals/setup`. The fix is `cd day02-fundamentals/setup` first (or giving the full path).

**0.3**
| Script | Error | Cause and fix |
|---|---|---|
| `broken_1.py` | `SyntaxError: expected ':'` | missing colon after `if temperature > 20` ([`exercise_0_3_fixed_1.py`](exercise_0_3_fixed_1.py)) |
| `broken_2.py` | `NameError: name 'neuron_cont' is not defined` | misspelled variable, should be `neuron_count` ([`exercise_0_3_fixed_2.py`](exercise_0_3_fixed_2.py)) |
| `broken_3.py` | `ModuleNotFoundError: No module named 'mathh'` | the module is called `math` ([`exercise_0_3_fixed_3.py`](exercise_0_3_fixed_3.py)) |
| `broken_4.py` | `FileNotFoundError: ... 'recording_notes.txt'` | the code is correct; run it from the folder that contains the file (`cd day02-fundamentals/setup`), or give the full path |

Point out that `ModuleNotFoundError` has two common causes: a misspelled name, or a package missing from the active environment.

**0.4** Checkpoint, no solution file.
