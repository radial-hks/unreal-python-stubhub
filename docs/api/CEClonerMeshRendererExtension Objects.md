## CEClonerMeshRendererExtension Objects

```python
class CEClonerMeshRendererExtension(CEClonerExtensionBase)
```

Extension dealing with mesh rendering options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerMeshRendererExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_meshes`` (Array[StaticMesh]):  [Read-Write] When nothing is attached to the cloner, these meshes are used as default
- ``mesh_cast_shadows`` (bool):  [Read-Write] Whether clones cast shadow, disabling will result in better performance
- ``mesh_facing_mode`` (NiagaraMeshFacingMode):  [Read-Write] Mode to indicate how clones facing is determined
- ``mesh_render_mode`` (CEClonerMeshRenderMode):  [Read-Write] Indicates how we select the mesh to render on each clones
- ``override_material`` (MaterialInterface):  [Read-Write] The override materials that will be set instead of meshes materials, bVisualizeEffectors must be disabled
- ``sort_translucent_particles`` (bool):  [Read-Write] Sort particles by depth when it has a translucent material, this will avoid flickering artifacts from appearing
- ``use_override_material`` (bool):  [Read-Write] Whether to override meshes materials with another material
- ``visualize_effectors`` (bool):  [Read-Write] Override materials to show effectors applied on this cloner based on their color property

<a id="unreal.CEClonerMeshRendererExtension.set_visualize_effectors"></a>

#### set_visualize_effectors

```python
def set_visualize_effectors(visualize: bool) -> None
```

x.set_visualize_effectors(visualize) -> None
Set Visualize Effectors

Args:
    visualize (bool):

<a id="unreal.CEClonerMeshRendererExtension.set_use_override_material"></a>

#### set_use_override_material

```python
def set_use_override_material(override: bool) -> None
```

x.set_use_override_material(override) -> None
Set Use Override Material

Args:
    override (bool):

<a id="unreal.CEClonerMeshRendererExtension.set_sort_translucent_particles"></a>

#### set_sort_translucent_particles

```python
def set_sort_translucent_particles(sort: bool) -> None
```

x.set_sort_translucent_particles(sort) -> None
Set Sort Translucent Particles

Args:
    sort (bool):

<a id="unreal.CEClonerMeshRendererExtension.set_override_material"></a>

#### set_override_material

```python
def set_override_material(material: MaterialInterface) -> None
```

x.set_override_material(material) -> None
Set Override Material

Args:
    material (MaterialInterface):

<a id="unreal.CEClonerMeshRendererExtension.set_mesh_render_mode"></a>

#### set_mesh_render_mode

```python
def set_mesh_render_mode(mode: CEClonerMeshRenderMode) -> None
```

x.set_mesh_render_mode(mode) -> None
Set Mesh Render Mode

Args:
    mode (CEClonerMeshRenderMode):

<a id="unreal.CEClonerMeshRendererExtension.set_mesh_facing_mode"></a>

#### set_mesh_facing_mode

```python
def set_mesh_facing_mode(mode: NiagaraMeshFacingMode) -> None
```

x.set_mesh_facing_mode(mode) -> None
Set Mesh Facing Mode

Args:
    mode (NiagaraMeshFacingMode):

<a id="unreal.CEClonerMeshRendererExtension.set_mesh_cast_shadows"></a>

#### set_mesh_cast_shadows

```python
def set_mesh_cast_shadows(inb_cast_shadows: bool) -> None
```

x.set_mesh_cast_shadows(inb_cast_shadows) -> None
Set Mesh Cast Shadows

Args:
    inb_cast_shadows (bool):

<a id="unreal.CEClonerMeshRendererExtension.set_default_meshes"></a>

#### set_default_meshes

```python
def set_default_meshes(meshes: Array[StaticMesh]) -> None
```

x.set_default_meshes(meshes) -> None
Set Default Meshes

Args:
    meshes (Array[StaticMesh]):

<a id="unreal.CEClonerMeshRendererExtension.get_visualize_effectors"></a>

#### get_visualize_effectors

```python
def get_visualize_effectors() -> bool
```

x.get_visualize_effectors() -> bool
Get Visualize Effectors

Returns:
    bool:

<a id="unreal.CEClonerMeshRendererExtension.get_use_override_material"></a>

#### get_use_override_material

```python
def get_use_override_material() -> bool
```

x.get_use_override_material() -> bool
Get Use Override Material

Returns:
    bool:

<a id="unreal.CEClonerMeshRendererExtension.get_sort_translucent_particles"></a>

#### get_sort_translucent_particles

```python
def get_sort_translucent_particles() -> bool
```

x.get_sort_translucent_particles() -> bool
Get Sort Translucent Particles

Returns:
    bool:

<a id="unreal.CEClonerMeshRendererExtension.get_override_material"></a>

#### get_override_material

```python
def get_override_material() -> MaterialInterface
```

x.get_override_material() -> MaterialInterface
Get Override Material

Returns:
    MaterialInterface:

<a id="unreal.CEClonerMeshRendererExtension.get_mesh_render_mode"></a>

#### get_mesh_render_mode

```python
def get_mesh_render_mode() -> CEClonerMeshRenderMode
```

x.get_mesh_render_mode() -> CEClonerMeshRenderMode
Get Mesh Render Mode

Returns:
    CEClonerMeshRenderMode:

<a id="unreal.CEClonerMeshRendererExtension.get_mesh_facing_mode"></a>

#### get_mesh_facing_mode

```python
def get_mesh_facing_mode() -> NiagaraMeshFacingMode
```

x.get_mesh_facing_mode() -> NiagaraMeshFacingMode
Get Mesh Facing Mode

Returns:
    NiagaraMeshFacingMode:

<a id="unreal.CEClonerMeshRendererExtension.get_mesh_cast_shadows"></a>

#### get_mesh_cast_shadows

```python
def get_mesh_cast_shadows() -> bool
```

x.get_mesh_cast_shadows() -> bool
Get Mesh Cast Shadows

Returns:
    bool:

<a id="unreal.CEClonerMeshRendererExtension.get_default_meshes"></a>

#### get_default_meshes

```python
def get_default_meshes() -> Array[StaticMesh]
```

x.get_default_meshes() -> Array[StaticMesh]
Get Default Meshes

Returns:
    Array[StaticMesh]: 

    out_meshes (Array[StaticMesh]):

<a id="unreal.CEClonerProgressExtension"></a>