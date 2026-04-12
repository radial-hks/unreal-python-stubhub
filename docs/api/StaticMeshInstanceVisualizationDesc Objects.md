## StaticMeshInstanceVisualizationDesc Objects

```python
class StaticMeshInstanceVisualizationDesc(TableRowBase)
```

Static Mesh Instance Visualization Desc

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassRepresentation
- **File**: MassRepresentationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meshes`` (Array[MassStaticMeshInstanceVisualizationMeshDesc]):  [Read-Write] Mesh descriptions. These will be instanced together using the same transform for each, to
  visualize the given agent.
- ``transform_offset`` (Transform):  [Read-Write] Transform to offset the static meshes if not align the mass agent transform
- ``use_transform_offset`` (bool):  [Read-Write] Boolean to enable code to transform the static meshes if not align the mass agent transform

<a id="unreal.StaticMeshInstanceVisualizationDesc.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SimDebugDataRow"></a>