## DisplayClusterConfigurationMediaUniformTileOutput Objects

```python
class DisplayClusterConfigurationMediaUniformTileOutput(StructBase)
```

Uniform tile media output item. Maps a tile to a media output.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``media_output`` (MediaOutput):  [Read-Write] Media output to use
- ``position`` (IntPoint):  [Read-Write] Tile position

<a id="unreal.DisplayClusterConfigurationMediaUniformTileOutput.__init__"></a>

#### __init__

```python
def __init__(position: IntPoint = [0, 0],
             media_output: MediaOutput = None) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaUniformTileOutput.position"></a>

#### position

```python
@property
def position() -> IntPoint
```

(IntPoint):  [Read-Only] Tile position

<a id="unreal.DisplayClusterConfigurationMediaUniformTileOutput.media_output"></a>

#### media_output

```python
@property
def media_output() -> MediaOutput
```

(MediaOutput):  [Read-Write] Media output to use

<a id="unreal.DisplayClusterConfigurationMediaUniformTileOutput.media_output"></a>

#### media_output

```python
@media_output.setter
def media_output(value: MediaOutput) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledInputGroup"></a>