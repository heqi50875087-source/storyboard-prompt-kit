# AI 视频提示词 · 导演级写法技法卡（Veo / Sora / Kling / Runway）

> 一句话:把"提示词"当**分镜表**写——一镜=一个景别+一个运镜+一支镜头,再叠光线、调色、节拍。少即是多,术语要"行话",动作要"可数"。

## 来源
- awesome-ai-video-prompts（聚合 Veo/Sora/Runway/Pika/Kling 官方指南与模板的开源库）：https://github.com/geekjourneyx/awesome-ai-video-prompts
- OpenAI 官方 Sora 2 Prompting Guide（Cookbook）：https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide
- Prompt Architects《30 Cinematic Camera Prompts for Veo 3 & Kling》：https://prompt-architects.com/blog/25-30-cinematic-camera-prompts-for-veo3-and-kling
- LzyPrompt《AI Video Camera Movement Prompts — 2026 Director's Cheatsheet》：https://lzyprompt.com/blog/ai-video-camera-movement-prompts/

---

## 一、结构公式（先定语序,模型才不打架）
不同模型"读"提示词的顺序不同,语序错了就抓不到重点:

- **通用万能序**：`主体 Subject → 动作 Action → 运镜 Camera → 镜头/景别 Lens/Framing → 光线/风格 Lighting/Style`
- **Veo 3「镜头优先」**：`Cinematography（机位/运镜）+ Subject + Action + Context + Style & Ambiance` —— 把摄影机放第一句。
- **Kling「镜头垫后」**：`Subject + Environment + Action + Lighting + Style + Camera Movement` —— 运镜写在最后,用 `Camera:` 起一句单列。
- **Sora 2「分层叙事」**：把信息**分块**写 —— ①散文式场景描述（人物/服装/环境/天气）②Cinematography（景别+情绪）③Actions（动作节拍）④Dialogue（简短台词）。官方强调"不是死配方",**适度留白**反而激发模型创造力。

## 二、一镜三件套 + 修饰封顶(最硬的一条)
- 每个镜头只给 **1 个景别 + 1 个主导运镜 + 1 支镜头**(lens)。
- 实测 200 条 prompt：**相机修饰词 2–3 个最优,超过 3 个画面就"和稀泥"**(指令互相打架)。一个 clip 只配一个主运镜。
- **用真实电影术语,别用大白话**：写 `dolly shot` 而不是 "camera moves forward"——模型能解析行话,会连带给出那个运镜的情绪与节奏。**禁用空泛词 "cinematic"**,用具体技法代替。

## 三、景别 + 角度词汇(框定构图)
- 景别：`wide establishing shot` / `medium close-up` / `aerial wide shot` / `extreme close-up`。
- 角度：`eye level` / `low angle` / `high angle` / `slight angle from behind` / `slight downward angle`。
- 需要不动时**显式声明**：`static shot` / `locked-off camera` / `tripod-mounted, no movement`(不写,模型会自作主张乱推)。

## 四、八大运镜词 + 速度档(可直接抄进分镜)
1. **Static 固定**：locked-off / tripod-mounted, no movement
2. **Pan 横摇**：slow pan left across the [environment]
3. **Tilt 纵摇**：tilt up from [foreground] to [background]
4. **Dolly 推拉(整机进退)**：dolly in slowly toward [subject]
5. **Tracking 跟移(横向平移)**：tracking shot, camera follows [subject] from the side
6. **Crane 升降(摇臂)**：crane up from low angle to high angle
7. **Push-in / Pull-out 情绪推近/拉远**：slow push-in toward [subject's face], emotional tension
8. **Orbit / Arc 环绕**：orbit around [subject], 180 degree arc

**速度档(慢→快,慢=最电影感的默认)**：imperceptible → slow → steady/measured → smooth/fluid → quick → whip。

**多段运镜**：Sora 2 / Veo 3.1 支持一镜内变招——`"Static for first 2 seconds, then slow dolly-in toward [subject]"`、`"Wide shot, then crane down to eye level"`；**Kling / Runway 偏好单一运镜**,复杂序列拆成多次生成再后期拼。

## 五、动作要"可数"(节拍化,杀掉模糊)
- 用具体名词+动作动词替换模糊词：把 "walks across" 写成
  `"Actor takes four steps to the window, pauses, and pulls the curtain in the final second"`；
  把 "moves quickly" 写成 `"Cyclist pedals three times, brakes, and stops at crosswalk"`。
- 给**秒数/拍数**,模型才能对齐时间轴与节奏。

## 六、光线 & 调色(分层 + 颜色锚点)
- 别写 "brightly lit room"。用**分层光**：`"soft window light with warm lamp fill, cool rim from hallway"`(主光+补光+轮廓光)。
- 给 **3–5 个颜色锚点**：`amber, cream, walnut brown` / `muted teal palette`，统一片子色调。

## 七、质感 / VFX(把"胶片味"说成参数)
- 引用真实器材与镜头：`shot on ARRI Alexa`、`anamorphic lens`、`85mm portrait lens`、`shallow depth of field f/1.4`。
- 质感词：`cinematic film grain`、`low fog`、`realistic film style`、`golden hour`。这些比 "VFX"、"特效感" 更可控。

## 八、节奏 / 台词 / 音频(原生音轨别浪费)
- 台词**简短自然**,按时长配量：4 秒 clip 给 1–2 句,8 秒可更多;多角色**一致标注 speaker**。
- 即使静默镜头也加一句**节奏音效线索**：`"distant traffic hiss"`——给画面定脉搏。

## 九、模型差异(同一分镜,改写口吻)
- **Sora 2**：吃**叙事/描述性**,讲故事而非堆参数;善用 `"the camera reveals / we discover / the scene transforms"`,加情绪词 `intimate / epic / whimsical`;原生音频强。
- **Veo 3.1**：吃**技术精确**,引用相机系统、镜头特性、精确光线;镜头优先语序。
- **Kling**：camera-last 语序,有多镜头 storyboard 模式;一句一运镜。
- **Runway Gen-4**：图生视频最强全能,参考图 + 相机控制 + 角色一致性好,适合定角色后批量出镜。

## 十、避坑清单
- ✗ 混用景别词("wide shot close-up zoom")  ✗ 省略 lens  ✗ 修饰词 >3
- ✗ 该静止不写 static  ✗ 用空泛 "cinematic"  ✗ 运镜过快→主体变形
- ✗ 主体运动与相机运动互相抵消(破坏时间连贯)

---

## 可复用示例提示词(英文原样)

**1) Veo 3 · 镜头优先(推镜+定调)**
```
Slow dolly push from a medium shot to a close-up, 35mm lens. A weathered fisherman mends a net on a wooden dock. Cold morning light, low fog over grey water, muted teal palette.
```

**2) Kling · 镜头垫后(同场景,语序调换)**
```
A weathered fisherman mends a net on a wooden dock. Cold morning, low fog over grey water, muted teal palette, realistic film style. Camera: slow dolly push from medium shot to close-up.
```

**3) 通用万能序 · 跟移 + 黄金时刻**
```
A surfer paddling out through the lineup, slow tracking shot from the side, low angle just above the water, golden hour lighting, cinematic film grain.
```
