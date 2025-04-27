## PlatformMediaSource Objects

```python
class PlatformMediaSource(MediaSource)
```

A media source that selects other media sources based on target platform.

Use this asset to override media sources on a per-platform basis.

**C++ Source:**

- **Module**: MediaAssets
- **File**: PlatformMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``platform_media_sources`` (Map[str, MediaSource]):  [Read-Write] Media sources per platform.

<a id="unreal.StreamMediaSource"></a>