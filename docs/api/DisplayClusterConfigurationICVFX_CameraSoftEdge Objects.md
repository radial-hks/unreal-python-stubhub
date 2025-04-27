## DisplayClusterConfigurationICVFX_CameraSoftEdge Objects

```python
class DisplayClusterConfigurationICVFX_CameraSoftEdge(StructBase)
```

Display Cluster Configuration ICVFX Camera Soft Edge

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``feather`` (float):  [Read-Write] Feather.
- ``horizontal`` (float):  [Read-Write] Adjust blur amount to the left and right side edges of the inner frustum.
- ``vertical`` (float):  [Read-Write] Adjust blur amount to the top and bottom edges of the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.__init__"></a>

#### __init__

```python
def __init__(vertical: float = 0.000000,
             horizontal: float = 0.000000,
             feather: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.vertical"></a>

#### vertical

```python
@property
def vertical() -> float
```

(float):  [Read-Write] Adjust blur amount to the top and bottom edges of the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.vertical"></a>

#### vertical

```python
@vertical.setter
def vertical(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.horizontal"></a>

#### horizontal

```python
@property
def horizontal() -> float
```

(float):  [Read-Write] Adjust blur amount to the left and right side edges of the inner frustum.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.horizontal"></a>

#### horizontal

```python
@horizontal.setter
def horizontal(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.feather"></a>

#### feather

```python
@property
def feather() -> float
```

(float):  [Read-Write] Feather.

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge.feather"></a>

#### feather

```python
@feather.setter
def feather(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraBorder"></a>