# Local-Auto-Agent 实施方案 v1.3

> **云端模型做大脑（决策/规划），本地微调模型做手脚（工具执行），1+1 离线协同。**

当前状态：Phase 2 进行中，分批测试 92% 工具选择率，跳过 Phase 3-4 微调。

---

## 核心架构

```
用户指令 → cloud_bridge.py（云端规划）→ JSON 步骤计划
                ↓
       local_agent.py（逐步解析、调用 tools.py）
                ↓
          tools.py（安全收口的 Python 函数库，68 个工具）
```

## 工具清单（68 个，含 Skill 系统）

### 文件操作（14个）
find_files, list_directory, read/write_file_content, open_file, rename_file,
delete_file, copy_file, make_directory, grep_file, batch_rename, file_info,
count_words, read/write_json, zip/unzip, download_file

### 办公文档（12个）
create/read_docx, edit_docx, create/read_pptx, create/read_pdf, create_html,
read/write_excel, sum_excel_column, sum_csv_column, merge_csvs, csv_to_json

### 系统信息（11个）
get_current_time, get_current_directory, get_username, get_hostname, get_ip,
ping_host, list_processes, kill_process, screen_capture

### 浏览器（6个）
browser_open, browser_click, browser_type, browser_read, browser_screenshot, web_search

### 网络 & GitHub（6个）
http_request, github_search, github_get_repo, github_download_repo, install_skill

### 安全 & 工具（19个）
execute_command, run_python, sql_query, sql_exec, send_email, send_notification,
image_resize, translate_text, clipboard_copy/paste, set_reminder, calculator,
generate_password, hash_text, base64_cmd, date_diff

## 安装

```bash
pip install requests pandas openpyxl python-docx python-pptx PyPDF2 pillow playwright
playwright install msedge
```

## 安全设计

- workspace 边界锁：`set_workspace()` 前所有文件操作拒绝
- CMD 黑名单：format/del/shutdown 等禁止执行
- HITL 确认：写入/打开/合并/删除均需确认
- 模型不可绕过：ask_user_confirmation 不暴露给模型 Schema
