## BaseMediaSource Objects

```python
class BaseMediaSource(MediaSource)
```

Base class for concrete media sources.

**C++ Source:**

- **Module**: MediaAssets
- **File**: BaseMediaSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``platform_player_names`` (Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).

<a id="unreal.BaseMediaSource.platform_player_names"></a>

#### platform_player_names

```python
@property
def platform_player_names() -> Map[str, Name]
```

(Map[str, Name]):  [Read-Write] Override native media player plug-ins per platform (Empty = find one automatically).

<a id="unreal.BaseMediaSource.platform_player_names"></a>

#### platform_player_names

```python
@platform_player_names.setter
def platform_player_names(value: Map[str, Name]) -> None
```

<a id="unreal.FileMediaSource"></a>