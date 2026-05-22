## v2.1 (2026-05-22)

### Fixed
- agent_server: add try/except around execute_plan to prevent crashes blocking the watch loop
- agent_server: catch scan exceptions in watch_claude_plans with traceback logging
- cloud_bridge: fix step reference parsing — support both `{step.output}` and `{{step.output}}` with array indexing `[0]`
- tools.py: increase execute_command timeout from 30s to 120s

### Changed
- build_local_prompt: reduce core tools from 28 to 18 to fit 4K context (2,196 tokens)
- AGENTS.md: updated to 18-tool quick reference
