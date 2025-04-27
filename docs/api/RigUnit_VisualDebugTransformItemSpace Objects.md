## RigUnit_VisualDebugTransformItemSpace Objects

```python
class RigUnit_VisualDebugTransformItemSpace(RigUnit_DebugBase)
```

Debug draw parameters for an Axis given a transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_VisualDebug.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.__init__"></a>

#### __init__

```python
def __init__(value: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
             enabled: bool = False,
             thickness: float = 0.000000,
             scale: float = 0.000000,
             space: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugTransformItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ConvertTransform"></a>