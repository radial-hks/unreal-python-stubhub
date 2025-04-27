## RigVMFunction_MathRayGetAt Objects

```python
class RigVMFunction_MathRayGetAt(RigVMFunction_MathRayBase)
```

Returns the position on a ray

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ratio`` (float):  [Read-Write]
- ``ray`` (Ray):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayGetAt.__init__"></a>

#### __init__

```python
def __init__(ray: Ray = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000]],
             ratio: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathRayGetAt.ray"></a>

#### ray

```python
@property
def ray() -> Ray
```

(Ray):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayGetAt.ray"></a>

#### ray

```python
@ray.setter
def ray(value: Ray) -> None
```

<a id="unreal.RigVMFunction_MathRayGetAt.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayGetAt.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.RigVMFunction_MathRayGetAt.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayTransform"></a>