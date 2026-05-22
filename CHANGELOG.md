## v3.0.2 (2026-05-22)

### Fixed
- execute_plan: callback-based step reference resolver — correctly handles multiple different references in one string
- execute_plan: nested key resolution now works for `{step0.output.memory.percent}`
- test_regex.py: verified 4/4 callback resolver cases

### Added
- setup.bat: one-click dependency installer
- requirements.txt: pinned dependency versions
- test_security.py: 17 security boundary tests (ALL PASS)
- git tools: git_clone, git_status, git_commit, git_push, git_pull

Total: 105 tools
