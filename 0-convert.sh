#!/bin/sh
for lang in zh_CN zh_HK zh_TW; do {
    echo $lang
    opencc -c $lang.json -i common.zh_Hant.po >common.$lang.po
    opencc -c $lang.json -i README.zh_Hant.md >README.$lang.md
}; done
