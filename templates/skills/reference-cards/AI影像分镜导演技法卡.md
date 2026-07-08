# 导演思维 × AI 分镜：从主题/剧本到电影感镜头的硬方法

> 一句话总览：**先用导演的"故事节拍 + 镜头覆盖"把主题拆成镜头表，再用平台公式把每个镜头翻译成"一句话讲清的提示词"。** 关键不是写得花，而是写得"准"——一个景别、一个运镜、一支镜头，配上"先定风格再定人"的一致性套路。

## 来源链接（真实 URL）

- StudioBinder · 如何做分镜表（导演拆镜流程）：https://www.studiobinder.com/blog/how-to-make-a-shot-list/
- StudioBinder · Save the Cat 15 拍节拍表：https://www.studiobinder.com/blog/save-the-cat-beat-sheet/
- Save the Cat 官方节拍工具：https://savethecat.com/beat-sheets ｜ https://savethecat.com/beat-mapper
- Prompt Architects · Veo3/Kling 30 条电影运镜提示词：https://prompt-architects.com/blog/25-30-cinematic-camera-prompts-for-veo3-and-kling
- AtlasCloud · Kling 提示词公式 + 示例：https://www.atlascloud.ai/blog/guides/kling-ai-video-prompt-guide
- Medium（CreativeAININJA）· Runway/Kling/Veo/Sora 控制策略：https://medium.com/@creativeaininja/how-to-actually-control-next-gen-video-ai-runway-kling-veo-and-sora-prompting-strategies-92ef0055658b
- Midjourney 角色一致性（--cref/--cw/seed）：https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds
- Segmind · 首帧尾帧（First & Last Frame）视频模型：https://www.segmind.com/models/all/first-and-last-frame-video-models
- Curious Refuge · 全球第一所 AI 电影学校：https://curiousrefuge.com/ai-filmmaking

---

## 技法 A：导演思维——主题/剧本 → 镜头表（不碰相机，先拆故事）

**铁律：从剧本出发，不从镜头出发。每个镜头都要能追溯到"它为故事做了什么"。**

1. **先用 15 拍把主题骨架搭好（Save the Cat）**，短片可压缩成"开场画面→主题点题→催化事件→中点→一败涂地→灵魂黑夜→破入第三幕→结尾画面"。整片工作流就一条线：**节拍表 → 场景清单 → 初稿 → 节拍审计 → 重写**。开场画面与结尾画面要"对仗"，一头一尾框住主题、展示"改变了什么"。
2. **逐场标"故事节拍"(story beats)**：把一场戏里每个情绪/动作转折点圈出来，反复问那句导演口头禅——**"How can I film this in a way that serves the story?"**
3. **给每个节拍配镜头参数**：景别（Shot size = 主体在画面里多大）+ 机位角度（Angle = 相机相对主体的位置，平视/俯/仰/荷兰角）+ 镜头焦段 + 是否运动。**记住：景别和机位是两件事，要分开写。**
4. **想"覆盖"，别只想"英雄镜头"(think coverage, not just hero shots)**：一场戏至少备齐 **主镜(master) + 过肩(OTS) + 插入特写(insert)**，多给角度和插入镜头是"保护剪辑"——后期才有的剪。
5. **按"布光相同"分组拍/分组生成(setup)**：需要同一套光的镜头放一起做，效率最高（AI 出图也一样：同一光线设定的镜头连着出，风格更稳）。
6. **配参考图/floor plan**：每个镜头贴一张参考帧或故事板，标清相机、人物、光位的空间关系，再动手。

> 套路记忆：**主题 →（15拍）故事线 → 逐场圈节拍 → 每拍配[景别+角度+焦段+运镜] → 补齐覆盖镜头 → 按布光分组**。这套表直接就是 AI 出图/出片的"派活清单"。

---

## 技法 B：AI 视频提示词的两套语序公式（讲清"套路"）

不同模型"读"提示词的顺序不同，记两套语序即可：

- **Veo / Google 系（运镜在前）**：`Cinematography + Subject + Action + Context + Style & Ambiance`（运镜手法 + 主体 + 动作 + 环境 + 风格氛围）
- **Kling 官方公式（运镜在后）**：`Subject + Subject Movement + Scene + (Camera Language + Lighting + Atmosphere)`（主体 + 主体动作 + 场景 +（运镜语言 + 光线 + 氛围））

**三条纪律（最值钱）：**

1. **2–3 个修饰符封顶，一个主导运镜**：一个镜头只给"一个景别 + 一个运镜 + 一支镜头"。这条"克制"才是所有花式运镜真正生效的原因。反面教材：堆景别词、不写焦段、超过 3 个修饰符、滥用万能词 "cinematic"。
2. **60–100 词的聚焦提示词 > 2000 字的形容词墙**。Kling 单条上限约 2500 字符，但写满没用。
3. **"模糊运镜"是画面不稳的头号原因——把口语换成行话**（直接照抄这张对照表）：
   - "Cinematic movement" → **Slow dolly-in, shallow depth of field**
   - "Make it dynamic" → **Fast whip-pan following subject**
   - "Nice angle" → **Low-angle tracking shot, 35mm**
   - "Zoom around it" → **Orbit left, smooth 180-degree arc**
   - "Add motion" → **Handheld push-in with subtle shake**
4. **光的方向比什么都改气氛**：明确写"方向 + 色温(暖/冷) + 质感(硬光/柔散)"，例如 "golden hour from camera-left" 和 "overcast diffused light" 是两种片子。模型懂真实行话：`wide shot / medium close-up / dolly in / tracking / crane / aerial / low angle / Dutch tilt / 35mm / 85mm / shallow depth of field`。

---

## 技法 C：生图"风格 + 角色"一致性的具体写法

