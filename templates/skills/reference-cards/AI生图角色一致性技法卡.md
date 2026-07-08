# AI 生图技法卡 · 风格一致性 / 角色一致性 / 剧本→分镜导演流程

> 适用：童话节、童年档案馆、馆员说、绘本插画、儿童阅读推广短片等需要"同一个角色跨多张图/多镜头不崩脸"的场景。
> 三大主力工具：**Midjourney**（sref/cref/oref）、**Nano Banana / Gemini**（Google 即 Nano Banana Pro）、**即梦 Seedream 4.0**（字节）。

## 一句话心法（所有工具通用）

**先建"角色圣经"，再每镜复用。** 一致性 = 同一张参考图 + 同一段不变的角色描述 + 每镜只改"动作/环境/景别/情绪"。崩脸的根因永远是"每次重新描述角色"——把角色描述当常量复制粘贴，把场景当变量改。

---

## 核心技法（分平台讲清"公式/套路"）

### A. Midjourney —— 参数三件套（注意版本！）

- **`--sref`（风格参考）**：只搬"风格"——配色、媒介、笔触、光影，不搬人/物。配 `--sv 1/2/3/4` 切风格算法版本（sv1/sv3 更"氛围感"，sv2/sv4 更"精准")。多张图可叠加做风格融合。
- **`--cref`（角色参考）= 旧版 V6 用**：搬人物核心特征（脸/发/配色）。配 `--cw 0–100` 调强度：`--cw 100`（默认）连脸+发+衣一起搬；`--cw 0` **只搬脸**（适合换装/换发型）。⚠️ **V7 已不支持 `--cref`，会报错或被忽略。**
- **`--oref`（Omni Reference）= V7 现役做法**：通吃人/物/载具/生物，把参考图里的视觉元素"嵌入"新图。配 `--ow 1–1000`（默认 100）：`--ow 25` 用于换风格（如真人转动漫），`--ow 400` 用于死保脸/保服装；一般别超过 400 否则结果乱。⚠️ 只能传 1 张参考图、且必须是已联网的图片 URL；耗 2 倍 GPU 时长。
- **套路**：先用一张**正面、清晰、头肩特写**当参考 → 再用 `--ow`/`--cw` 微调"搬多少"。`--sref` 与角色参考可同时用（一个锁风格、一个锁人）。

### B. Nano Banana / Gemini（Nano Banana Pro）—— 公式 + 锚定词 + 多图分工

- **文生图公式**：`[主体] + [动作] + [地点/语境] + [构图/景别] + [风格]`。
- **带参考图（多模态）公式**：`[参考图] + [关系指令] + [新场景]`——这是保角色/换场景的主力。
- **一致性锚定词（必加）**：`same character` / `maintain facial features` / `preserve proportions` / `use this character as reference, keep identity`。换场景时用"定点编辑"而非整张重画：`change background to forest`、`change clothing to winter coat`，主体保持不动。
- **多图分工法（最实用）**：可传 6–14 张互不相关的图，明确每张的角色分工——`Use Image A for the character's pose, Image B for the art style, and Image C for the background environment`。
- **首帧定调省 token**：第一条 prompt 把角色（年龄/脸/发/配色/服装/风格）写全，同一会话后续只写"动作+情绪"，模型自动复用稳定的角色表示。
- **360° 角色表**：先让它出 2–3 张"正面/左/右/背面"角色立绘，给足模型对角色的完整理解，再开始正式出分镜。
- **JSON 提示法（进阶·一致性最强）**：用结构化 JSON 强制模型把"角色/光影/构图"各装各的盒子，防"概念串味"。实测 JSON 角色漂移 <3%，自然语言可漂 20%。做"角色圣经"JSON 反复复用即可锁人（见下方示例 3）。

### C. 即梦 Seedream 4.0 —— 编辑公式 + 图片索引 + 组图

- **编辑公式**：`变化动作 + 变化对象 + 变化特征`，例 "把骑士的头盔换成金色的"。生图分两层写：**内容层**（主体+行为+环境）+ **美学层**（风格+色彩+光影+构图）。
- **多图参考（最多 10 张）+ 显式图片索引**：直接在 prompt 里点名第几张图干什么——"把图1的人物放到图2的背景里，并参考图3的风格生成"。
- **实操配比**：一次别堆太多，**3–5 张**最稳（1–2 张锁角色、1–2 张定场景/风格），图太多模型会懵。
- **组图（一致性序列）**：一次最多出 9 张"角色一致、风格统一"的关联图——天然适合**连环画/分镜/绘本/表情包/IP 周边**。
- **素材文件夹法（做长片）**：把素材按 `人物参考图 / 场景风格图 / 镜头参考 / 音频 / 提示词` 分目录管理，再喂模型。

---

## 剧本 / 主题 → 分镜：导演工作流（5 步，工具无关）

