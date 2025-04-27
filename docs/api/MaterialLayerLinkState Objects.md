## MaterialLayerLinkState Objects

```python
class MaterialLayerLinkState(EnumBase)
```

EMaterial Layer Link State

**C++ Source:**

- **Module**: Engine
- **File**: MaterialLayersFunctions.h

<a id="unreal.MaterialLayerLinkState.UNINITIALIZED"></a>

#### UNINITIALIZED

0

<a id="unreal.MaterialLayerLinkState.LINKED_TO_PARENT"></a>

#### LINKED_TO_PARENT

1: Saved with previous engine version

<a id="unreal.MaterialLayerLinkState.UNLINKED_FROM_PARENT"></a>

#### UNLINKED_FROM_PARENT

2: Layer should mirror changes from parent material

<a id="unreal.MaterialLayerLinkState.NOT_FROM_PARENT"></a>

#### NOT_FROM_PARENT

3: Layer is based on parent material, but should not mirror changes

<a id="unreal.SkeletalMeshTerminationCriterion"></a>