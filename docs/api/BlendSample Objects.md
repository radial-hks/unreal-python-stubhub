## BlendSample Objects

```python
class BlendSample(StructBase)
```

Sample data

**C++ Source:**

- **Module**: Engine
- **File**: BlendSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation`` (AnimSequence):  [Read-Write] For linked animations
- ``include_in_analyse_all`` (bool):  [Read-Write] Whether or not this sample will be moved when the "analyse all" button is used. Note that, even if disabled,
  it will still be available for individual sample analysis/moving
- ``rate_scale`` (float):  [Read-Write]
- ``sample_value`` (Vector):  [Read-Write] blend 0->x, blend 1->y, blend 2->z

<a id="unreal.BlendSample.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BlendParameter"></a>