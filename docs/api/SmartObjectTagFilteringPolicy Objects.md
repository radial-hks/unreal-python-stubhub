## SmartObjectTagFilteringPolicy Objects

```python
class SmartObjectTagFilteringPolicy(EnumBase)
```

Indicates how TagQueries from slots and parent object will be processed against Tags from a find request.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

<a id="unreal.SmartObjectTagFilteringPolicy.NO_FILTER"></a>

#### NO\_FILTER

0: TagQueries in the object and slot definitions are not used by the framework to filter results. Users can access them and perform its own filtering.

<a id="unreal.SmartObjectTagFilteringPolicy.COMBINE"></a>

#### COMBINE

1: Both TagQueries (parent object and slot) will be applied to the Tags provided by a request.

<a id="unreal.SmartObjectTagFilteringPolicy.OVERRIDE"></a>

#### OVERRIDE

2: TagQuery in slot (if any) will be used instead of the parent object TagQuery to run against the Tags provided by a request. EmptyTagQuery on a slot indicates no override.

<a id="unreal.TrySpawnActorIfDehydrated"></a>