## SyncOption Objects

```python
class SyncOption(EnumBase)
```

ESync Option

**C++ Source:**

- **Module**: Engine
- **File**: LODSyncComponent.h

<a id="unreal.SyncOption.DRIVE"></a>

#### DRIVE

0: Drive LOD from this component. It will contribute to the change of LOD

<a id="unreal.SyncOption.PASSIVE"></a>

#### PASSIVE

1: It follows what's currently driven by other components. It doesn't contribute to the change of LOD

<a id="unreal.SyncOption.DISABLED"></a>

#### DISABLED

2: It is disabled, it doesn't do anything

<a id="unreal.SplinePointType"></a>