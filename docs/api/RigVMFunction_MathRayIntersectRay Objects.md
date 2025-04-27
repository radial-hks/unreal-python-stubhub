## RigVMFunction_MathRayIntersectRay Objects

```python
class RigVMFunction_MathRayIntersectRay(RigVMFunction_MathRayBase)
```

Returns the closest point intersection of a ray with another ray

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Ray):  [Read-Write]
- ``b`` (Ray):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``ratio_a`` (float):  [Read-Write]
- ``ratio_b`` (float):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectRay.__init__"></a>

#### __init__

```python
def __init__(a: Ray = [[0.000000, 0.000000, 0.000000],
                       [0.000000, 0.000000, 0.000000]],
             b: Ray = [[0.000000, 0.000000, 0.000000],
                       [0.000000, 0.000000, 0.000000]],
             result: Vector = [0.000000, 0.000000, 0.000000],
             distance: float = 0.000000,
             ratio_a: float = 0.000000,
             ratio_b: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectRay.a"></a>

#### a

```python
@property
def a() -> Ray
```

(Ray):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectRay.a"></a>

#### a

```python
@a.setter
def a(value: Ray) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectRay.b"></a>

#### b

```python
@property
def b() -> Ray
```

(Ray):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectRay.b"></a>

#### b

```python
@b.setter
def b(value: Ray) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectRay.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayIntersectRay.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayIntersectRay.ratio_a"></a>

#### ratio_a

```python
@property
def ratio_a() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayIntersectRay.ratio_b"></a>

#### ratio_b

```python
@property
def ratio_b() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayIntersectPlane"></a>