#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""storyboard-prompt-kit 组装器：分镜意图 -> 生图/生视频提示词。

零依赖（纯标准库）。两种模式：
  --dry-run          只组装提示词包并打印，不调用任何模型（复制粘贴到任意 LLM 使用）
  默认               调用 OpenAI 兼容接口生成（本地 Ollama/LM Studio 或云端 API 均可）

示例：
  python3 agent/generate.py --type image --intent "戴眼镜的小熊在图书馆讲绘本" --dry-run
  python3 agent/generate.py --type video --skill fairytale-festival --intent "开幕式收尾致谢，12秒"
"""
import argparse
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "templates"

BUNDLES = {
    "image": ["image/storyboard-image.md", "image/character-reference.md"],
    "video": ["video/shot-prompt.md", "video/continuity-rules.md", "video/negative-prompts.md"],
}
SKILL_FILES = {"image": "image-prompts.md", "video": "video-prompts.md"}

SYSTEM = (
    "你是一名 AI 内容生产的提示词工程师。依据下面的模板与规则，"
    "把用户的分镜意图改写成一条可直接投喂{kind}模型的完整提示词。"
    "要求：抽象形容词改写为可见动作与空间关系；角色外观逐项写全；"
    "严格套用模板中的硬约束与负面提示词；只输出最终提示词本身，不要解释。\n\n"
    "==== 模板与规则 ====\n{rules}"
)


def load_rules(gen_type, skill=None):
    parts = []
    for rel in BUNDLES[gen_type]:
        parts.append((TPL / rel).read_text(encoding="utf-8"))
    if skill:
        sf = TPL / "skills" / skill / SKILL_FILES[gen_type]
        if not sf.exists():
            sys.exit(f"未找到 Skill 文件: {sf}")
        parts.append(sf.read_text(encoding="utf-8"))
    return "\n\n---\n\n".join(parts)


def call_llm(cfg: dict, system: str, user: str) -> str:
    req = urllib.request.Request(
        cfg["endpoint"].rstrip("/") + "/chat/completions",
        data=json.dumps({
            "model": cfg["model"],
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": cfg.get("temperature", 0.7),
        }).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cfg.get('api_key', 'none')}",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def main() -> None:
    ap = argparse.ArgumentParser(description="分镜意图 -> 生图/生视频提示词")
    ap.add_argument("--type", choices=["image", "video"], required=True)
    ap.add_argument("--intent", required=True, help="分镜意图（一句话或结构化描述）")
    ap.add_argument("--skill", default=None, help="可选场景方案，如 fairytale-festival")
    ap.add_argument("--dry-run", action="store_true", help="只输出组装的提示词包，不调用模型")
    ap.add_argument("--config", default=str(ROOT / "agent" / "config.json"))
    args = ap.parse_args()

    rules = load_rules(args.type, args.skill)
    kind = "文生图/图生图" if args.type == "image" else "图生视频/文生视频"
    system = SYSTEM.format(kind=kind, rules=rules)
    user = f"分镜意图：{args.intent}"

    if args.dry_run:
        print("=" * 20, "SYSTEM（模板与规则）", "=" * 20)
        print(system)
        print("=" * 20, "USER（你的意图）", "=" * 20)
        print(user)
        print("\n将以上两段一起粘贴给任意大语言模型即可。")
        return

    cfg_path = Path(args.config)
    if not cfg_path.exists():
        sys.exit("未找到 config.json——复制 agent/config.example.json 为 agent/config.json 并填写，或改用 --dry-run。")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    print(call_llm(cfg, system, user))


if __name__ == "__main__":
    main()
