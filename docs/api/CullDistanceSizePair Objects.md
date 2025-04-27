## CullDistanceSizePair Objects

```python
class CullDistanceSizePair(StructBase)
```

Helper structure containing size and cull distance pair.

**C++ Source:**

- **Module**: Engine
- **File**: CullDistanceVolume.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cull_distance`` (float):  [Read-Write] Cull distance associated with size.
- ``size`` (float):  [Read-Write] Size to associate with cull distance.

<a id="unreal.CullDistanceSizePair.__init__"></a>

#### __init__

```python
def __init__(size: float = 0.000000, cull_distance: float = 0.000000) -> None
```

<a id="unreal.CullDistanceSizePair.size"></a>

#### size

```python
@property
def size() -> float
```

(float):  [Read-Only] Size to associate with cull distance.

<a id="unreal.CullDistanceSizePair.cull_distance"></a>

#### cull_distance

```python
@property
def cull_distance() -> float
```

(float):  [Read-Only] Cull distance associated with size.

<a id="unreal.RuntimeVectorCurve"></a>