## v3.0.3 (2026-05-22)

### Fixed
- agent_server: execute_plan now uses callback-based resolver (same as cloud_bridge)
- Nested data references verified E2E: `{step0.output.memory.percent}` → 78.4%
- Agent responsiveness: async watch loop + 60s timeout + "running" status

### Verified
- 4-step plan with data passing: system_info → get_time → create_docx → read_docx
- All references resolved correctly: CPU 12.9%, Mem 78.4%, Disk 93.1%
- Agent no longer blocks: instant response + background execution
