## OptimusSkinnedMeshVertexAttributeDataProvider Objects

```python
class OptimusSkinnedMeshVertexAttributeDataProvider(ComputeDataProvider)
```

Compute Framework Data Provider for reading skeletal mesh.

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusDataInterfaceSkinnedMeshVertexAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_name`` (Name):  [Read-Write]
- ``skinned_mesh_component`` (SkinnedMeshComponent):  [Read-Write]

<a id="unreal.OptimusSkinnedMeshVertexAttributeDataProvider.skinned_mesh_component"></a>

#### skinned_mesh_component

```python
@property
def skinned_mesh_component() -> SkinnedMeshComponent
```

(SkinnedMeshComponent):  [Read-Write]

<a id="unreal.OptimusSkinnedMeshVertexAttributeDataProvider.skinned_mesh_component"></a>

#### skinned_mesh_component

```python
@skinned_mesh_component.setter
def skinned_mesh_component(value: SkinnedMeshComponent) -> None
```

<a id="unreal.OptimusSkinnedMeshVertexAttributeDataProvider.attribute_name"></a>

#### attribute_name

```python
@property
def attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.OptimusSkinnedMeshVertexAttributeDataProvider.attribute_name"></a>

#### attribute_name

```python
@attribute_name.setter
def attribute_name(value: Name) -> None
```

<a id="unreal.OptimusSkinWeightsAsVertexMaskDataProvider"></a>