1. **定角色圣经**：写死角色描述（脸型/眼/发/服装/配色/画风），先出"正面清晰头像 + 360° 角色表"，选一张当**唯一参考图**。
2. **锁参考 + 锁种子**：每个镜头都复用同一张参考图 + 同一段角色描述（Midjourney 用 `--oref`/`--sref`；Gemini/即梦 上传同一参考图 + 锚定词；能锁 `seed` 就锁）。
3. **剧本拆镜**：把脚本切成镜头清单，每镜**只改 4 个变量**——动作、环境、景别（特写/中景/全景）、情绪；**角色描述整段照抄不动**。
4. **分镜出图 + 一致性校验**：批量出图后逐镜核对"脸/发/服装"是否一致，崩的单独重抽或用"定点编辑"修。
5. **进视频**：用"图生视频"延展（即梦 Seedance / Veo），或在 ComfyUI 里用 ControlNet 锁姿势 + Qwen Image Edit 迭代场景，再 WAN 出动态。

---

## 可复用示例提示词（英文原样，直接拿去改）

**示例 1 · Nano Banana / Gemini：锚定角色 + 换场景**
```
Using the uploaded reference, keep the SAME character — maintain identical facial
features, hairstyle, and body proportions. Now place her in a snowy bamboo forest
at golden hour, wearing a red winter coat, holding a paper lantern.
Medium full shot, eye level, soft cinematic lighting, 16:9.
```

**示例 2 · Midjourney V7：Omni Reference 保角色出分镜**
```
a young female knight standing in a misty bamboo forest at dawn, holding a sword,
cinematic morning light, film still --oref https://YOUR_IMAGE_URL.jpg --ow 250 --ar 16:9 --v 7
```

**示例 3 · "角色圣经" JSON（Nano Banana Pro，跨镜锁人，复制后只改 shot 段）**
```json
{
  "character_bible": {
    "name": "Mei",
    "age": "around 10",
    "face": "round face, large brown almond eyes, small nose, light freckles",
    "hair": "shoulder-length black hair with straight bangs",
    "outfit": "mustard-yellow raincoat, blue rubber boots",
    "style": "soft 3D Pixar-like render, warm color palette",
    "consistency": "keep identical face, hair and proportions in every shot"
  },
  "shot": {
    "action": "jumping over a puddle, laughing",
    "scene": "rainy city street at dusk, neon reflections on wet ground",
    "camera": "medium shot, eye level, 35mm lens, shallow depth of field",
    "aspect_ratio": "16:9"
  }
}
```

**示例 4 · 即梦 Seedream：多图索引合成（中文直接喂）**
```
把图1的人物放进图2的背景里,穿上图3的服装,保持人物的脸型与身体比例一致;
水墨淡彩风格,暖色调,竖屏 9:16 壁纸,柔和电影光。
```

---

## 跟谁学（大神 / 平台 / 仓库 / 频道，点名给链接）

- **Nick St. Pierre（@nickfloats）** —— Midjourney 一致性角色头号实战派，cref/cw/oref 测试帖最权威。课程 [Midjourney for Creatives (Maven)](https://maven.com/nick-st-pierre/midjourney-for-creatives) · [X 主页](https://twitter.com/nickfloats)
- **Curious Refuge**（Shelby & Caleb Ward）—— 全球第一所 AI 电影学校，剧本→分镜→成片全流程。[官网](https://curiousrefuge.com/) · [YouTube @curiousrefuge](https://www.youtube.com/@curiousrefuge)
- **Theoretically Media（Tim）** —— 一线 AI 视频/图像工具横评，"哪个工具干哪个活"讲得最清楚。[官网](https://theoreticallymedia.com/)
- **Google 官方** —— [Nano Banana 终极提示词指南](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) · [Nano Banana Pro 提示词技巧](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/)
- **GitHub 仓库** —— [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro)（Nano Banana Pro 精选 prompt）· [JSON 结构化 prompt schema gist](https://gist.github.com/alexewerlof/1d13401a7647339469141dc2960e66a9)
- **ComfyUI 分镜流** —— [从剧本到画面·宫崎骏风分镜教程](https://comfyui.org/en/miyazaki-style-storyboard-guide)

## 来源链接（核心参考）

- Midjourney 官方文档：[Character Reference (--cref)](https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference) · [Style Reference (--sref)](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference) · [Omni Reference (--oref)](https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference)
- Nano Banana Pro 角色一致性：[prompting.systems 指南](https://prompting.systems/blog/nano-banana-pro-character-consistency-guide)
- 即梦 Seedream 4.0：[即梦4.0提示词手册（苏米客）](https://www.xmsumi.com/detail/1550) · [Seedream 4.0 深度报告（知乎）](https://zhuanlan.zhihu.com/p/1951967614642401917)
