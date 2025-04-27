## NDIStaticMesh_SourceMode Objects

```python
class NDIStaticMesh_SourceMode(EnumBase)
```

ENDIStatic Mesh Source Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceStaticMesh.h

<a id="unreal.NDIStaticMesh_SourceMode.DEFAULT"></a>

#### DEFAULT

0: Default behavior follows the order of.
- Use "Source" when specified (either set explicitly or via blueprint with Set Niagara Static Mesh Component).
- Use Mesh Parameter Binding if valid
- Find Static Mesh Component, Attached Actor, Attached Component
- Falls back to 'Default Mesh' specified on the data interface

<a id="unreal.NDIStaticMesh_SourceMode.SOURCE"></a>

#### SOURCE

1: Only use "Source" (either set explicitly or via blueprint with Set Niagara Static Mesh Component).

<a id="unreal.NDIStaticMesh_SourceMode.ATTACH_PARENT"></a>

#### ATTACH_PARENT

2: Only use the parent actor or component the system is attached to.

<a id="unreal.NDIStaticMesh_SourceMode.DEFAULT_MESH_ONLY"></a>

#### DEFAULT_MESH_ONLY

3: Only use the "Default Mesh" specified.

<a id="unreal.NDIStaticMesh_SourceMode.MESH_PARAMETER_BINDING"></a>

#### MESH_PARAMETER_BINDING

4: Only use the mesh parameter binding.

<a id="unreal.NDIObjectPropertyReaderSourceMode"></a>