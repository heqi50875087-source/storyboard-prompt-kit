# fairytale-festival · 童话节/少儿节日活动方案（可选 Skill）

面向少儿阅读节、开幕式、亲子活动等场景的成套提示词方案，源自一场真实开幕式宣传片（约 8 分钟成片）的完整生产。

## 适用

- 节日开幕式/闭幕式视频、活动宣传片、舞台大屏素材
- 少儿向 3D 卡通风格、双角色主持结构（真人感 IP + 吉祥物）
- 儿童友好审美：暖色调、圆润造型、明快节奏

## 内容

| 文件 | 用途 |
|---|---|
| `image-prompts.md` | 节日生图方案：舞台/海报氛围、角色同框、书籍意象 |
| `video-prompts.md` | 节日视频方案：连续音轨结构、口型绑定、空镜声明、收尾定格 |

## 使用前提

角色外观均为 `[占位符]`——替换为你自己的角色设定即可。建议先用 `templates/image/character-reference.md` 为你的角色建立参考图，再进入本方案。

## 调用

```bash
python3 agent/generate.py --type video --skill fairytale-festival --intent "你的分镜意图" --dry-run
```
