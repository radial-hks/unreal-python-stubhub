## ResonanceRenderMode Objects

```python
class ResonanceRenderMode(EnumBase)
```

EResonance Render Mode

**C++ Source:**

- **Plugin**: ResonanceAudio
- **Module**: ResonanceAudio
- **File**: ResonanceAudioAmbisonicsSettings.h

<a id="unreal.ResonanceRenderMode.STEREO_PANNING"></a>

#### STEREO_PANNING

0: Stereo panning, i.e., this disables HRTF-based rendering.

<a id="unreal.ResonanceRenderMode.BINAURAL_LOW_QUALITY"></a>

#### BINAURAL_LOW_QUALITY

1: HRTF-based rendering using First Order Ambisonics, over a virtual array of
8 loudspeakers arranged in a cube configuration around the listener's head.

<a id="unreal.ResonanceRenderMode.BINAURAL_MEDIUM_QUALITY"></a>

#### BINAURAL_MEDIUM_QUALITY

2: HRTF-based rendering using Second Order Ambisonics, over a virtual array of
12 loudspeakers arranged in a dodecahedral configuration (using faces of
the dodecahedron).

<a id="unreal.ResonanceRenderMode.BINAURAL_HIGH_QUALITY"></a>

#### BINAURAL_HIGH_QUALITY

3: HRTF-based rendering using Third Order Ambisonics, over a virtual array of
26 loudspeakers arranged in a Lebedev grid: https:goo.gl/DX1wh3.

<a id="unreal.ResonanceRenderMode.ROOM_EFFECTS_ONLY"></a>

#### ROOM_EFFECTS_ONLY

4: Room effects only rendering. This disables HRTF-based rendering and direct
(dry) output of a sound object. Note that this rendering mode should *not*
be used for general-purpose sound object spatialization, as it will only
render the corresponding room effects of given sound objects without the
direct spatialization.

<a id="unreal.StateTreeStateType"></a>