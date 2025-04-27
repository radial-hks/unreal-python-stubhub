## PositionHistory Objects

```python
class PositionHistory(StructBase)
```

An easing type defining how to ease float values.
The FPositionHistory is a container to record position changes
over time. This is used to calculate velocity of a bone, for example.
The FPositionArray also tracks the last index used to allow for
reuse of entries (instead of appending to the array all the time).

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: KismetAnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``positions`` (Array[Vector]):  [Read-Write] The recorded positions
- ``range`` (float):  [Read-Write] The range for this particular history

<a id="unreal.PositionHistory.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimationStateResultReference"></a>