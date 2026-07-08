# AI 影像创作技法卡 · 电影级提示词公式 + 角色一致性 + 跟谁学(2026)

> 调研主题:best AI filmmaking creators / cinematic AI video / Higgsfield 提示词专家。
> 关于「HixBuild」:全网检索**查无此人/此物**,极可能是 **Higgsfield(希格斯场)** 的误拼,本卡按 Higgsfield 生态展开,请勿被错名误导。

## 来源链接(真实可查)
- GitHub 提示词技能库(MCSLA/Soul ID/DISCIPLINE 全公式):https://github.com/OSideMedia/higgsfield-ai-prompt-skill
- Higgsfield 官方 Soul ID 角色一致性:https://higgsfield.ai/blog/Soul-ID-AI-Character-Consistency
- Higgsfield 官方 Popcorn & Recast 提示词指南:https://higgsfield.ai/blog/Prompt-Guide-to-Cinematic-AI-Videos
- 2026 电影级提示词专家手册(8 点 Shot Grammar):https://www.truefan.ai/blogs/cinematic-ai-video-prompts-2026
- 分类型 50+ 电影提示词范例(含选型路由):https://www.imagine.art/blogs/ai-film-prompts-guide

---

## 一、三套「能直接套」的提示词公式

### 公式 A:MCSLA 五层结构(Higgsfield / Kling,最省脑)
按**固定顺序**逐层填空,模型不用猜:

| 层 | 含义 | 写法示例 |
|---|---|---|
| **M** Model 模型 | 指定底模 | `Kling 3.0` |
| **C** Camera 运镜 | 镜头运动 | `FPV drone weaving through the alley` |
| **S** Subject 主体 | 人物/对象 | `A woman in a tactical jacket` |
| **L** Look 风格 | 影调+画幅 | `Cinematic, cold blue shadows, 16:9` |
| **A** Action 动作 | 主体动作 | `She sprints, slides under a gate` |

> 铁律(来自该库的 DISCIPLINE 框架):**Identity vs. Motion 分离**——人物身份用 Soul ID 锁死,**运镜/时间类动作只写进视频提示词**(交给懂时间的 Veo/Sora/Kling),不要混在一句里。

### 公式 B:8 点 Shot Grammar(电影感最强,逐项给齐)
缺一项画面就「塌」一档,顺序即提示词顺序:
1. **Subject & Action** 主体+具体物理动作
2. **Emotional Energy** 表演情绪(如 micro-expressions of relief)
3. **Camera Optics** 镜头(35mm anamorphic / 85mm prime、景深、变焦)
4. **Motion** 运镜+走位(dolly-in / crane / parallax)
5. **Lighting Physics** 布光(主/补/轮廓光、色温、体积雾尘)
6. **Style & Color Science** 胶片/LUT(如 Teal-and-Orange)
7. **Audio Targets** 声音(环境底噪、foley、卡点)
8. **Continuity Constraints** 连续性锁定(服装、道具、时间 token)

### 公式 C:4 要素极简框架(imagine.art,新手友好)
`镜头类型+机位 → 布光语言(如 Rembrandt lighting) → 有动机的运镜 → 氛围与质感(颗粒/镜头/色温/画幅)`
**选型路由**:剧情/爱情/纪录 → **Seedance 2.0**;动作/黑色/恐怖/科幻 → **Kling 3.0 Pro**;史诗大场面 → **Veo 3.1**。

---

## 二、角色一致性:Soul ID 工作流(同一张脸跨所有镜头)
1. **喂图**:上传**20+ 张**同一人照片;光线统一、多角度露脸;**至少 1 张全身**(校准身材比例);用近 4-5 个月的近照;**忌**墨镜/重阴影/裁切脸。
2. **训练**:约 **3-5 分钟**出一个身份层。
3. **命名**:给角色起名,后续从 **Character 标签**调用。
4. **出片**:**预设优于手写提示词**(Presets beat freehand prompting)——Soul 2.0 内置 20+ 风格预设(Warm Ambient / Retro BW / Y2K Street…),换风格但脸不变。
5. **偷风格**:用 **Image Reference / 「Higgsfield Steal」浏览器扩展**——抓任意网图的风格/光/构图,直接套到你的 Soul ID 角色上,一个字都不用写。

