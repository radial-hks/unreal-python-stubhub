## DisplayClusterConfigurationMediaICVFX Objects

```python
class DisplayClusterConfigurationMediaICVFX(StructBase)
```

* Media settings for ICVFX cameras

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_nodes_to_render_unbound_tiles`` (DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Choose nodes that should render camera tiles that don't have any media assigned
- ``enable`` (bool):  [Read-Write] Enable/disable media
- ``late_ocio_pass`` (bool):  [Read-Write] Allows the receviers to apply their own OCIO transformations (per node OCIO override). Requires the media to support FloatRGBA.
- ``media_input_groups`` (Array[DisplayClusterConfigurationMediaInputGroup]):  [Read-Write] Media input mapping (Full frame)
- ``media_output_groups`` (Array[DisplayClusterConfigurationMediaOutputGroup]):  [Read-Write] Media output mapping (Full frame)
- ``split_type`` (DisplayClusterConfigurationMediaSplitType):  [Read-Write] Media frame split type
- ``tile_overscan`` (DisplayClusterConfigurationTile_Overscan):  [Read-Write] Overscan settings for tile.
- ``tiled_media_input_groups`` (Array[DisplayClusterConfigurationMediaTiledInputGroup]):  [Read-Write] Media input mapping (Tiled)
- ``tiled_media_output_groups`` (Array[DisplayClusterConfigurationMediaTiledOutputGroup]):  [Read-Write] Media output mapping (Tiled)
- ``tiled_split_layout`` (IntPoint):  [Read-Write] Split layout

<a id="unreal.DisplayClusterConfigurationMediaICVFX.__init__"></a>

#### __init__

```python
def __init__(
        enable: bool = False,
        split_type:
    DisplayClusterConfigurationMediaSplitType = DisplayClusterConfigurationMediaSplitType
    .FULL_FRAME,
        media_input_groups: Array[
            DisplayClusterConfigurationMediaInputGroup] = [],
        media_output_groups: Array[
            DisplayClusterConfigurationMediaOutputGroup] = [],
        tiled_split_layout: IntPoint = [0, 0],
        tile_overscan: DisplayClusterConfigurationTile_Overscan = [
            False, True, True,
            DisplayClusterConfigurationViewportOverscanMode.PERCENT, 10.000000
        ],
        cluster_nodes_to_render_unbound_tiles:
    DisplayClusterConfigurationClusterItemReferenceList = [[]],
        tiled_media_input_groups: Array[
            DisplayClusterConfigurationMediaTiledInputGroup] = [],
        tiled_media_output_groups: Array[
            DisplayClusterConfigurationMediaTiledOutputGroup] = [],
        late_ocio_pass: bool = False) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enable/disable media

<a id="unreal.DisplayClusterConfigurationMediaICVFX.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.split_type"></a>

#### split_type

```python
@property
def split_type() -> DisplayClusterConfigurationMediaSplitType
```

(DisplayClusterConfigurationMediaSplitType):  [Read-Write] Media frame split type

<a id="unreal.DisplayClusterConfigurationMediaICVFX.split_type"></a>

#### split_type

```python
@split_type.setter
def split_type(value: DisplayClusterConfigurationMediaSplitType) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.media_input_groups"></a>

#### media_input_groups

```python
@property
def media_input_groups() -> Array[DisplayClusterConfigurationMediaInputGroup]
```

(Array[DisplayClusterConfigurationMediaInputGroup]):  [Read-Write] Media input mapping (Full frame)

<a id="unreal.DisplayClusterConfigurationMediaICVFX.media_input_groups"></a>

#### media_input_groups

```python
@media_input_groups.setter
def media_input_groups(
        value: Array[DisplayClusterConfigurationMediaInputGroup]) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.media_output_groups"></a>

#### media_output_groups

```python
@property
def media_output_groups(
) -> Array[DisplayClusterConfigurationMediaOutputGroup]
```

(Array[DisplayClusterConfigurationMediaOutputGroup]):  [Read-Write] Media output mapping (Full frame)

<a id="unreal.DisplayClusterConfigurationMediaICVFX.media_output_groups"></a>

#### media_output_groups

```python
@media_output_groups.setter
def media_output_groups(
        value: Array[DisplayClusterConfigurationMediaOutputGroup]) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tiled_split_layout"></a>

#### tiled_split_layout

```python
@property
def tiled_split_layout() -> IntPoint
```

(IntPoint):  [Read-Write] Split layout

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tiled_split_layout"></a>

#### tiled_split_layout

```python
@tiled_split_layout.setter
def tiled_split_layout(value: IntPoint) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tile_overscan"></a>

#### tile_overscan

```python
@property
def tile_overscan() -> DisplayClusterConfigurationTile_Overscan
```

(DisplayClusterConfigurationTile_Overscan):  [Read-Write] Overscan settings for tile.

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tile_overscan"></a>

#### tile_overscan

```python
@tile_overscan.setter
def tile_overscan(value: DisplayClusterConfigurationTile_Overscan) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.cluster_nodes_to_render_unbound_tiles"></a>

#### cluster_nodes_to_render_unbound_tiles

```python
@property
def cluster_nodes_to_render_unbound_tiles(
) -> DisplayClusterConfigurationClusterItemReferenceList
```

(DisplayClusterConfigurationClusterItemReferenceList):  [Read-Write] Choose nodes that should render camera tiles that don't have any media assigned

<a id="unreal.DisplayClusterConfigurationMediaICVFX.cluster_nodes_to_render_unbound_tiles"></a>

#### cluster_nodes_to_render_unbound_tiles

```python
@cluster_nodes_to_render_unbound_tiles.setter
def cluster_nodes_to_render_unbound_tiles(
        value: DisplayClusterConfigurationClusterItemReferenceList) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tiled_media_input_groups"></a>

#### tiled_media_input_groups

```python
@property
def tiled_media_input_groups(
) -> Array[DisplayClusterConfigurationMediaTiledInputGroup]
```

(Array[DisplayClusterConfigurationMediaTiledInputGroup]):  [Read-Write] Media input mapping (Tiled)

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tiled_media_input_groups"></a>

#### tiled_media_input_groups

```python
@tiled_media_input_groups.setter
def tiled_media_input_groups(
        value: Array[DisplayClusterConfigurationMediaTiledInputGroup]) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tiled_media_output_groups"></a>

#### tiled_media_output_groups

```python
@property
def tiled_media_output_groups(
) -> Array[DisplayClusterConfigurationMediaTiledOutputGroup]
```

(Array[DisplayClusterConfigurationMediaTiledOutputGroup]):  [Read-Write] Media output mapping (Tiled)

<a id="unreal.DisplayClusterConfigurationMediaICVFX.tiled_media_output_groups"></a>

#### tiled_media_output_groups

```python
@tiled_media_output_groups.setter
def tiled_media_output_groups(
        value: Array[DisplayClusterConfigurationMediaTiledOutputGroup]
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaICVFX.late_ocio_pass"></a>

#### late_ocio_pass

```python
@property
def late_ocio_pass() -> bool
```

(bool):  [Read-Write] Allows the receviers to apply their own OCIO transformations (per node OCIO override). Requires the media to support FloatRGBA.

<a id="unreal.DisplayClusterConfigurationMediaICVFX.late_ocio_pass"></a>

#### late_ocio_pass

```python
@late_ocio_pass.setter
def late_ocio_pass(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaTiledOutputGroup"></a>