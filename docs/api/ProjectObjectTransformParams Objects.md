## ProjectObjectTransformParams Objects

```python
class ProjectObjectTransformParams(ParamsBase)
```

Project Object Transform Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpProjectEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale3d`` (Vector):  [Read-Write]

<a id="unreal.ProjectObjectTransformParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: int = 0,
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Rotator = [0.000000, 0.000000, 0.000000],
             scale3d: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.ProjectObjectTransformParams.eid"></a>

#### eid

```python
@property
def eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.ProjectObjectTransformParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: int) -> None
```

<a id="unreal.ProjectObjectTransformParams.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.ProjectObjectTransformParams.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.ProjectObjectTransformParams.scale3d"></a>

#### scale3d

```python
@property
def scale3d() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.ProjectObjectTransformResult"></a>