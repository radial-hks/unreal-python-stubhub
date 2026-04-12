## CameraData Objects

```python
class CameraData(StructBase)
```

Camera Data

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: Visible2DAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hide_distance`` (float):  [Read-Write]
- ``hide_type`` (str):  [Read-Write]
- ``scale_mode`` (str):  [Read-Write]
- ``size`` (Vector2D):  [Read-Write]
- ``url`` (str):  [Read-Write] none, default and url

<a id="unreal.CameraData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(hide_distance: float = 0.000000,
             hide_type: str = "",
             url: str = "",
             size: Vector2D = [0.000000, 0.000000],
             scale_mode: str = "") -> None
```

<a id="unreal.CameraData.hide_distance"></a>

#### hide\_distance

```python
@property
def hide_distance() -> float
```

(float):  [Read-Only]

<a id="unreal.CameraData.hide_type"></a>

#### hide\_type

```python
@property
def hide_type() -> str
```

(str):  [Read-Only]

<a id="unreal.CameraData.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Only] none, default and url

<a id="unreal.CameraData.size"></a>

#### size

```python
@property
def size() -> Vector2D
```

(Vector2D):  [Read-Only]

<a id="unreal.CameraData.scale_mode"></a>

#### scale\_mode

```python
@property
def scale_mode() -> str
```

(str):  [Read-Only]

<a id="unreal.InteractionData"></a>