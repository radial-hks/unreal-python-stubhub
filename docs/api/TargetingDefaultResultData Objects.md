## TargetingDefaultResultData Objects

```python
class TargetingDefaultResultData(StructBase)
```

struct: FTargetingDefaultResultData

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSystemTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hit_result`` (HitResult):  [Read-Write] The hit result for this target
- ``score`` (float):  [Read-Write] The score associated w/ this target

<a id="unreal.TargetingDefaultResultData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(hit_result: HitResult = [
    False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0, 0,
    [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
],
             score: float = 0.000000) -> None
```

<a id="unreal.TargetingDefaultResultData.hit_result"></a>

#### hit\_result

```python
@property
def hit_result() -> HitResult
```

(HitResult):  [Read-Only] The hit result for this target

<a id="unreal.TargetingDefaultResultData.score"></a>

#### score

```python
@property
def score() -> float
```

(float):  [Read-Only] The score associated w/ this target

<a id="unreal.TargetingSourceContext"></a>