## v3.0 (2026-05-22) — Architecture Restructure

### Breaking Changes
- tools.py split into 10 modules under tools/
- Old tools.py renamed to tools.py.bak

### Added
- tools/validate.py — deterministic validation layer with 4-level risk system
- Risk levels: low(48) / medium(40) / high(11) / critical(1)
- validate_step() — per-step schema/path/injection checks
- validate_plan() — plan-level risk analysis, blocks critical ops
- All 100 tools tagged with risk levels

### Changed
- cloud_bridge: planner outputs strict JSON with risk labels
- cloud_bridge: execute_plan runs validate_plan before execution
- cloud_bridge: blocks critical-level operations (run_python) without explicit approval
- cloud_bridge: supports new {tool, args} format alongside legacy {function, arguments}

### Architecture
```
User task → DeepSeek → JSON steps (with risk labels)
                         ↓
              validate.py (deterministic checks)
                         ↓
              tools/ (100 functions, 10 modules)
```
