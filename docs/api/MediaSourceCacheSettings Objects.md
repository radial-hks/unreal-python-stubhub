## MediaSourceCacheSettings Objects

```python
class MediaSourceCacheSettings(StructBase)
```

Cache settings to pass to the player.

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaSourceOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override`` (bool):  [Read-Write] Override the default cache settings.
  Currently only the ImgMedia player supports these settings.
- ``time_to_look_ahead`` (float):  [Read-Write] The cache will fill up with frames that are up to this time from the current time.
  E.g. if this is 0.2, and we are at time index 5 seconds,
  then we will fill the cache with frames between 5 seconds and 5.2 seconds.

<a id="unreal.MediaSourceCacheSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MediaCaptureDevice"></a>