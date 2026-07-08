# 端到端示例：从意图到成片素材

以"节日开幕式收尾致谢镜头"为例走一遍完整流程。

## 第 1 步 · 为你的角色建参考图

用 `templates/image/character-reference.md` 模板，替换角色描述后生成四视角参考图，人工挑选定版。

## 第 2 步 · 分镜生图

```bash
python3 agent/generate.py --type image --skill fairytale-festival \
  --intent "两位主持角色（人形馆员+吉祥物）在舞台中央向观众鞠躬致谢，暖金舞台光，台下坐满小朋友" \
  --dry-run
```

把输出贴给任意大模型得到生图提示词 → 投喂文生图平台（附上第 1 步参考图）→ 多版本比选定版。

## 第 3 步 · 图生视频

```bash
python3 agent/generate.py --type video --skill fairytale-festival \
  --intent "以定版图为首帧：0-2秒两人直起身站定微笑，2-5秒A说'感谢大家'（口型对应），5-8秒B展臂'明年再见'（口型对应），末2秒定格，共10秒" \
  --dry-run
```

输出的视频提示词连同定版首帧图一起投喂视频平台。

## 第 4 步 · 出片排查

对照 `templates/skills/fairytale-festival/video-prompts.md` 末尾的排查清单逐项检查；哪一拍崩单独重生成那一拍。

## 三条底线（再念一遍）

1. 图像先行——图不定版不进视频。
2. 免费试错、付费出片——未验证的提示词不进付费生成。
3. 文字后期加——别让模型画字。
