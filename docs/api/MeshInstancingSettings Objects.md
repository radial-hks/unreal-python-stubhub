## MeshInstancingSettings Objects

```python
class MeshInstancingSettings(StructBase)
```

Mesh instance-replacement settings

**C++ Source:**

- **Module**: Engine
- **File**: MeshInstancingSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_class_to_use`` (type(Class)):  [Read-Write] The actor class to attach new instance static mesh components to
- ``instance_replacement_threshold`` (int32):  [Read-Write] The number of static mesh instances needed before a mesh is replaced with an instanced version
- ``ism_component_to_use`` (type(Class)):  [Read-Write] Whether to use the Instanced Static Mesh Compoment or the Hierarchical Instanced Static Mesh Compoment
- ``skip_meshes_with_vertex_colors`` (bool):  [Read-Write] Whether to skip the conversion to an instanced static mesh for meshes with vertex colors.
  Instanced static meshes do not support vertex colors per-instance, so conversion will lose
  this data.
- ``use_hlod_volumes`` (bool):  [Read-Write] Whether split up instanced static mesh components based on their intersection with HLOD volumes

<a id="unreal.MeshInstancingSettings.__init__"></a>

#### __init__

```python
def __init__(actor_class_to_use: Class = None,
             instance_replacement_threshold: int = 0,
             skip_meshes_with_vertex_colors: bool = False,
             use_hlod_volumes: bool = False,
             ism_component_to_use: Class = None) -> None
```

<a id="unreal.MeshInstancingSettings.actor_class_to_use"></a>

#### actor_class_to_use

```python
@property
def actor_class_to_use() -> Class
```

(type(Class)):  [Read-Write] The actor class to attach new instance static mesh components to

<a id="unreal.MeshInstancingSettings.actor_class_to_use"></a>

#### actor_class_to_use

```python
@actor_class_to_use.setter
def actor_class_to_use(value: Class) -> None
```

<a id="unreal.MeshInstancingSettings.instance_replacement_threshold"></a>

#### instance_replacement_threshold

```python
@property
def instance_replacement_threshold() -> int
```

(int32):  [Read-Write] The number of static mesh instances needed before a mesh is replaced with an instanced version

<a id="unreal.MeshInstancingSettings.instance_replacement_threshold"></a>

#### instance_replacement_threshold

```python
@instance_replacement_threshold.setter
def instance_replacement_threshold(value: int) -> None
```

<a id="unreal.MeshInstancingSettings.skip_meshes_with_vertex_colors"></a>

#### skip_meshes_with_vertex_colors

```python
@property
def skip_meshes_with_vertex_colors() -> bool
```

(bool):  [Read-Write] Whether to skip the conversion to an instanced static mesh for meshes with vertex colors.
Instanced static meshes do not support vertex colors per-instance, so conversion will lose
this data.

<a id="unreal.MeshInstancingSettings.skip_meshes_with_vertex_colors"></a>

#### skip_meshes_with_vertex_colors

```python
@skip_meshes_with_vertex_colors.setter
def skip_meshes_with_vertex_colors(value: bool) -> None
```

<a id="unreal.MeshInstancingSettings.use_hlod_volumes"></a>

#### use_hlod_volumes

```python
@property
def use_hlod_volumes() -> bool
```

(bool):  [Read-Write] Whether split up instanced static mesh components based on their intersection with HLOD volumes

<a id="unreal.MeshInstancingSettings.use_hlod_volumes"></a>

#### use_hlod_volumes

```python
@use_hlod_volumes.setter
def use_hlod_volumes(value: bool) -> None
```

<a id="unreal.MeshInstancingSettings.ism_component_to_use"></a>

#### ism_component_to_use

```python
@property
def ism_component_to_use() -> Class
```

(type(Class)):  [Read-Write] Whether to use the Instanced Static Mesh Compoment or the Hierarchical Instanced Static Mesh Compoment

<a id="unreal.MeshInstancingSettings.ism_component_to_use"></a>

#### ism_component_to_use

```python
@ism_component_to_use.setter
def ism_component_to_use(value: Class) -> None
```

<a id="unreal.MeshReductionSettings"></a>