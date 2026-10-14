#!/usr/bin/env bash
# Rebuild every app and refresh the site folder.
set -e
cd "$(dirname "$0")"
python3 dump.py maths   part1,part2,part3,ext_maths,ext2_maths
python3 dump.py english eng1,eng2,eng3,ext_eng,ext2_eng
python3 dump.py science sci1,sci2,sci3,ext_sci,ext2_sci
python3 dump.py social  sst1,sst2,sst3,ext_sst,ext2_sst
for s in maths english science social; do python3 build_subject.py $s; done
python3 build_hub.py
python3 make_site.py
echo "Done. Commit and push, or drag the site folder to Netlify."
