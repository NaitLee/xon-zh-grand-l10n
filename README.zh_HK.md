# xon-zh-grand-l10n

（非官方）Xonotic 一統中文本地化

## “為何你要這麼做？”

沒錯，翻譯的官方途徑是通過 Transifex 服務。[官方維基有相關指南。](https://gitlab.com/xonotic/xonotic/-/wikis/Translating)

也的確，官方的目的是確保合作、管理便捷有效。

*不過，*[這並沒有保障中文翻譯的質量。](https://forums.xonotic.org/showthread.php?tid=9490)

為此，有了一統中文本地化：我自己保留一份主要的翻譯文件 `common.zh_Hant.po`，其他的版本（`zh_CN`, `zh_HK`, `zh_TW`）從 [OpenCC](https://github.com/BYVoid/OpenCC) 優雅地轉換而來。

## “那*你*怎麼確保*你的*翻譯質量呢？”

在翻譯完成之前，我做了一些事：

- 從 `zh_CN` 開始，在現有的翻譯中尋找*所有*不當之處，並定下（隱）規則、加以糾正
- 日復一日地就着自己的翻譯玩 Xonotic，每當發現問題就立即改正
- 從 `zh_TW` 蒐集好翻譯
- 把一些 Xonotic 術語變種整理到 `patch-twp.txt`
- 如此，我將 `zh_CN` 翻譯轉換到 `zh_Hant`（OpenCC 標準，所有中文形式的[近似全集](https://github.com/BYVoid/OpenCC/wiki/%E7%B7%A3%E7%94%B1)），並檢查兩遍、手動糾錯
- 此後，對所有中文形式的翻譯都由我在此文件完成。在 Transifex 上對 `zh_HK` 的申請通過後，其翻譯亦以此方式從 0% 填到 100%
- 在翻譯更新後，所有形式的中文翻譯都分別上傳到 Transifex 服務（而非使用編輯器），之後同步到官方倉庫

## “那要是我也想貢獻翻譯怎麼辦？”

我也不知道 🙃

從現狀來看，不必要參與——我經常巡視最新的翻譯現況。近年來，貢獻者太少，人數和效率成反比。

如將來有變動，可為另外的一位活躍貢獻者“傳授”此倉庫，或乾脆放棄此模式，眾人拾柴。

## 文件

- `0-convert.sh`: 將 `.po` 文件和 `.md` 文檔轉換到其他中文版本
- `1-update.sh`: 從本地的 `xonotic-data.pk3dir` 文件夾更新翻譯文件，獲取新字符串

另見 [Xonotic “擴展”漢化包（非官方）](https://github.com/NaitLee/xon-cn-ext)。

## 翻譯規則

- 術語正確、統一、分明

如，“cells”在遊戲中作為 Electro 等電氣主題武器的彈藥，應當翻譯為“電池”而非“細胞”。

再如，“capture”在遊戲中的用法分為“capture flag”和“capture control point”，不能一概而論、混為一談。需視情況譯為“奪取”或“佔領”。

- 語法、語序準確，但不失靈活

如，要把原因放在句子主幹前。“之所以……是因為……”一樣的話出現在激烈的遊戲過程中是要捱打的。

再如，可視語境把被動句變為主動句。避免晦澀的“翻譯腔”。

- 留意標點、符號、佔位格式

可從翻譯文件觀察它們的具體形式。

官方文檔有關於[佔位符](https://gitlab.com/xonotic/xonotic/-/wikis/List-of-translation-placeholders)和[顏色碼](https://gitlab.com/xonotic/xonotic/-/wikis/List-of-color-codes)的具體解釋。不要落下它們。

- 留意前綴

[前綴](https://gitlab.com/xonotic/xonotic/-/wikis/List-of-translation-prefixes)明確告訴了字符串的上下文。

比如，`SCO^` 前綴表示此字符串是記分板表頭，那麼此字符串的翻譯應當儘可能短。

建議在翻譯結果中去掉前綴。

- 負責任

是人都會犯錯。當發現自己或別人的不當翻譯時，請改正，必要時可討論。

## 許可

同 Xonotic 官方遊戲資源，使用 GNU 通用公共許可證第 3 版。