**核心套路：先锁风格(look)，再锁角色(who)，最后才谈构图——分层引用、各管一摊。**

- **Midjourney 分层公式**：`--sref（风格参考：调色/笔触/质感） + Omni/Character Reference（角色身份：谁） + --cref（角色参考） + --cw（角色权重，控参考影响强弱） + --ar（画幅） + --s（风格化强度，越高越自由发挥） + seed（锁初始噪声，去掉最后 5% 抖动）`。v6.1 角色一致性最好，作默认。
- **风格 vs 角色要分清**：要"同一种画风"用 `--sref` / 个性化档案/情绪板；要"同一个人"用 `--cref` + Omni Reference。两者别混在一个参数里。
- **接受 85% 上限**：现技术做不到 50+ 张 100% 一致；把目标定在 85%，剩下 15% 留后期修，然后**交付**——别在一致性上无限磨。
- **专业工作流（Curious Refuge 同款思路）**：**先用 AI 生图逐镜头做"参考帧"并锁定统一视觉风格 → 再把这些帧逐个动起来**，让每个 clip 互相对得上。即"先定 look、出关键帧、再动画化"。

---

## 技法 D：首帧/尾帧关键帧工作流（把"运镜"变成可控插值）

比纯文生视频/图生视频更稳的一招——**用两张静帧夹住一个镜头**：

- **做法**：上传 Frame A（起始帧）+ Frame B（结束帧）+ 一句话描述中间运动，模型插值出中间所有帧，画面从 A 平滑变到 B。
- **导演用法**：与其赌文字"从面部慢摇到远方地平线"，不如把**特写当 Frame A、远景当 Frame B**，直接用两帧规定相机运动和人物走位(blocking)。
- **稳的关键**：两帧的**构图/光线/主体位置越接近越平滑**——让模型"插值运动"，而不是"打架式重排版"。变角色时保持景别和比例一致。
- **支持模型**：Kling（O1 首尾帧）、Wan 2.x（FLF2V）、LTX、Seedance 等。

---

## 技法 E：四大平台"方言"差异（同一镜头，不同写法）

同一个"雨中追车"，四家要喂不同结构：

- **Runway Gen 4.5**：**力—反应物理句法**，描述"力"而非"外观"（"重型老爷车高速撞混凝土护栏，物理：引擎盖向内溃缩"）；相机 token：`Camera pan left/right`、`Truck left/right`、`Dolly in/out`、`Zoom in/out`。
- **Kling 2.6**：**时间轴节拍脚本**，用 `0–4s / 4–8s` 给画面+音频打点，音画同生；对白每段 <5 秒，加语气 `(whispering) / (shouting)`。
- **Veo 3.1**：**JSON 结构化参数**（把 lighting / camera / subject / environment 拆成字段），并支持"配料式(ingredient)"角色跨镜一致。
- **Sora 2**：**因果链**——解释事件"为什么"发生（玻璃在支点上倾倒、液体表面张力），最长约 20 秒。

---

## 可复用示例提示词（英文原样）

1. **跟随追踪 + 单焦段（来自 Prompt Architects，照搬可用）**
   `Medium tracking shot from the subject's right side. Camera moves at the subject's walking speed. 35mm lens, slight handheld feel.`

2. **产品/物体环绕弧形运镜（Runway 风格，物体居中）**
   `Low angle, wide shot of a futuristic sneaker on wet asphalt. Camera: Smooth arc shot orbiting the shoe clockwise, maintaining the shoe as the central focal point.`

3. **Kling 官方公式套用（主体+动作+场景+运镜+光+氛围，60–100 词聚焦）**
   `A weathered fisherman in a yellow raincoat hauls a heavy net over the boat's edge. Storm-lit pier at dawn. Slow dolly-in, low angle, 35mm. Cold backlight, rim light through heavy rain, volumetric god rays, shallow depth of field, cinematic.`

---

## 跟谁学：大神 / 平台 / 仓库 / 频道（点名 + 链接）

- **Curious Refuge（Caleb Ward & Shelby Ward 夫妇创办）** — 全球第一所 AI 电影学校，覆盖前期到分发的完整流程，名言"输入一句提示词不会得到一部电影，讲好故事才是核心"。官网 https://curiousrefuge.com/ai-filmmaking ｜ YouTube https://www.youtube.com/@curiousrefuge
- **StudioBinder** — 分镜表/节拍表/景别角度的行业级教程库（导演拆镜思维的"圣经"）：https://www.studiobinder.com/blog/how-to-make-a-shot-list/
- **Blake Snyder · Save the Cat** — 15 拍节拍法 + 在线节拍映射工具：https://savethecat.com/beat-mapper
- **Boords** — 故事板/分镜表在线工具 + 免费模板：https://boords.com/shot-list-template
- **Prompt Architects** — Veo3/Kling 电影运镜提示词合集（30 条结构化范例）：https://prompt-architects.com/blog/25-30-cinematic-camera-prompts-for-veo3-and-kling
- **主流出片平台（按方言差异选）**：Google **Veo 3.1**、快手 **Kling 2.6/3.0**（fal.ai 上 `fal-ai/kling-video/o1`）、**Runway Gen 4.5**、OpenAI **Sora 2**；生图一致性用 **Midjourney v6.1**、**FLUX**、**Gemini 2.5 Flash Image**；首尾帧/开源用 **LTX**、**Wan 2.x**、**Seedance**。

> 工作流串起来：**Save the Cat 搭主题骨架 → StudioBinder 式分镜表（景别+角度+运镜+覆盖）→ Midjourney 先锁风格出关键帧 → 两套语序公式把每镜写成 60–100 词提示词 → 首尾帧夹住运镜 → 按平台方言喂给 Veo/Kling/Runway/Sora。**
