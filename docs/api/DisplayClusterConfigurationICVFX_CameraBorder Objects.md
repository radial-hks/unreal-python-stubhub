## DisplayClusterConfigurationICVFX_CameraBorder Objects

```python
class DisplayClusterConfigurationICVFX_CameraBorder(StructBase)
```

Display Cluster Configuration ICVFX Camera Border

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] Adjust color of the border edges of the inner frustum.
- ``enable`` (bool):  [Read-Write] Enable Inner Frustum Border.
- ``thickness`` (float):  [Read-Write] Adjust border width to the top and bottom edges of the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.__init__"></a>

#### __init__

```python
def __init__(
        enable: bool = False,
        thickness: float = 0.000000,
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enable Inner Frustum Border.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write] Adjust border width to the top and bottom edges of the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] Adjust color of the border edges of the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraCustomFrustum"></a>