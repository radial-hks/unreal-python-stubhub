## NonSpatializedRadiusSpeakerMapMode Objects

```python
class NonSpatializedRadiusSpeakerMapMode(EnumBase)
```

Defines how to speaker map the sound when using the non-spatialized radius feature

**C++ Source:**

- **Module**: Engine
- **File**: SoundAttenuation.h

<a id="unreal.NonSpatializedRadiusSpeakerMapMode.OMNI_DIRECTIONAL"></a>

#### OMNI_DIRECTIONAL

0: Will blend the 3D sound to an omni-directional sound (equal output mapping in all directions)

<a id="unreal.NonSpatializedRadiusSpeakerMapMode.DIRECT2D"></a>

#### DIRECT2D

1: Will blend the 3D source to the same representation speaker map used when playing the asset 2D

<a id="unreal.NonSpatializedRadiusSpeakerMapMode.SURROUND2D"></a>

#### SURROUND2D

2: Will blend the 3D source to a multichannel 2D version (i.e. upmix stereo to quad) if rendering in surround

<a id="unreal.SourceBusSendLevelControlMethod"></a>