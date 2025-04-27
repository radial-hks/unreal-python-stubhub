## OverlapFilterOption Objects

```python
class OverlapFilterOption(EnumBase)
```

Specifies what types of objects to return from an overlap physics query
warning: If you change this, change GetCollisionChannelFromOverlapFilter() to match

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.OverlapFilterOption.OVERLAP_FILTER_ALL"></a>

#### OVERLAP_FILTER_ALL

0: Returns both overlaps with both dynamic and static components

<a id="unreal.OverlapFilterOption.OVERLAP_FILTER_DYNAMIC_ONLY"></a>

#### OVERLAP_FILTER_DYNAMIC_ONLY

1: returns only overlaps with dynamic actors (far fewer results in practice, much more efficient)

<a id="unreal.OverlapFilterOption.OVERLAP_FILTER_STATIC_ONLY"></a>

#### OVERLAP_FILTER_STATIC_ONLY

2: returns only overlaps with static actors (fewer results, more efficient)

<a id="unreal.NetRole"></a>