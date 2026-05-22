# Local-Auto-Agent

离线优先的电脑操作助手。云端大模型做任务规划，本地 Qwen 7B 做工具执行，1+1 协同。

## 架构

```
复杂任务 → DeepSeek（拆步规划，68 工具）→ JSON 步骤计划
                                              ↓
                                   本地 7B（翻译单步，18 核心工具）
                                              ↓
                                   tools.py（68 个安全收口函数）
```

## 快速开始

```bash
pip install requests pandas openpyxl python-docx python-pptx PyPDF2 pillow playwright
playwright install msedge
```

编辑 `启动服务器.bat`，填入 API Key：
```bat
set DEEPSEEK_API_KEY=sk-xxx
set GITHUB_TOKEN=ghp_xxx
```

双击 `启动服务器.bat`，浏览器打开 http://localhost:8765

## 工具概览（68 个 + Skill 系统）

| 类别 | 数量 | 示例 |
|------|------|------|
| 文件操作 | 17 | find, read, write, delete, copy, grep, batch_rename |
| 办公文档 | 13 | Excel, Word, PPT, PDF 读写编辑 |
| 系统信息 | 10 | 时间, 进程, 截图, IP |
| 浏览器 | 6 | 打开网页, 搜索, 点击, 截图 |
| 网络/GitHub | 5 | HTTP, GitHub 搜索/下载/安装 |
| 安全/工具 | 17 | CMD+黑名单, SQL, 邮件, 翻译 |

## Skill 系统

```python
install_skill("owner/repo")  # 从 GitHub 一键安装
```

创建 Skill：[hello-skill](https://github.com/sovevip/hello-skill) 模板

## 安全

- workspace 边界锁
- CMD 黑名单（format/del/shutdown）
- 写入/删除需确认
- 确认函数不暴露给模型

## 状态

| Phase 1 | Phase 2 | Phase 5 | Phase 6 |
|---------|---------|---------|---------|
| ✅ 68 工具全绿 | ✅ 92% 跳过微调 | ✅ 执行循环 | ✅ 云端规划 |
