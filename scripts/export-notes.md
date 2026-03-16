# Export Notes

The repository keeps the Twee file in `story/` as the source of truth. Exported playable builds belong in `build/`.

Suggested local workflow:

1. Edit `story/mansion-of-ashes.tw`
2. Run `scripts/build-story.sh`
3. Open `build/mansion-of-ashes.html`
4. Smoke-test the build in a browser before sharing or pushing

The repository prefers the local Tweego setup if present. The build script compiles with the pinned SugarCube format in `.storyformats/`.

```bash
scripts/build-story.sh
```

Equivalent direct command:

```bash
./.tools/tweego/tweego -f sugarcube-2 -o build/mansion-of-ashes.html story/mansion-of-ashes.tw
```
