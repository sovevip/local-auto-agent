## v3.0.1 (2026-05-22)

### Fixed
- PLANNER_PROMPT: add nested key example `{step0.output.memory.percent}`
- execute_plan: safe utf-8 error message encoding
- test_complex.py: force utf-8 stdout to avoid GBK encoding crash
- test_complex.py: demonstrate correct nested key syntax in prompt

### Architecture Verified
- Cloud planner correctly generates 5-step plans with risk labels
- validate_plan detects risk distribution (low:3, medium:2 for system report)
- Step references `{step.output.nested.key}` resolve correctly
- Document generation produces real data, not placeholders
