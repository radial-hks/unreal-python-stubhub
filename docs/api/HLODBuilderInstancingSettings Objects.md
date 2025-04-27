## HLODBuilderInstancingSettings Objects

```python
class HLODBuilderInstancingSettings(HLODBuilderSettings)
```

HLODBuilder Instancing Settings

**C++ Source:**

- **Plugin**: WorldPartitionHLODUtilities
- **Module**: WorldPartitionHLODUtilities
- **File**: HLODBuilderInstancing.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disallow_nanite`` (bool):  [Read-Write] If enabled, the components created for the HLODs will not use Nanite.
  Necessary if you want to use the last LOD & the mesh is Nanite enabled, as forced LODs are ignored by Nanite

<a id="unreal.HLODBuilderInstancingSettings.disallow_nanite"></a>

#### disallow_nanite

```python
@property
def disallow_nanite() -> bool
```

(bool):  [Read-Write] If enabled, the components created for the HLODs will not use Nanite.
Necessary if you want to use the last LOD & the mesh is Nanite enabled, as forced LODs are ignored by Nanite

<a id="unreal.HLODBuilderInstancingSettings.disallow_nanite"></a>

#### disallow_nanite

```python
@disallow_nanite.setter
def disallow_nanite(value: bool) -> None
```

<a id="unreal.HLODBuilderMeshApproximateSettings"></a>