> **单图多镜(Multi-Shot)做整片**:Kling 3.0 上传**一张起始图**→点 Multi-cam →逐镜设时长、只描述「每个镜头的差异」,即可让角色/场景在整部短片里保持一致(Dave Clark 的短片《MIRA》全片每个镜头都来自同一张起始图)。

---

## 三、可复用示例提示词(英文原样,直接粘)

**① MCSLA 组装(动作/谍战)**
```
Kling 3.0; FPV drone weaving through the alley; a woman in a tactical jacket; cinematic, cold blue shadows, 16:9; she sprints, slides under a gate.
```

**② 8 点 Shot Grammar(纪录写实)**
```
A Mumbai Dabbawala cycles through monsoon-soaked lanes at blue hour; 35mm anamorphic lens with shallow DoF; slow dolly-in with slight parallax; sodium-vapor rim lighting + soft key 5600K; documentary realism style, light drizzle foley with bicycle bell chime; wearing a white Gandhi topi and Nehru jacket.
```

**③ 科幻史诗(用 Veo 3.1)**
```
Ultra-wide establishing shot. A massive spacecraft, miles long, descends through cloud cover over a city — the ship is larger than the skyline. Storm-lit — lightning illuminates the ship's underside.
```

**④ 黑色电影(用 Kling 3.0 Pro)**
```
Medium shot, harsh overhead practical light cutting the frame diagonally. A man in a dark coat, single chair across from an empty one. The light creates one harsh highlight on his cheekbone — everything else is deep shadow.
```

---

## 四、跟谁学:大神 / 频道 / 仓库(点名 + 链接)
- **Curious Refuge**(创始人 Caleb Ward)— 全球第一所 AI 电影学校,系统课最权威。YouTube https://www.youtube.com/@curiousrefuge · 官网 https://curiousrefuge.com
- **Theoretically Media**(Tim Simmons)— 新工具/工作流「真上手实测」,跟得上版本。YouTube https://www.youtube.com/channel/UC9Ryt3XOGYBoAJVsBHNGDzA · X https://x.com/TheoMediaAI
- **PJ Accetturo(PJ Ace)**— 病毒级 AI 广告之王(Veo 3 制作 Kalshi 广告 48h 破 1800 万曝光),擅长 ChatGPT/Gemini/Midjourney 写脚本+排 shot list。X https://x.com/pjaccetturo
- **Dave Clark(@Diesol)**— 单图多镜叙事代表(短片《MIRA》),Kling/Veo 实战派。X https://x.com/diesol
- **MattVidPro AI** — AI 工具拆解科普。YouTube https://www.youtube.com/channel/UC5Wz4fFacYuON6IKbhSa7Zw
- **AI Andy(Andy Hafell)** — 新工具上手教程。YouTube https://www.youtube.com/@TheAIAndy
- **Higgsfield AI(官方)** — 平台+提示词指南源头。YouTube https://www.youtube.com/@HiggsfieldAI · 官网 https://higgsfield.ai
- **GitHub:OSideMedia/higgsfield-ai-prompt-skill** — MCSLA、Soul ID、Seedance 2.0 六模式、Kling 3.0 运镜、DISCIPLINE、17 套模板,可当 Claude 技能直接装。https://github.com/OSideMedia/higgsfield-ai-prompt-skill

---

## 一句话上手
**用 Soul ID 锁脸(20+ 张照片)→ 按 MCSLA 或 8 点 Shot Grammar 写提示词 → 身份归身份、运镜归视频模型 → 按题材选 Seedance/Kling/Veo → 单图多镜串成片。**