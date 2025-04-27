## HLODBatchingPolicy Objects

```python
class HLODBatchingPolicy(EnumBase)
```

Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.

**C++ Source:**

- **Module**: Engine
- **File**: HLODBatchingPolicy.h

<a id="unreal.HLODBatchingPolicy.NONE"></a>

#### NONE

0: No batching to be performed, geometry is to be simplified.

<a id="unreal.HLODBatchingPolicy.MESH_SECTION"></a>

#### MESH_SECTION

1: Batch this component geometry (using the lowest LOD) as a separate mesh section, grouping by material.

<a id="unreal.HLODBatchingPolicy.INSTANCING"></a>

#### INSTANCING

2: Batch this component geometry (using the lowest LOD) as a separate instanced static mesh component in the generated actor.

<a id="unreal.FirstPersonPrimitiveType"></a>