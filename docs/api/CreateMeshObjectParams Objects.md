## CreateMeshObjectParams Objects

```python
class CreateMeshObjectParams(StructBase)
```

FCreateMeshObjectParams is a collection of input data intended to be passed to
UModelingObjectsCreationAPI::CreateMeshObject(). Not all data necessarily needs
to be specified, this will depend on the particular implementation. The comments
below are representative of how this data structure is used in the Tools and
API implementation(s) provided with Unreal Engine, but end-user implementors
could abuse these fields as necessary.

The definition of a "mesh object" is implementation-specific.

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_materials`` (Array[MaterialInterface]):  [Read-Write] Optional Materials for a newly-created Mesh Asset, if this is applicable for the created mesh object
- ``base_name`` (str):  [Read-Write] The base name of the new mesh object
- ``collision_mode`` (CollisionTraceFlag):  [Read-Write] Which Collision mode to enable on the new mesh object, if supported
- ``enable_collision`` (bool):  [Read-Write] Specify whether the new mesh object should have collision support/data
- ``enable_nanite`` (bool):  [Read-Write] Specify whether Nanite should be enabled on this new mesh object
- ``enable_raytracing_support`` (bool):  [Read-Write] Specify whether normals should be automatically recomputed for this new mesh object
- ``enable_recompute_normals`` (bool):  [Read-Write] Specify whether normals should be automatically recomputed for this new mesh object
- ``enable_recompute_tangents`` (bool):  [Read-Write] Specify whether tangents should be automatically recomputed for this new mesh object
- ``generate_lightmap_u_vs`` (bool):  [Read-Write] Specify whether to auto-generate Lightmap UVs (if applicable for the output mesh type)
- ``materials`` (Array[MaterialInterface]):  [Read-Write] Materials for the new mesh object
- ``nanite_proxy_triangle_percent`` (float):  [Read-Write] Specify the Nanite proxy triangle percentage for this new mesh object
  deprecated: Replaced NaniteProxyTrianglePercent with usage of Engine FMeshNaniteSettings
- ``nanite_settings`` (MeshNaniteSettings):  [Read-Write] Specify the Nanite Settings for this new mesh object, only used if bEnableNanite=true
- ``source_component`` (PrimitiveComponent):  [Read-Write] A Source Component the new mesh is based on, if such a Component exists
- ``target_world`` (World):  [Read-Write] The World/Level the new mesh object should be created in (if known)
- ``transform`` (Transform):  [Read-Write] The 3D local-to-world transform for the new mesh object
- ``type_hint`` (CreateObjectTypeHint):  [Read-Write] A suggested type for the newly-created Mesh (possibly ignored)
- ``type_hint_class`` (type(Class)):  [Read-Write] A suggested UClass type for the newly-created Object (possibly ignored)
- ``type_hint_extended`` (int32):  [Read-Write] An arbitrary integer that can be used to pass data to an API implementation

<a id="unreal.CreateMeshObjectParams.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CreateMeshObjectParams.nanite_proxy_triangle_percent"></a>

#### nanite_proxy_triangle_percent

```python
@property
def nanite_proxy_triangle_percent() -> float
```

(float):  [Read-Write] Specify the Nanite proxy triangle percentage for this new mesh object
deprecated: Replaced NaniteProxyTrianglePercent with usage of Engine FMeshNaniteSettings

<a id="unreal.CreateMeshObjectParams.nanite_proxy_triangle_percent"></a>

#### nanite_proxy_triangle_percent

```python
@nanite_proxy_triangle_percent.setter
def nanite_proxy_triangle_percent(value: float) -> None
```

<a id="unreal.CreateMeshObjectResult"></a>