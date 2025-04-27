## MaterialLayersFunctionsEditorOnlyData Objects

```python
class MaterialLayersFunctionsEditorOnlyData(StructBase)
```

Material Layers Functions Editor Only Data

**C++ Source:**

- **Module**: Engine
- **File**: MaterialLayersFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``deleted_parent_layer_guids`` (Array[Guid]):  [Read-Write] List of Guids that exist in the parent material that have been explicitly deleted
  This is needed to distinguish these layers from newly added layers in the parent material
- ``layer_guids`` (Array[Guid]):  [Read-Write] Guid that identifies each layer in this stack
- ``layer_link_states`` (Array[MaterialLayerLinkState]):  [Read-Write] State of each layer's link to parent material
- ``layer_names`` (Array[Text]):  [Read-Write]
- ``layer_states`` (Array[bool]):  [Read-Write]
- ``restrict_to_blend_relatives`` (Array[bool]):  [Read-Write]
- ``restrict_to_layer_relatives`` (Array[bool]):  [Read-Write]

<a id="unreal.MaterialLayersFunctionsEditorOnlyData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.TimeStretchCurveMarker"></a>