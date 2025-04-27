## MeshUVChannelInfo Objects

```python
class MeshUVChannelInfo(StructBase)
```

The world size for each texcoord mapping. Used by the texture streaming.

**C++ Source:**

- **Module**: Engine
- **File**: MeshUVChannelInfo.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_uv_densities`` (float):  [Read-Write] The UV density in the mesh, before any transform scaling, in world unit per UV.
  This value represents the length taken to cover a full UV unit.
- ``override_densities`` (bool):  [Read-Write] Whether this values was set manually or is auto generated.

<a id="unreal.MeshUVChannelInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NavAvoidanceMask"></a>