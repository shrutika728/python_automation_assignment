# Python Automation Assignment

Quick guide to run Robot tests locally and in CI.

## Run locally (recommended)
1. Create and activate virtual environment (if not already created):
   - PowerShell: & .\.venv\Scripts\Activate.ps1
   - CMD: .\.venv\Scripts\activate
   - Bash: source .venv/bin/activate

2. Install dependencies:
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Run tests using the project's Python so project root is on sys.path:
   ```powershell
   .\.venv\Scripts\python -m robot.run tests
   ```

4. Results: `output.xml`, `report.html`, and `log.html` will be generated in the project root.

## Why use `python -m robot.run` instead of `robot`/`robot.exe` directly
- Running `python -m robot.run` ensures the project root (current working directory) is on Python's `sys.path` so Robot can import local libraries (like `libraries.custom_lib`) without extra configuration.
- Calling `robot`/`robot.exe` directly can run a different Python interpreter or omit the project root from `PYTHONPATH`, causing `ModuleNotFoundError: No module named 'libraries'` or missing custom keywords like `Get Base Url`.

## Quick workaround (if you must use `robot` directly)
- Set PYTHONPATH to include the project root before running `robot`:
  - PowerShell: `$env:PYTHONPATH = (Get-Location).Path; robot tests`
  - CMD: `set PYTHONPATH=%CD% && robot tests`

## CI
The included GitHub Actions workflow `.github/workflows/robot-tests.yml` runs `python -m robot.run tests` to avoid import issues.

---
If you want, I can also add a script (e.g., `run_tests.ps1`) to encapsulate these steps for convenience.