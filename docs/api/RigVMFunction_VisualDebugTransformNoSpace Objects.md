## RigVMFunction_VisualDebugTransformNoSpace Objects

```python
class RigVMFunction_VisualDebugTransformNoSpace(RigVMFunction_DebugBase)
```

Debug draw parameters for an Axis given a transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_VisualDebug.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.__init__"></a>

#### __init__

```python
def __init__(value: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
             enabled: bool = False,
             thickness: float = 0.000000,
             scale: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugTransformNoSpace.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigVMFunction_ForLoopCount"></a>