## DisplayClusterConfigurationMediaUniformTileInput Objects

```python
class DisplayClusterConfigurationMediaUniformTileInput(StructBase)
```

Uniform tile media input item. Maps a tile to a media source.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``media_source`` (MediaSource):  [Read-Write] Media source to use
- ``position`` (IntPoint):  [Read-Write] Tile position

<a id="unreal.DisplayClusterConfigurationMediaUniformTileInput.__init__"></a>

#### __init__

```python
def __init__(position: IntPoint = [0, 0],
             media_source: MediaSource = None) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaUniformTileInput.position"></a>

#### position

```python
@property
def position() -> IntPoint
```

(IntPoint):  [Read-Only] Tile position

<a id="unreal.DisplayClusterConfigurationMediaUniformTileInput.media_source"></a>

#### media_source

```python
@property
def media_source() -> MediaSource
```

(MediaSource):  [Read-Write] Media source to use

<a id="unreal.DisplayClusterConfigurationMediaUniformTileInput.media_source"></a>

#### media_source

```python
@media_source.setter
def media_source(value: MediaSource) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Overscan"></a>