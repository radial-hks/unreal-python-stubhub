## DisplayClusterConfigurationTile_Overscan Objects

```python
class DisplayClusterConfigurationTile_Overscan(StructBase)
```

Display Cluster Configuration Tile Overscan

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Tile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_sides`` (float):  [Read-Write] Overscan value for all sides.
- ``enabled`` (bool):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.
- ``mode`` (DisplayClusterConfigurationViewportOverscanMode):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.
- ``optimize_tile_overscan`` (bool):  [Read-Write] Optimize overscan values on boundary tiles.
  When enabled, tile sides not in contact with other tiles will use zero overscan.
- ``oversize`` (bool):  [Read-Write] Set to True to render at the overscan resolution, set to false to render at the resolution in the configuration and scale for overscan.

<a id="unreal.DisplayClusterConfigurationTile_Overscan.__init__"></a>

#### __init__

```python
def __init__(
        enabled: bool = False,
        oversize: bool = False,
        optimize_tile_overscan: bool = False,
        mode:
    DisplayClusterConfigurationViewportOverscanMode = DisplayClusterConfigurationViewportOverscanMode
    .PIXELS,
        all_sides: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Overscan.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.

<a id="unreal.DisplayClusterConfigurationTile_Overscan.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Overscan.oversize"></a>

#### oversize

```python
@property
def oversize() -> bool
```

(bool):  [Read-Write] Set to True to render at the overscan resolution, set to false to render at the resolution in the configuration and scale for overscan.

<a id="unreal.DisplayClusterConfigurationTile_Overscan.oversize"></a>

#### oversize

```python
@oversize.setter
def oversize(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Overscan.optimize_tile_overscan"></a>

#### optimize_tile_overscan

```python
@property
def optimize_tile_overscan() -> bool
```

(bool):  [Read-Write] Optimize overscan values on boundary tiles.
When enabled, tile sides not in contact with other tiles will use zero overscan.

<a id="unreal.DisplayClusterConfigurationTile_Overscan.optimize_tile_overscan"></a>

#### optimize_tile_overscan

```python
@optimize_tile_overscan.setter
def optimize_tile_overscan(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Overscan.mode"></a>

#### mode

```python
@property
def mode() -> DisplayClusterConfigurationViewportOverscanMode
```

(DisplayClusterConfigurationViewportOverscanMode):  [Read-Write] Enable/disable Viewport Overscan and specify units as percent or pixel values.

<a id="unreal.DisplayClusterConfigurationTile_Overscan.mode"></a>

#### mode

```python
@mode.setter
def mode(value: DisplayClusterConfigurationViewportOverscanMode) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Overscan.all_sides"></a>

#### all_sides

```python
@property
def all_sides() -> float
```

(float):  [Read-Write] Overscan value for all sides.

<a id="unreal.DisplayClusterConfigurationTile_Overscan.all_sides"></a>

#### all_sides

```python
@all_sides.setter
def all_sides(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaOutput"></a>