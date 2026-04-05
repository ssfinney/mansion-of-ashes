# Export Notes

The repository keeps the Twee file in `story/` as the source of truth. Exported playable builds belong in `build/`.

## Building with Tweego (local toolchain)

`scripts/build-story.sh` expects a Tweego binary at `.tools/tweego/tweego` and
SugarCube 2 format files in `.storyformats/`. These are not committed to the repo.

**Install steps:**

1. Download Tweego from https://www.motoslave.net/tweego/
2. Place the binary at `.tools/tweego/tweego` and `chmod +x` it
3. Download SugarCube 2 from https://www.motoslave.net/sugarcube/2/
4. Unzip it into `.storyformats/sugarcube-2/`

Then run:

```bash
scripts/build-story.sh
# outputs build/mansion-of-ashes.html
```

Equivalent direct command:

```bash
./.tools/tweego/tweego -f sugarcube-2 -o build/mansion-of-ashes.html story/mansion-of-ashes.tw
```

## Alternative: Import into Twine 2 (no toolchain required)

1. Open https://twinery.org/2 or the Twine 2 desktop app
2. **Library → Import From File** → select `story/mansion-of-ashes.tw`
3. Click **Play** to test in-browser, or **Publish to File** to export HTML

## Smoke-test checklist

- [ ] Title screen loads and Begin link works
- [ ] Kitchen → matches; Basement Stairs gated without them
- [ ] Study → ledger → Hallway portrait → silver key
- [ ] Conservatory → birdcage examine (test with and without diary page)
- [ ] Fuse Box → power restored → Main Exit → caretaker appears
- [ ] All three endings reachable; Bitter Truth requires diary + ledger + conservatory + pantry clue
- [ ] Dawn sky text progresses in Hallway across a full playthrough
