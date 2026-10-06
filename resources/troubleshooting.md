# Troubleshooting Guide & FAQ
*Introduction to Scientific Programming - Common Issues and Solutions*

## 🚨 Quick Emergency Fixes

### Can't find Python or conda?
```bash
# Try these commands to locate your installation:
which python    # macOS/Linux
where python    # Windows
which conda     # macOS/Linux  
where conda     # Windows
```

### VS Code not working with Python?
1. **Ctrl+Shift+P** → "Python: Select Interpreter"
2. Choose Anaconda Python (path contains `anaconda3`)
3. Restart VS Code

### Import errors?
```bash
# Check what's installed:
conda list
# Install missing packages:
conda install package_name
```

---

## 📋 Installation & Setup Issues

### Q: "Python not found" or "conda not found" error
**A:** This is a PATH issue - your system doesn't know where to find Python/conda.

**Windows Solutions:**
- Reinstall Anaconda and **check "Add Anaconda to PATH"** during installation
- Manually add to PATH: `C:\Anaconda3\` and `C:\Anaconda3\Scripts\`
- Use Anaconda Prompt instead of Command Prompt
- Try full path: `C:\Anaconda3\python.exe --version`

**macOS Solutions:**
- Run `conda init zsh` (or `conda init bash`) in Terminal
- Restart Terminal completely
- Check if conda is in `/opt/anaconda3/bin/conda`
- Add to shell profile: `export PATH="/opt/anaconda3/bin:$PATH"`

**Linux Solutions:**
- Run `conda init bash` and restart terminal
- Check installation path: usually `~/anaconda3/bin/conda`
- Source your shell profile: `source ~/.bashrc`

### Q: VS Code doesn't recognize my Python installation
**A:** VS Code needs to be told which Python interpreter to use.

**Solution:**
1. Open VS Code
2. **Ctrl+Shift+P** (Cmd+Shift+P on Mac) → "Python: Select Interpreter"
3. Choose the Anaconda Python (path should contain `anaconda3`)
4. If not listed, click "Enter interpreter path" and browse to:
   - Windows: `C:\Anaconda3\python.exe`
   - macOS: `/opt/anaconda3/bin/python`
   - Linux: `~/anaconda3/bin/python`

### Q: Package installation fails with permission errors
**A:** Don't use `sudo` with conda/pip - this causes permission issues.

**Solutions:**
- Use `conda install` instead of `pip install` when possible
- If using pip: `pip install --user package_name`
- Check conda environment: `conda info --envs`
- Create new environment if needed: `conda create -n myenv python=3.11`

### Q: "SSL Certificate" errors during package installation
**A:** Network/firewall issues preventing secure downloads.

**Solutions:**
- Try: `conda config --set ssl_verify false` (temporary fix)
- Use different conda channel: `conda install -c conda-forge package_name`
- Check institutional firewall settings
- Try pip instead: `pip install package_name`

---

## 🐍 Python & Package Management

### Q: Import errors - "ModuleNotFoundError"
**A:** Package not installed or wrong environment active.

**Debugging Steps:**
1. Check active environment: `conda info --envs` (active has `*`)
2. List installed packages: `conda list | grep package_name`
3. Install missing package: `conda install package_name`
4. Verify in Python: `import package_name; print(package_name.__version__)`

### Q: Different Python versions causing conflicts
**A:** Multiple Python installations can conflict.

**Solution:**
1. Check all Python installations: `which -a python` (macOS/Linux)
2. Use conda environments to isolate projects:
   ```bash
   conda create -n scientific python=3.11
   conda activate scientific
   conda install numpy pandas matplotlib
   ```
3. Always activate correct environment before working

### Q: Jupyter notebooks not working in VS Code
**A:** Missing Jupyter extension or kernel issues.

**Solutions:**
1. Install VS Code Jupyter extension
2. Install Jupyter: `conda install jupyter`
3. Select correct kernel in VS Code (top-right of notebook)
4. If kernel missing: **Ctrl+Shift+P** → "Jupyter: Select Interpreter to Start Jupyter Server"

### Q: Packages installed but still getting import errors
**A:** Likely using wrong Python interpreter or environment.

**Check:**
```python
import sys
print(sys.executable)  # Shows which Python is running
print(sys.path)        # Shows where Python looks for packages
```

**Fix:** Ensure VS Code uses same Python as where packages are installed.

---

## 💻 Development Environment Issues

### Q: VS Code Python extension not working
**A:** Extension conflicts or outdated versions.

**Solutions:**
1. Update VS Code and Python extension
2. Disable conflicting extensions temporarily
3. Reload window: **Ctrl+Shift+P** → "Developer: Reload Window"
4. Check extension logs: **Ctrl+Shift+P** → "Python: Show Output"

### Q: Code formatting not working (Black, autopep8)
**A:** Formatter not installed or not configured.

**Setup:**
1. Install formatter: `conda install black`
2. VS Code settings: **Ctrl+,** → search "python formatting"
3. Set "Python › Formatting: Provider" to "black"
4. Format on save: enable "Editor: Format On Save"

### Q: Debugging not working in VS Code
**A:** Debugger configuration issues.

**Solutions:**
1. Install "Python Debugger" extension
2. Set breakpoints by clicking left margin
3. Press **F5** to start debugging
4. If issues persist: **Ctrl+Shift+P** → "Python: Configure Debug Configuration"

### Q: Terminal not opening in VS Code
**A:** Terminal configuration or permission issues.

**Solutions:**
- **Ctrl+`** to open integrated terminal
- Check terminal settings: **Ctrl+,** → search "terminal"
- Windows: Set default terminal to Command Prompt or PowerShell
- macOS: Ensure Terminal app has proper permissions

