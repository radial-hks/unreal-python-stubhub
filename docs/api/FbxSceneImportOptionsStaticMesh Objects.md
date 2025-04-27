## FbxSceneImportOptionsStaticMesh Objects

```python
class FbxSceneImportOptionsStaticMesh(Object)
```

Fbx Scene Import Options Static Mesh

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxSceneImportOptionsStaticMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_generate_collision`` (bool):  [Read-Write] If checked, collision will automatically be generated (ignored if custom collision is imported or used).
- ``build_reversed_index_buffer`` (bool):  [Read-Write]
- ``generate_lightmap_u_vs`` (bool):  [Read-Write]
- ``normal_generation_method`` (FBXSceneNormalGenerationMethod):  [Read-Write] Use the MikkTSpace tangent space generator for generating normals and tangents on the mesh
- ``normal_import_method`` (FBXSceneNormalImportMethod):  [Read-Write] Enabling this option will read the tangents(tangent,binormal,normal) from FBX file instead of generating them automatically.
- ``one_convex_hull_per_ucx`` (bool):  [Read-Write] If checked, one convex hull per UCX_ prefixed collision mesh will be generated instead of decomposing into multiple hulls
- ``remove_degenerates`` (bool):  [Read-Write] Disabling this option will keep degenerate triangles found.  In general you should leave this option on.
- ``vertex_color_import_option`` (FbxSceneVertexColorImportOption):  [Read-Write] Specify how vertex colors should be imported
- ``vertex_override_color`` (Color):  [Read-Write] Specify override color in the case that VertexColorImportOption is set to Override

<a id="unreal.FbxSkeletalMeshImportData"></a>