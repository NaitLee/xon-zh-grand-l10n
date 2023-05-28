# xon-zh-grand-l10n

（非官方）Xonotic 一统中文本地化

## “为何你要这么做？”

没错，翻译的官方途径是通过 Transifex 服务。[官方维基有相关指南。](https://gitlab.com/xonotic/xonotic/-/wikis/Translating)

也的确，官方的目的是确保合作、管理便捷有效。

*不过，*[这并没有保障中文翻译的质量。](https://forums.xonotic.org/showthread.php?tid=9490)

为此，有了一统中文本地化：我自己保留一份主要的翻译文件 `common.zh_Hant.po`，其他的版本（`zh_CN`, `zh_HK`, `zh_TW`）从 [OpenCC](https://github.com/BYVoid/OpenCC) 优雅地转换而来。

## “那*你*怎么确保*你的*翻译质量呢？”

在翻译完成之前，我做了一些事：

- 从 `zh_CN` 开始，在现有的翻译中寻找*所有*不当之处，并定下（隐）规则、加以纠正
- 日复一日地就着自己的翻译玩 Xonotic，每当发现问题就立即改正
- 从 `zh_TW` 搜集好翻译
- 把一些 Xonotic 术语变种整理到 `patch-twp.txt`
- 如此，我将 `zh_CN` 翻译转换到 `zh_Hant`（OpenCC 标准，所有中文形式的[近似全集](https://github.com/BYVoid/OpenCC/wiki/%E7%B7%A3%E7%94%B1)），并检查两遍、手动纠错
- 此后，对所有中文形式的翻译都由我在此文件完成。在 Transifex 上对 `zh_HK` 的申请通过后，其翻译亦以此方式从 0% 填到 100%
- 在翻译更新后，所有形式的中文翻译都分别上传到 Transifex 服务（而非使用编辑器），之后同步到官方仓库

## “那要是我也想贡献翻译怎么办？”

我也不知道 🙃

从现状来看，不必要参与——我经常巡视最新的翻译现况。近年来，贡献者太少，人数和效率成反比。

如将来有变动，可为另外的一位活跃贡献者“传授”此仓库，或干脆放弃此模式，众人拾柴。

## 文件

- `0-convert.sh`: 将 `.po` 文件和 `.md` 文档转换到其他中文版本
- `1-update.sh`: 从本地的 `xonotic-data.pk3dir` 文件夹更新翻译文件，获取新字符串

另见 [Xonotic “扩展”汉化包（非官方）](https://github.com/NaitLee/xon-cn-ext)。

## 翻译规则

- 术语正确、统一、分明

如，“cells”在游戏中作为 Electro 等电气主题武器的弹药，应当翻译为“电池”而非“细胞”。

再如，“capture”在游戏中的用法分为“capture flag”和“capture control point”，不能一概而论、混为一谈。需视情况译为“夺取”或“占领”。

- 语法、语序准确，但不失灵活

如，要把原因放在句子主干前。“之所以……是因为……”一样的话出现在激烈的游戏过程中是要挨打的。

再如，可视语境把被动句变为主动句。避免晦涩的“翻译腔”。

- 留意标点、符号、占位格式

可从翻译文件观察它们的具体形式。

官方文档有关于[占位符](https://gitlab.com/xonotic/xonotic/-/wikis/List-of-translation-placeholders)和[颜色码](https://gitlab.com/xonotic/xonotic/-/wikis/List-of-color-codes)的具体解释。不要落下它们。

- 留意前缀

[前缀](https://gitlab.com/xonotic/xonotic/-/wikis/List-of-translation-prefixes)明确告诉了字符串的上下文。

比如，`SCO^` 前缀表示此字符串是记分板表头，那么此字符串的翻译应当尽可能短。

建议在翻译结果中去掉前缀。

- 负责任

是人都会犯错。当发现自己或别人的不当翻译时，请改正，必要时可讨论。

## 许可

同 Xonotic 官方游戏资源，使用 GNU 通用公共许可证第 3 版。
