## SkeletalMaterial Objects

```python
class SkeletalMaterial(StructBase)
```

Skeletal Material

**C++ Source:**

- **Module**: Engine
- **File**: SkinnedAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``imported_material_slot_name`` (Name):  [Read-Only] This name should be use when we re-import a skeletal mesh so we can order the Materials array like it should be
- ``material_interface`` (MaterialInterface):  [Read-Write]
- ``material_slot_name`` (Name):  [Read-Write] This name should be use by the gameplay to avoid error if the skeletal mesh Materials array topology change
- ``uv_channel_data`` (MeshUVChannelInfo):  [Read-Only] Data used for texture streaming relative to each UV channels.

<a id="unreal.SkeletalMaterial.__init__"></a>

#### __init__

```python
def __init__(material_interface: MaterialInterface = None,
             material_slot_name: Name = "None",
             uv_channel_data: MeshUVChannelInfo = []) -> None
```

<a id="unreal.SkeletalMaterial.material_interface"></a>

#### material_interface

```python
@property
def material_interface() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.SkeletalMaterial.material_interface"></a>

#### material_interface

```python
@material_interface.setter
def material_interface(value: MaterialInterface) -> None
```

<a id="unreal.SkeletalMaterial.material_slot_name"></a>

#### material_slot_name

```python
@property
def material_slot_name() -> Name
```

(Name):  [Read-Write] This name should be use by the gameplay to avoid error if the skeletal mesh Materials array topology change

<a id="unreal.SkeletalMaterial.material_slot_name"></a>

#### material_slot_name

```python
@material_slot_name.setter
def material_slot_name(value: Name) -> None
```

<a id="unreal.SkeletalMaterial.uv_channel_data"></a>

#### uv_channel_data

```python
@property
def uv_channel_data() -> MeshUVChannelInfo
```

(MeshUVChannelInfo):  [Read-Only] Data used for texture streaming relative to each UV channels.

<a id="unreal.SoundClassProperties"></a>