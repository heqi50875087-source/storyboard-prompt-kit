# ChatGPT Image 2(GPT Image 2)生图提示词技法卡

> 主力工具:用户常用 ChatGPT 的 GPT Image 2 出图。本卡提炼其提示词套路 + 跨图一致性公式。
> 配套:本机 `gpt-image-2` 技能(18 大类、80+ 结构化模板,含电影分镜 cinematic-storyboard-grid、角色表 character-sheet)。

## 一、GPT Image 2 的脾气(和 Midjourney 反着来)
- **吃自然语言长描述**:它是对话式模型,指令跟随强、文字渲染强。用**细致、具体的英文段落**,别堆关键词。
- **能用结构化 JSON**:画面元素多、要多区域/多 panel、要复用调试时,用 JSON 强约束——把"角色/光影/构图"各装各的盒子,**防 concept bleed**(实测角色漂移 <3%,自然语言可漂 20%)。
- **编辑能力强**:可上传参考图做"定点编辑"(change background / change clothing),主体不动只改局部。

## 二、跨图一致性公式(核心,不崩脸)
1. **角色圣经(Character Bible)**:把每个角色的固定特征(脸型/眼/发/服装/配色/年龄)写成**一段常量**,每张图**原样复用、绝不改写**;只改 动作/环境/景别/情绪。崩脸根因=每次重描角色。
2. **风格圣经(Style Bible)**:媒介/画风/调色板/光线/渲染 固化成一段,**每张图末尾原样粘贴**。
3. **锚点帧**:先精修一张"定妆照"hero frame,风格定死,再用它当参考(上传图)生成其余。
4. **JSON 角色圣经**(一致性最强):把角色固定属性独立成 `subject.character` 字段,每镜只换 `shot` 段。

## 三、电影分镜 JSON 骨架(来自 gpt-image-2 技能 5.5.1)
```json
{
  "subject": { "primary": "", "mood": "", "style": "", "aspect_ratio_per_panel": "" },
  "character": { "name": "", "age": "", "face": "", "hair": "", "outfit": "" },
  "layout": { "grid": {"rows":0,"columns":0,"count":0},
              "continuity": "(必填)声明 N 个 panel 是连续叙事/同一 hero/同一 mood" },
  "lighting": { "primary": "", "secondary": "" },
  "environment": { "location": "", "weather": "" }
}
```
经验:每镜含「景别 + 主体动作 + 光线/情绪」三要素;远/中/近/POV 混搭;`continuity` 必填。

## 四、可复用示例(英文原样,复制到 ChatGPT)
**逐镜关键帧(自然语言版,角色圣经嵌入)**
```
A medium full shot of Mei — a 10-year-old girl with a round face, large brown almond
eyes, light freckles, shoulder-length black hair with straight bangs, wearing a
mustard-yellow raincoat and blue rubber boots — jumping over a puddle and laughing,
on a rainy neon-lit city street at dusk, reflections on wet ground, eye level, joyful.
Soft 3D Pixar-like render, warm color palette, gentle cinematic lighting. 16:9.
```
**JSON 角色圣经(跨镜锁人,只改 shot 段)**
```json
{ "character_bible": {"name":"Mei","face":"round face, large brown almond eyes, freckles",
  "hair":"shoulder-length black hair, straight bangs","outfit":"mustard-yellow raincoat, blue boots",
  "style":"soft 3D Pixar-like, warm palette","consistency":"keep identical face/hair/proportions every shot"},
  "shot": {"action":"jumping over a puddle, laughing","scene":"rainy neon street at dusk",
  "camera":"medium shot, eye level","aspect_ratio":"16:9"} }
```

## 五、来源
- 本机 `gpt-image-2` 技能(claude-config/skills/gpt-image-2):references/prompt-writing.md(JSON 总规范)、storyboards-and-sequences/cinematic-storyboard-grid.md、portraits-and-characters/character-sheet.md
