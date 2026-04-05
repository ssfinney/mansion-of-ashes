# Audio Design Guide

## Design principle

The story is grief-forward, not horror-forward. Audio should suggest the house existing around you: settling wood, distant wind, intermittent electrical hum. Silence remains the dominant texture. Music appears rarely and only where it reinforces emotional turns.

## Runtime mix goals

- Music bed: `0.20–0.30`
- Room tones: `0.15–0.25`
- Spot SFX: `0.60–0.80`
- Caretaker confrontation: `0.00–0.10` (prefer silence)

## Recommended licensed sources

### Music (Scott Buckley, CC BY 4.0)

- **Undertow**
  - Use: Title and opening moments.
  - Library page: <https://www.scottbuckley.com.au/library/undertow/>
- **Hiraeth**
  - Use: Core exploration loop (hallway, kitchen, study).
  - Library page: <https://www.scottbuckley.com.au/library/hiraeth/>
- **Conservatory theme candidate**
  - Use: Conservatory reveal and emotionally intense endings.
  - Source pool: <https://www.scottbuckley.com.au/library/instrumentation/cello/>

### Ambience (Freesound)

- **Windy, creaky old house ambience** by pfranzen (CC BY 3.0)
  - <https://freesound.org/people/pfranzen/sounds/393808/>
- **room-tone windy house** by klankbeeld (CC BY 3.0)
  - <https://freesound.org/people/klankbeeld/sounds/172307/>
- **Old HOUSE atmosphere sounds** pack by Robinhood76
  - Check individual file licenses before shipping.
  - <https://freesound.org/people/Robinhood76/packs/4054/>

### Spot SFX (Freesound)

- **Match - Strike and Light 02** by JarredGibb (CC0)
  - <https://freesound.org/people/JarredGibb/sounds/248236/>
- **Match strike 01** by scalywhale (CC0, backup)
  - <https://freesound.org/people/scalywhale/sounds/423809/>
- **SFX Ambiance: Electrical Hum** by trullilulli (CC0)
  - <https://freesound.org/people/trullilulli/sounds/422645/>
- **Backrooms Ambience** by Resaural (CC0, alternate)
  - <https://freesound.org/people/Resaural/sounds/626096/>
- **Creaking Floorboard** by Benboncan (CC BY 3.0)
  - <https://freesound.org/people/Benboncan/sounds/101381/>
- **wood door old open close slow creak steps enter** by kyles
  - Check license on page.
  - <https://freesound.org/people/kyles/sounds/455852/>
- **creaking floor** by petewyer2 (CC0)
  - <https://freesound.org/people/petewyer2/sounds/347851/>

## SugarCube integration pattern

Use StoryInit for audio registration:

```twine
<<cacheaudio "music-undertow" "assets/audio/music/undertow.mp3">>
<<cacheaudio "music-hiraeth" "assets/audio/music/hiraeth.mp3">>
<<cacheaudio "amb-house" "assets/audio/ambience/house-interior.mp3">>
<<cacheaudio "sfx-match-strike" "assets/audio/sfx/match-strike.mp3">>
```

Passage-level playback:

```twine
<<audio "amb-house" loop volume 0.2 play>>
<<if $powerOn>><<audio "amb-elec-hum" loop volume 0.14 play>><</if>>
```

One-shot trigger example:

```twine
<<audio "sfx-match-strike" volume 0.75 play>>
```

Use `fadein` / `fadeout` for transitions between title, exploration, and conservatory sequences.

## File organization

```text
assets/
└── audio/
    ├── music/
    │   ├── hiraeth.mp3
    │   ├── undertow.mp3
    │   └── conservatory-theme.mp3
    ├── ambience/
    │   ├── house-interior.mp3
    │   ├── windy-room.mp3
    │   └── electrical-hum.mp3
    └── sfx/
        ├── match-strike.mp3
        ├── floorboard-creak.mp3
        └── door-creak.mp3
```

## Attribution template

Add to in-game credits and/or README, then prune to only shipped files:

```text
Music by Scott Buckley — released under Creative Commons Attribution 4.0
https://www.scottbuckley.com.au

Sound effects from Freesound.org:
- "Windy, creaky old house ambience" by pfranzen (CC BY 3.0)
- "Match - Strike and Light 02" by JarredGibb (CC0)
- "SFX Ambiance: Electrical Hum" by trullilulli (CC0)
- "Backrooms Ambience" by Resaural (CC0)
- "Creaking Floorboard" by Benboncan (CC BY 3.0)
- "creaking floor" by petewyer2 (CC0)
- "room-tone windy house" by klankbeeld (CC BY 3.0)
```
