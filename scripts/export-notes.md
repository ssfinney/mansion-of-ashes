# Export Notes

The repository keeps the Twee file in `story/` as the source of truth. Exported playable builds belong in `build/`.

Suggested local workflow:

1. Edit `story/mansion-of-ashes.tw`
2. Export to HTML with your preferred Twine/Twee toolchain
3. Save the generated file in `build/`, for example `build/mansion-of-ashes.html`
4. Smoke-test the build in a browser before sharing or pushing

If using Tweego locally, a typical command would look like:

```bash
tweego -o build/mansion-of-ashes.html story/mansion-of-ashes.tw
```
