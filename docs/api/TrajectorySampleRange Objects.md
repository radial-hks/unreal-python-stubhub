## TrajectorySampleRange Objects

```python
class TrajectorySampleRange(StructBase)
```

A container of ordered trajectory samples and associated sampling rate

**C++ Source:**

- **Module**: Engine
- **File**: MotionTrajectoryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``samples`` (Array[TrajectorySample]):  [Read-Write] Linearly ordered container for past, present, and future trajectory samples

<a id="unreal.TrajectorySampleRange.__init__"></a>

#### __init__

```python
def __init__(samples: Array[TrajectorySample] = []) -> None
```

<a id="unreal.TrajectorySampleRange.samples"></a>

#### samples

```python
@property
def samples() -> Array[TrajectorySample]
```

(Array[TrajectorySample]):  [Read-Write] Linearly ordered container for past, present, and future trajectory samples

<a id="unreal.TrajectorySampleRange.samples"></a>

#### samples

```python
@samples.setter
def samples(value: Array[TrajectorySample]) -> None
```

<a id="unreal.AssetCompileData"></a>