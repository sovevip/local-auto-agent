## v3.0.1 (2026-05-22)

### Fixed
- execute_plan: nested key regex changed from `?` to `*` for multi-level references
- agent_server: watch_claude_plans now async with 90s thread timeout
- agent_server: execute_plan runs in daemon thread, doesn't block plan scanning
- test_complex.py: utf-8 stdout wrapper
- PLANNER_PROMPT: nested key example `{step0.output.memory.percent}`
