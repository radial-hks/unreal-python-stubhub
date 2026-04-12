## ProjectObjectTransform Objects

```python
class ProjectObjectTransform(StructBase)
```

Project Object Transform

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpProjectEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale3d`` (Vector):  [Read-Write]

<a id="unreal.ProjectObjectTransform.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Rotator = [0.000000, 0.000000, 0.000000],
             scale3d: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.ProjectObjectTransform.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.ProjectObjectTransform.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.ProjectObjectTransform.scale3d"></a>

#### scale3d

```python
@property
def scale3d() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.ProjectObjectTransformParams"></a>