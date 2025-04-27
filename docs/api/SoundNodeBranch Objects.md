## SoundNodeBranch Objects

```python
class SoundNodeBranch(SoundNode)
```

Selects a child node based on the value of a boolean parameter

**C++ Source:**

- **Module**: Engine
- **File**: SoundNodeBranch.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool_parameter_name`` (Name):  [Read-Write] The name of the boolean parameter to use to determine which branch we should take
- ``child_nodes`` (Array[SoundNode]):  [Read-Write]

<a id="unreal.SoundNodeConcatenator"></a>