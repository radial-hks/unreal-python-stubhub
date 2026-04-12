## SmartObjectTagMergingPolicy Objects

```python
class SmartObjectTagMergingPolicy(EnumBase)
```

Indicates how Tags from slots and parent object are combined to be evaluated by a TagQuery from a find request.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

<a id="unreal.SmartObjectTagMergingPolicy.COMBINE"></a>

#### COMBINE

0: Tags are combined (parent object and slot) and TagQuery from the request will be run against the combined list.

<a id="unreal.SmartObjectTagMergingPolicy.OVERRIDE"></a>

#### OVERRIDE

1: Tags in slot (if any) will be used instead of the parent object Tags when running the TagQuery from a request. Empty Tags on a slot indicates no override.

<a id="unreal.SmartObjectTagFilteringPolicy"></a>