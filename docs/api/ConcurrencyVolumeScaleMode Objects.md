## ConcurrencyVolumeScaleMode Objects

```python
class ConcurrencyVolumeScaleMode(EnumBase)
```

EConcurrency Volume Scale Mode

**C++ Source:**

- **Module**: Engine
- **File**: SoundConcurrency.h

<a id="unreal.ConcurrencyVolumeScaleMode.DEFAULT"></a>

#### DEFAULT

0: Scales volume of older sounds more than newer sounds (default)

<a id="unreal.ConcurrencyVolumeScaleMode.DISTANCE"></a>

#### DISTANCE

1: Scales distant sounds by volume scalar more than closer sounds

<a id="unreal.ConcurrencyVolumeScaleMode.PRIORITY"></a>

#### PRIORITY

2: Scales lower priority sounds by volume scalar more than closer sounds

<a id="unreal.TextureSourceEncoding"></a>