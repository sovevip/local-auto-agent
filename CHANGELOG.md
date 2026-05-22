## v2.1 (2026-05-22)

### Fixed
- agent_server: add try/except around execute_plan to prevent crashes
- agent_server: catch scan exceptions with traceback logging
- cloud_bridge: fix step reference parsing — `{step.output}[0]` array indexing
- tools.py: increase execute_command timeout 30s→120s

### Changed
- build_local_prompt: reduce core tools 28→18 (2,196 tokens, fits 4K ctx)
- build_local_prompt: add extra_rules param, AGENTS.md now injected into model prompt
- local_agent.py: load AGENTS.md and pass via build_local_prompt()
- agent_server.py: load AGENTS.md at startup and inject into local_chat()
- AGENTS.md: updated to 18-tool quick reference

### Added
- README.md: project overview, quick start, architecture diagram
- 启动服务器.bat: GITHUB_TOKEN placeholder
- test_new_tools.py: lightweight test for 17 new tools (13/14 PASS)
- test_exec_loop.py: 8/8 core scenarios verified
- test_cloud.py: cloud_bridge integration test (3/3 PASS)
- run_tests.py: test runner with output capture
