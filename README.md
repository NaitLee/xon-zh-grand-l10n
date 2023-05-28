English | [中文（简体字）](./README.zh_CN.md) | [中文（正體字）](./README.zh_TW.md) | [中文（香港字）](./README.zh_HK.md) | [中文（傳統字）](./README.zh_Hant.md)

# xon-zh-grand-l10n

*(Unofficial) The Grand Chinese localization for Xonotic*

## “Why do you do this?”

Yes, official way of doing Xonotic translations is via Transifex. [There is a guideline in official wiki.](https://gitlab.com/xonotic/xonotic/-/wikis/Translating)

Sure, this is for ease of collaboration and ease of management.

*But,* [this way have failed to keep Chinese translations quality at all.](https://forums.xonotic.org/showthread.php?tid=9490)

So now comes this Grand Localization repository: one piece of main translation file `common.zh_Hant.po` is kept by myself, and all other variants (`zh_CN`, `zh_HK`, `zh_TW`) are converted by [OpenCC](https://github.com/BYVoid/OpenCC), very gracefully.

## “So, how do *you* keep *your* translation quality?”

Before the translation was completed, I did the following:

- Starting with `zh_CN`, seek for *all* of the inconsistency in existing translation, do some regulation for wrong terms/grammar and correct all of them
- Play Xonotic with my own translation days after days, correct whenever I feel not ok
- Gather good parts of existing `zh_TW` translation
- Gather some Xonotic-specific term variations in `patch-twp.txt`
- For that sake, I’ve converted `zh_CN` to `zh_Hant` (OpenCC standard, [almost a superset](https://github.com/BYVoid/OpenCC/wiki/%E7%B7%A3%E7%94%B1) for all Chinese variants), checked twice for convertion consistency
- From then on, translation for all variants are done in that file, by myself and some conversion. `zh_HK` is filled from 0% to 100% in this way, after someone requesting it on Transifex.
- All variants are uploaded to Transifex service respectively (instead of using the editor) whenever translation is updated here, then went to official repository.

## “What if I want to contribute too?”

I don’t know 🙃

From todays perspective, no need to join this job — I’m watching translation progress. There are very few Chinese translation contributor these years, and number of contributors is inversely proportional to efficiency.

If matters going to change in the future, I could “pass” this repository to one, or go back to collabrative contribution.

## Files

- `0-convert.sh`: Convert `.po` files and `.md` docs to other Chinese variants
- `1-update.sh`: Update current translation file from local `xonotic-data.pk3dir`, so that new string are included

Also see [“Extended” Chinese Language Pack for game Xonotic (Unofficial)](https://github.com/NaitLee/xon-cn-ext).

## Rules

*See Chinese versions of README.*

## License

As official Xonotic game assets, GNU General Public License version 3.
