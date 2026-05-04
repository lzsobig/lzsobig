# 🔮 RAG 知识库智能问答系统

基于检索增强生成（RAG）架构的企业级知识库问答系统，支持文档上传、智能分块、语义检索与多 Agent 协作生成。

## 核心特性

- **多 Agent 长链推理** — 向量检索 → 上下文组装 → LLM 生成，全链路可视化
- **智能文档解析** — 支持 .txt / .md / .pdf，自动分块与向量化
- **语义检索** — 基于 ChromaDB 向量数据库，精准匹配相关片段
- **来源溯源** — 每条回答标注来源文档与相关度评分
- **Token 统计** — 实时追踪消耗量，便于成本管控

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | 原生 HTML/CSS/JS，Agent 链路动画可视化 |
| 后端 | Python + FastAPI |
| 向量数据库 | ChromaDB（all-MiniLM-L6-v2 embedding） |
| LLM | OpenRouter API（DeepSeek V3） |

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置 API Key
export OPENROUTER_API_KEY="sk-or-你的key"

# 启动
python app.py

