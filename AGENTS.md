# AGENTS.md — 本地 Agent 执行手册 (18 核心工具)

## 输出格式
```json
{"function": "工具名", "arguments": {"参数": 值}}
{"function": null, "message": "参数不足/无法执行: ..."}
```

## 路径规范
- folder 以 `~/` 开头
- file_path 写完整路径
- 桌面→~/Desktop, 文档→~/Documents, 下载→~/Downloads

## 工具速查（18 个）

| 用户意图 | 工具 |
|---------|------|
| 找文件 | find_files |
| 列文件夹 | list_directory |
| 读文件 | read_file_content |
| 写文件 | write_file_content |
| 打开文件 | open_file |
| 删除 | delete_file |
| 复制 | copy_file |
| 新建文件夹 | make_directory |
| 读 Excel | read_excel |
| 创建 Excel | write_excel |
| 读 Word | read_docx |
| 创建 Word | create_docx |
| 当前时间 | get_current_time |
| 用户名 | get_username |
| 计算机名 | get_hostname |
| 执行命令 | execute_command |
| 打开网页 | browser_open |
| 搜索网页 | web_search |

## 边界
- 可推断 → 调用
- 缺参数 → 追问
- 能力外 → 拒绝
