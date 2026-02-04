# Python API Automation — Robot Framework

A small automation framework that tests the public JSONPlaceholder REST API (https://jsonplaceholder.typicode.com) using Robot Framework and RequestsLibrary.

---

## Quick start (recommended) ✅
1. Create and activate virtual environment (if not created):
   - PowerShell: & .\\.venv\\Scripts\\Activate.ps1
   - CMD: .\\.venv\\Scripts\\activate
   - Bash: source .venv/bin/activate

2. Install dependencies:

   python -m pip install --upgrade pip
   pip install -r requirements.txt

3. Run tests (recommended to ensure local project imports work):

   .\\.venv\\Scripts\\python -m robot.run tests

4. View reports (generated in project root):
   - output.xml, report.html, log.html

---

## Alternative (if you prefer running `robot` directly)
- Ensure `robotframework` and `robotframework-requests` are installed in the Python used by the `robot` command, and set PYTHONPATH to project root if necessary:
  - PowerShell: $env:PYTHONPATH = (Get-Location).Path; robot tests
  - CMD: set PYTHONPATH=%CD% && robot tests

Note: Running `robot` directly can cause `ModuleNotFoundError: No module named 'libraries'` if the project root is not on PYTHONPATH. Using `python -m robot.run` avoids this by running Robot in the same interpreter that has the project on sys.path.

---

## Project structure
- tests/                 - Robot test suites
- resources/             - Robot resource files and keywords
- libraries/             - Python helper libraries (e.g., `custom_lib.py`)
- config/                - Configuration files (e.g., `config.yaml`)
- .github/workflows/     - CI workflows

---

## How tests are organized
- `tests/user_api_tests.robot` — core API scenarios (GET/POST/negative)
- `tests/data_driven_tests.robot` — data-driven example (template usage)
- `resources/api_keywords.robot` — reusable API keywords (session handling, CRUD actions)
- `libraries/custom_lib.py` — Python helpers: config loader, response helpers

---

## CI
The workflow `.github/workflows/robot-tests.yml` installs dependencies and runs tests with:

  python -m robot.run tests

This ensures consistent behavior on CI and avoids import issues.

---

## Troubleshooting
- "No keyword with name 'Get Base Url' found": run tests with the venv Python (see Quick start) so Robot can import `libraries` package.
- TLS/SSL warnings: add `verify=True` when creating sessions or configure cert verification as needed.

---

## Tips
- To add tests, create new files under `tests/` and use `Resource    ../resources/api_keywords.robot` to reuse keywords.
- Keep keywords simple and document them with `[Documentation]` lines.

---

If you want, I can also add a small `run_tests.ps1` helper script and a short CONTRIBUTING note explaining how to extend the framework.
