# Before Day 3: Git and GitHub (15 minutes)

Day 3 uses Git and GitHub. Do this once, before class.

1. **Create a free GitHub account** at <https://github.com/signup>. Remember your username.
2. **Install Git**
   - Windows: download "Git for Windows" from <https://git-scm.com/download/win>, install with the defaults (it includes Git Credential Manager, which handles the GitHub login for you).
   - macOS: in the terminal run `git --version`; if Git is missing, macOS offers to install the command line tools. Accept.
   - Linux: `sudo apt-get install git` (Debian, Ubuntu) or your distribution's equivalent.
3. **Check** (new terminal): `git --version` prints a version.
4. **Tell Git who you are** (use the e-mail of your GitHub account):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   git config --global init.defaultBranch main
   ```
5. **Add JupyterLab** to the course environment:
   ```bash
   conda activate scientific-programming
   conda install jupyterlab
   ```
6. **Check the GitHub login** (the first `git push` asks for it; see "Authenticating with GitHub" in the Day 3 handout). The simplest option on every system is the GitHub CLI: install it from <https://cli.github.com/> and run `gh auth login`, choosing HTTPS and "Login with a web browser".

Stuck? Bring the error message to class; we fix it together at the start.