---

## 📊 Data Analysis & Visualization Issues

### Q: Matplotlib plots not showing
**A:** Backend or display issues.

**Solutions:**
```python
import matplotlib
matplotlib.use('TkAgg')  # Try different backend
import matplotlib.pyplot as plt
plt.ion()  # Turn on interactive mode
plt.show()
```

### Q: "DLL load failed" errors on Windows
**A:** Missing Visual C++ redistributables or conflicting installations.

**Solutions:**
1. Install Visual C++ Redistributable from Microsoft
2. Reinstall problematic package: `conda uninstall package_name && conda install package_name`
3. Try conda-forge channel: `conda install -c conda-forge package_name`

### Q: Pandas reading CSV files with encoding errors
**A:** File encoding issues (common with international characters).

**Solutions:**
```python
# Try different encodings:
df = pd.read_csv('file.csv', encoding='utf-8')
df = pd.read_csv('file.csv', encoding='latin1')
df = pd.read_csv('file.csv', encoding='cp1252')

# Auto-detect encoding:
import chardet
with open('file.csv', 'rb') as f:
    encoding = chardet.detect(f.read())['encoding']
df = pd.read_csv('file.csv', encoding=encoding)
```

### Q: Memory errors with large datasets
**A:** Dataset too large for available RAM.

**Solutions:**
```python
# Read in chunks:
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    process_chunk(chunk)

# Use specific data types to reduce memory:
df = pd.read_csv('file.csv', dtype={'column': 'category'})

# Use Dask for larger-than-memory datasets:
import dask.dataframe as dd
df = dd.read_csv('large_file.csv')
```

---

## 🔧 Advanced Troubleshooting

### Q: How do I set up the course environment?
```bash
conda env create -f environment.yml        # Days 1-9 and 11
conda activate scientific-programming

conda env create -f environment-dl.yml     # Day 10 (adds PyTorch and friends)
conda activate scientific-programming-dl
```
No conda? Use `python -m venv .venv`, activate it, then `pip install -r requirements.txt` (or `requirements-dl.txt` for Day 10). Check the result with `python day01-introduction/demo_scripts/check_installation.py`.

### Q: A script or notebook cannot save a figure, or I cannot find the output
Scripts and notebooks write generated files to an `outputs/` folder next to where they run (it is created automatically and ignored by Git). Look there first.

### Q: Conda environments corrupted or broken
**A:** Environment corruption can happen with interrupted installations.

**Solutions:**
```bash
# List environments:
conda info --envs

# Remove corrupted environment:
conda env remove -n environment_name

# Create fresh environment:
conda create -n new_env python=3.11
conda activate new_env
conda install numpy pandas matplotlib seaborn scipy jupyter

# Export/import environments:
conda env export > environment.yml
conda env create -f environment.yml
```

### Q: Git integration not working in VS Code
**A:** Git not installed or not in PATH.

**Solutions:**
1. Install Git: https://git-scm.com/downloads
2. Restart VS Code after Git installation
3. Check Git path: **Ctrl+Shift+P** → "Git: Show Git Output"
4. Configure Git:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### Q: Performance issues - Python running slowly
**A:** Various optimization opportunities.

**Solutions:**
1. Use vectorized operations (NumPy/Pandas) instead of loops
2. Profile code: `python -m cProfile script.py`
3. Consider using Numba for numerical code:
   ```python
   from numba import jit
   @jit
   def fast_function(x):
       return x ** 2
   ```
4. Use appropriate data types (float32 vs float64, categories for strings)

---

## 🆘 Getting Help

### When to Ask for Help
- After trying solutions above for 15+ minutes
- When error messages are unclear or not covered here
- When you suspect hardware/system-level issues

### How to Ask Effective Questions
1. **Include error message** (full traceback)
2. **Describe what you were trying to do**
3. **Show your code** (minimal example that reproduces the issue)
4. **Mention your system**: OS, Python version, package versions
5. **What you've already tried**

### Information to Gather Before Asking
```bash
# System information:
python --version
conda --version
conda list | grep numpy  # or other relevant packages

# In Python:
import sys
print(sys.version)
print(sys.executable)

# VS Code information:
# Help → About (shows version)
# Extensions → Show installed extensions
```

### Where to Get Help
1. **Course GitHub Discussions** - for course-specific questions
2. **Stack Overflow** - for general programming questions
3. **Package documentation** - official docs are often best
4. **Office hours** - Fridays after class (by appointment)

---

## 📚 Useful Resources

### Documentation Links
- [Python Official Docs](https://docs.python.org/3/)
- [Anaconda User Guide](https://docs.anaconda.com/anaconda/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Community Forums
- [Python Reddit](https://www.reddit.com/r/Python/)
- [Stack Overflow Python Tag](https://stackoverflow.com/questions/tagged/python)
- [VS Code GitHub Issues](https://github.com/microsoft/vscode-python/issues)

---

*Remember: Troubleshooting is a skill that improves with practice. Don't get discouraged - even experienced programmers spend significant time debugging!*
