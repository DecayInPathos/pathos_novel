# Cloudyland · 云岛

> 海鸥徘徊在海崖，浪搅动沿岸。  
> 这座岛屿以终年盘桓的云雾命名——Cloudyland，云岛。

![云岛的海崖与海雾](Cloudyland/game/images/bg_the_hague_seagulls.png)

**一部使用 Ren’Py 制作的中文原创视觉小说。**

多年之后，一个远行的人再次踏上云岛。海雾、钟声与熟悉的街巷，让现实不断与记忆交叠。悬崖边的教堂、神父义兰，以及那个始终无法忘记的“你”，将他带回曾经离开的地方。

这里是否就是他的命定之地？

[开始体验](#开始体验) · [从源码运行](#从源码运行) · [项目结构](#项目结构) · [反馈](https://github.com/DecayInPathos/pathos_novel/issues)

## 关于作品

《云岛》围绕记忆、爱欲、信仰与归属展开，以第一人称独白和对话推进叙事。主人公重返故地，也再次面对那些未能结束的关系。

画面以水彩质感、粗笔触和概括化场景为主：蓝灰色的海雾、空寂的街巷，以及旧礼拜堂里昏黄的光。环境承担叙事，让未曾出现在画面中的人留在文字与记忆里。

故事中的“赫拉”是本作世界观中的原创神明，仅借用名字；她的信仰、传说与神圣契约均属于《云岛》的设定。

## 章节与进度

| 章节 | 进度 |
| --- | --- |
| 楔子 | 已有可运行脚本 |
| 第一章 · 命定之地 | 已完成了故事骨干，待完善 |
| 第二章 · 梦是梦的影子 | 穿件了CHR2.rpy，主要是关于赫拉的梦 |





## 从源码运行

1. 下载并安装 [Ren’Py SDK](https://www.renpy.org/latest.html)。
2. 克隆仓库，或通过 GitHub 的 **Code → Download ZIP** 下载后解压：

   ```bash
   git clone https://github.com/DecayInPathos/pathos_novel.git
   ```

3. 打开 Ren’Py Launcher，在偏好设置中将“项目目录”设为本地的 `pathos_novel` 文件夹。它的下一层应当是 `Cloudyland`，其中包含 `game` 文件夹。
4. 返回项目列表，选择 **Cloudyland**，点击 **启动项目 / Launch Project**。

本项目通过 Ren’Py Launcher 运行，无需单独用 Python 执行 `.rpy` 文件。

运行方式可参考 [Ren’Py 官方快速入门](https://www.renpy.org/doc/html/quickstart.html)。

## 项目结构

| 路径 | 内容 |
| --- | --- |
| [`Cloudyland/game/script.rpy`](Cloudyland/game/script.rpy) | 游戏入口与章节跳转 |
| [`Cloudyland/game/CHR/`](Cloudyland/game/CHR/) | 楔子及章节剧情脚本 |
| [`Cloudyland/game/Character.rpy`](Cloudyland/game/Character.rpy) | 角色定义 |
| [`Cloudyland/game/image.rpy`](Cloudyland/game/image.rpy) | 背景图像定义与显示尺寸 |
| [`Cloudyland/game/images/`](Cloudyland/game/images/) | 背景插图与图像素材 |
| [`Cloudyland/game/screens.rpy`](Cloudyland/game/screens.rpy) | 游戏界面 |
| [`Cloudyland/game/gui.rpy`](Cloudyland/game/gui.rpy) | 界面样式与基准分辨率 |
| [`Cloudyland/game/options.rpy`](Cloudyland/game/options.rpy) | 游戏名称、版本与构建设置 |
| [`Cloudyland-1.0-dists/`](Cloudyland-1.0-dists/) | 已有打包产物 |

## 反馈

欢迎通过 [Issues](https://github.com/DecayInPathos/pathos_novel/issues) 反馈错别字、画面问题或运行错误。

报告运行问题时，请附上操作系统、所用版本、复现步骤，以及报错文本或截图。涉及剧情的讨论请在标题中标注“剧透”。

---

*“离我而去的，逝去的，这些事情，都在我掌心摩挲良久。”*
