## RigVMFunction_MathTransformArrayToSRT Objects

```python
class RigVMFunction_MathTransformArrayToSRT(RigVMFunction_MathTransformBase)
```

Decomposes a Transform Array to its components.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rotations`` (Array[Quat]):  [Read-Write]
- ``scales`` (Array[Vector]):  [Read-Write]
- ``transforms`` (Array[Transform]):  [Read-Write]
- ``translations`` (Array[Vector]):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformArrayToSRT.__init__"></a>

#### __init__

```python
def __init__(transforms: Array[Transform] = [],
             translations: Array[Vector] = [],
             rotations: Array[Quat] = [],
             scales: Array[Vector] = []) -> None
```

<a id="unreal.RigVMFunction_MathTransformArrayToSRT.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformArrayToSRT.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigVMFunction_MathTransformArrayToSRT.translations"></a>

#### translations

```python
@property
def translations() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.RigVMFunction_MathTransformArrayToSRT.rotations"></a>

#### rotations

```python
@property
def rotations() -> Array[Quat]
```

(Array[Quat]):  [Read-Only]

<a id="unreal.RigVMFunction_MathTransformArrayToSRT.scales"></a>

#### scales

```python
@property
def scales() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.RigUnit_MathTransformArrayToSRT"></a>