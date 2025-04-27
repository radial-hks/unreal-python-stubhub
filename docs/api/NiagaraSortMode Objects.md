## NiagaraSortMode Objects

```python
class NiagaraSortMode(EnumBase)
```

ENiagara Sort Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraGPUSortInfo.h

<a id="unreal.NiagaraSortMode.NONE"></a>

#### NONE

0: Perform no additional sorting prior to rendering.

<a id="unreal.NiagaraSortMode.VIEW_DEPTH"></a>

#### VIEW_DEPTH

1: Sort by depth to the camera's near plane.

<a id="unreal.NiagaraSortMode.VIEW_DISTANCE"></a>

#### VIEW_DISTANCE

2: Sort by distance to the camera's origin.

<a id="unreal.NiagaraSortMode.CUSTOM_ASCENDING"></a>

#### CUSTOM_ASCENDING

3: Sort according to particles CustomSortingBinding (defaults to Particles.NormalizedAge).
Lower values will be sorted before higher values, i.e. 1 would draw on top of 0.

<a id="unreal.NiagaraSortMode.CUSTOM_DECENDING"></a>

#### CUSTOM_DECENDING

4: Sort according to particles CustomSortingBinding (defaults to Particles.NormalizedAge).
Higher values will be sorted before lower values, i.e. 0 would draw on top of 1.

<a id="unreal.NiagaraRendererSortPrecision"></a>