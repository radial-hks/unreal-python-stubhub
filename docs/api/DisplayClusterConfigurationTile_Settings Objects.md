## DisplayClusterConfigurationTile_Settings Objects

```python
class DisplayClusterConfigurationTile_Settings(StructBase)
```

* Tile rendering

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Tile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] Enable tile rendering.
- ``layout`` (IntPoint):  [Read-Write] Tiling layout (X by Y tiles amount).

<a id="unreal.DisplayClusterConfigurationTile_Settings.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False, layout: IntPoint = [0, 0]) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Settings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Enable tile rendering.

<a id="unreal.DisplayClusterConfigurationTile_Settings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Settings.layout"></a>

#### layout

```python
@property
def layout() -> IntPoint
```

(IntPoint):  [Read-Write] Tiling layout (X by Y tiles amount).

<a id="unreal.DisplayClusterConfigurationTile_Settings.layout"></a>

#### layout

```python
@layout.setter
def layout(value: IntPoint) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ICVFX"></a>