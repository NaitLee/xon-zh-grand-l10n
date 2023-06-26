#!/bin/sh
xonotic_data="/mnt/data/@/git-repo/xonotic/data/xonotic-data.pk3dir/"
cp common.zh_Hant.po common.zh_Hant.po.old
msgcat common.zh_Hant.po "$xonotic_data/common.pot" | python3 postprocess.py >>new.po
mv new.po common.zh_Hant.po
