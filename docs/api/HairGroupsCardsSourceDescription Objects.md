## HairGroupsCardsSourceDescription Objects

```python
class HairGroupsCardsSourceDescription(StructBase)
```

Hair Groups Cards Source Description

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetCards.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cards_info`` (HairGroupCardsInfo):  [Read-Only]
- ``group_index`` (int32):  [Read-Write] Group index on which this cards geometry will be used (#hair_todo: change this to be a dropdown selection menu in FHairLODSettings instead)
- ``guide_type`` (HairCardsGuideType):  [Read-Write]
- ``imported_mesh`` (StaticMesh):  [Read-Write]
- ``lod_index`` (int32):  [Read-Write] LOD on which this cards geometry will be used. -1 means not used  (#hair_todo: change this to be a dropdown selection menu in FHairLODSettings instead)
- ``textures`` (HairGroupCardsTextures):  [Read-Write]

<a id="unreal.HairGroupsCardsSourceDescription.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairLODSettings"></a>