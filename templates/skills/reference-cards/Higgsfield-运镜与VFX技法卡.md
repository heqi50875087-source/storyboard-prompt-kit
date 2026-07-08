# Higgsfield AI 运镜与VFX 提示词技法卡

> 提炼自 Higgsfield 官方运镜指南与社区高手实操,聚焦"预设(运镜)+提示词(表演)"双轨写法,直接拿来写分镜。

## 来源
- Higgsfield 官方 · WAN 相机控制指南:https://higgsfield.ai/blog/WAN-AI-Camera-Control-Your-Guide-to-Cinematic-Motion
- Higgsfield 官方 · 电影感视频提示词指南:https://higgsfield.ai/blog/Prompt-Guide-to-Cinematic-AI-Videos
- Higgsfield 官方 · Camera Controls 预设库(50+):https://higgsfield.ai/camera-controls
- Techpresso · 30 Best Higgsfield Prompts(2026):https://academy.techpresso.co/prompts/higgsfield-prompts
- Kolbo.AI · Higgsfield Suite 100+ 预设拆解:https://kolbo.ai/blog/higgsfield-suite-100-camera-presets

---

## 一、黄金公式(背下来直接套)
**主体 + 场景 + 单一运镜/VFX + 光线 + 情绪( + 镜头规格 + 画面比例)**

官方原句模板:
> "A cinematic shot of [谁,带年龄/外貌/表情/服装] in/at [具体地点+环境细节], [一个运镜动词] as [光线如何打在主体上], [情绪/调色], [镜头/画幅技术参数]."

要点:**descriptive specificity > brevity**(宁可写长写细,也别图省事;技术细节可用括号补充)。

## 二、五条硬规则(高手与小白的分水岭)
1. **一条 clip 只给一个运镜**——铁律。两个运镜塞进一条 prompt 几乎必崩(画面抖、主体糊)。要复杂运动就拆成多条 clip 再剪。
2. **预设管"镜头怎么动",提示词管"主体怎么演"**——在 App 里先选匹配的运镜预设(它会锁住主体),prompt 只描述运动期间发生什么(表演/环境揭示),别再用文字重复描述镜头。
3. **输入图要匹配运镜类型**:居中人物/物体 → 适合 Orbit / Dolly / Zoom;宽幅风景 → 适合 FPV 无人机 / Handheld;脸部或物体特写 → 适合 POV / Snorricam / Through-Object。
4. **招牌运镜一段只放一个"重拍"**:Crash Zoom 这类爆发性运镜,一条 clip 只用一次,滥用就失去冲击力。
5. **声音原生同步**:对白/歌词/音效直接写进 prompt(如 the singer performs the chorus…),Higgsfield 会做音画同步,无需另配。

## 三、运镜预设速查(按用途分类)
- **基础铺陈**:Dolly In(推近强调)/ Dolly Out(拉远揭示)/ Static / Tracking / Boom / Crane Up·Down
- **冲击爆点**:Crash Zoom In·Out(急推/急拉)/ Whip Pan(甩镜转场)/ Bullet Time(子弹时间环绕)
- **沉浸真实感**:Handheld(手持)/ Car Grip(车载)/ FPV Drone(穿越机环绕)/ Hyperlapse
- **极端 POV**:Eyes In / Mouth In / Through Object In·Out(穿物体,如穿过钥匙孔)/ Snorricam(绑身镜)
- **氛围/构图**:360 Orbit(环绕)/ Dutch Angle(斜角失衡)/ Focus Change(焦点转移)/ Pan·Dolly Left·Right

## 四、招牌 VFX/运镜的写法细节
- **Bullet Time**:写明几颗"悬浮粒子"(droplets / sparks / debris)让"时间冻结"被肉眼看见,环绕弧线才有 Matrix 味。
- **Crash Zoom**:配 motion-blurred zoom streaks + 一个被"砸向镜头"的元素(shockwave / debris blasting toward camera),冲击感拉满。
- **Through Object**:把"穿过的那个物体"写具体(through a keyhole into a candlelit room),揭示落点要明确。
- **节奏转折**:用"前 N 秒铺垫 + Suddenly 突变"制造戏剧弧光(她平静开车 → Suddenly turns her head → eyes widen in silent horror)。

## 五、光线 / 调色 / 镜头词库(直接抄进 prompt)
- **光线**:volumetric god rays、hard directional key light、soft studio key light、sunlight flickering across her face、lit by passing streetlights
- **调色**:moody teal-and-orange grade、synthwave palette、desaturated / muted yellow-green、high contrast blockbuster grade
- **镜头质感**:anamorphic lens flares、shallow depth of field、24fps film look、film grain、motion blur、4k commercial look
- **镜头规格**:35mm / 50mm / 75mm(越长越亲密)、eye-level framing、close-up / wide / medium
- **导演参考**:加一句 "inspired by Roger Deakins" 之类锁定打光与质感方向。

## 六、竖屏/带货钩子技法
- 写 **Vertical 9:16 POV**,首词就来个 crash-zoom-in 做 **scroll-stopping hook**;配 bright punchy lighting + fast-paced creator energy,标注 optimized for TikTok and Reels。

---

## 七、可复用示例提示词(英文原样)

**1) 慢推揭示 · Slow Dolly-In Reveal(预设选 Dolly In)**
```
Cinematic slow dolly-in on [SUBJECT] standing in a fog-filled warehouse, camera glides forward at a steady creep, shallow depth of field with the background softening as we approach, volumetric god rays cutting through haze, moody teal-and-orange color grade, anamorphic lens flares, 24fps film look, dramatic and tense mood
```

**2) 爆发急推 · Crash Zoom Impact(预设选 Crash Zoom In,一段一次)**
```
Explosive crash zoom snapping from a wide shot to an extreme close-up on [SUBJECT]'s eyes as a shockwave hits, debris and dust blasting toward camera, hard directional key light, motion-blurred zoom streaks, intense and shocking mood, blockbuster action grade, high contrast
```

**3) 夜驾氛围 · Neon Night-Drive(预设选 Tracking / Car Grip)**
```
Cinematic music-video shot from inside a car at night driving through a neon city, [SUBJECT] in the passenger seat lit by passing streetlights, reflections streaking across the window, moody synthwave color palette, smooth tracking motion, nostalgic and atmospheric, anamorphic lens flares
```
