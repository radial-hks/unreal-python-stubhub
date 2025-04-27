## WaterExclusionMode Objects

```python
class WaterExclusionMode(EnumBase)
```

EWater Exclusion Mode

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterBodyExclusionVolume.h

<a id="unreal.WaterExclusionMode.ADD_WATER_BODIES_LIST_TO_EXCLUSION"></a>

#### ADD_WATER_BODIES_LIST_TO_EXCLUSION

0: Adds all water bodies specified in the WaterBodies list to the exclusion volume.
If none are specified, no water body overlapped by this volume will be part of the exclusion.

<a id="unreal.WaterExclusionMode.REMOVE_WATER_BODIES_LIST_FROM_EXCLUSION"></a>

#### REMOVE_WATER_BODIES_LIST_FROM_EXCLUSION

1: Removes all water bodies specified in the WaterBodies list from the exclusion volume.
If none are specified, every water body overlapped by this volume will be part of the exclusion.

<a id="unreal.ACLVisualFidelity"></a>