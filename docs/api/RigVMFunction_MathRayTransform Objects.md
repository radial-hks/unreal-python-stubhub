## RigVMFunction_MathRayTransform Objects

```python
class RigVMFunction_MathRayTransform(RigVMFunction_MathRayBase)
```

Returns the division of the two values

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ray`` (Ray):  [Read-Write]
- ``result`` (Ray):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayTransform.__init__"></a>

#### __init__

```python
def __init__(
    ray: Ray = [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000,
                                                 0.000000]],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    result: Ray = [[0.000000, 0.000000, 0.000000],
                   [0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathRayTransform.ray"></a>

#### ray

```python
@property
def ray() -> Ray
```

(Ray):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayTransform.ray"></a>

#### ray

```python
@ray.setter
def ray(value: Ray) -> None
```

<a id="unreal.RigVMFunction_MathRayTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathRayTransform.result"></a>

#### result

```python
@property
def result() -> Ray
```

(Ray):  [Read-Only]

<a id="unreal.RigVMFunction_MathRBFInterpolateBase"></a>