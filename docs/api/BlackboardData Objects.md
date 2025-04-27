## BlackboardData Objects

```python
class BlackboardData(DataAsset)
```

Blackboard Data

**C++ Source:**

- **Module**: AIModule
- **File**: BlackboardData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keys`` (Array[BlackboardEntry]):  [Read-Write] blackboard keys
- ``parent`` (BlackboardData):  [Read-Write] parent blackboard (keys can be overridden)
- ``parent_keys`` (Array[BlackboardEntry]):  [Read-Only] all keys inherited from parent chain

<a id="unreal.BTFunctionLibrary"></a>