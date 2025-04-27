## HLODProxy Objects

```python
class HLODProxy(Object)
```

This asset acts as a proxy to a static mesh for ALODActors to display

**C++ Source:**

- **Module**: Engine
- **File**: HLODProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hlod_actors`` (Map[HLODProxyDesc, HLODProxyMesh]):  [Read-Only]
- ``owning_map`` (World):  [Read-Only] Keep hold of the level in the editor to allow for package cleaning etc.
- ``proxy_meshes`` (Array[HLODProxyMesh]):  [Read-Only] All the mesh proxies we contain

<a id="unreal.MorphTarget"></a>