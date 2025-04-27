## DMMaterialSlot Objects

```python
class DMMaterialSlot(DMMaterialComponent)
```

A list of operations/inputs daisy chained together to produce an output.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialSlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``index`` (int32):  [Read-Only]
- ``layer_objects`` (Array[DMMaterialLayerObject]):  [Read-Only]
- ``output_connector_types`` (Map[DMMaterialPropertyType, DMMaterialSlotOutputConnectorTypes]):  [Read-Only]

<a id="unreal.DMMaterialSlot.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.DMMaterialSlot.layer_objects"></a>

#### layer_objects

```python
@property
def layer_objects() -> Array[DMMaterialLayerObject]
```

(Array[DMMaterialLayerObject]):  [Read-Only]

<a id="unreal.DMMaterialSlot.output_connector_types"></a>

#### output_connector_types

```python
@property
def output_connector_types(
) -> Map[DMMaterialPropertyType, DMMaterialSlotOutputConnectorTypes]
```

(Map[DMMaterialPropertyType, DMMaterialSlotOutputConnectorTypes]):  [Read-Only]

<a id="unreal.DMMaterialSlot.set_layer_material_property_and_replace_others"></a>

#### set_layer_material_property_and_replace_others

```python
def set_layer_material_property_and_replace_others(
        layer: DMMaterialLayerObject, property_from: DMMaterialPropertyType,
        property_to: DMMaterialPropertyType) -> bool
```

x.set_layer_material_property_and_replace_others(layer, property_from, property_to) -> bool
Sets the material property of the given layer and changes all other layers matching that property to a different one.

Args:
    layer (DMMaterialLayerObject): 
    property_from (DMMaterialPropertyType): 
    property_to (DMMaterialPropertyType): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.remove_layer"></a>

#### remove_layer

```python
def remove_layer(layer: DMMaterialLayerObject) -> bool
```

x.remove_layer(layer) -> bool
Removes the layer, if possible.

Args:
    layer (DMMaterialLayerObject): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.move_layer_before"></a>

#### move_layer_before

```python
def move_layer_before(layer: DMMaterialLayerObject,
                      before_layer: DMMaterialLayerObject = None) -> bool
```

x.move_layer_before(layer, before_layer=None) -> bool
Move Layer Before

Args:
    layer (DMMaterialLayerObject): 
    before_layer (DMMaterialLayerObject): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.move_layer_after"></a>

#### move_layer_after

```python
def move_layer_after(layer: DMMaterialLayerObject,
                     after_layer: DMMaterialLayerObject = None) -> bool
```

x.move_layer_after(layer, after_layer=None) -> bool
Move Layer After

Args:
    layer (DMMaterialLayerObject): 
    after_layer (DMMaterialLayerObject): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.move_layer"></a>

#### move_layer

```python
def move_layer(layer: DMMaterialLayerObject, new_index: int) -> bool
```

x.move_layer(layer, new_index) -> bool
Move Layer

Args:
    layer (DMMaterialLayerObject): 
    new_index (int32): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.k2_get_slots_referenced_by"></a>

#### k2_get_slots_referenced_by

```python
def k2_get_slots_referenced_by() -> Array[DMMaterialSlot]
```

x.k2_get_slots_referenced_by() -> Array[DMMaterialSlot]
Returns an array of the slots referencing this slot.

Returns:
    Array[DMMaterialSlot]:

<a id="unreal.DMMaterialSlot.get_output_connector_types_for_material_property"></a>

#### get_output_connector_types_for_material_property

```python
def get_output_connector_types_for_material_property(
        material_property: DMMaterialPropertyType) -> Array[DMValueType]
```

x.get_output_connector_types_for_material_property(material_property) -> Array[DMValueType]
Returns the output types for the last layer with the given material property.

Args:
    material_property (DMMaterialPropertyType): 

Returns:
    Array[DMValueType]:

<a id="unreal.DMMaterialSlot.get_material_model_editor_only_data"></a>

#### get_material_model_editor_only_data

```python
def get_material_model_editor_only_data(
) -> DynamicMaterialModelEditorOnlyData
```

x.get_material_model_editor_only_data() -> DynamicMaterialModelEditorOnlyData
Get Material Model Editor Only Data

Returns:
    DynamicMaterialModelEditorOnlyData:

<a id="unreal.DMMaterialSlot.get_layer"></a>

#### get_layer

```python
def get_layer(layer_index: int) -> DMMaterialLayerObject
```

x.get_layer(layer_index) -> DMMaterialLayerObject
Get Layer

Args:
    layer_index (int32): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialSlot.get_last_layer_for_material_property"></a>

#### get_last_layer_for_material_property

```python
def get_last_layer_for_material_property(
        material_property: DMMaterialPropertyType) -> DMMaterialLayerObject
```

x.get_last_layer_for_material_property(material_property) -> DMMaterialLayerObject
Useful for determining output types.

Args:
    material_property (DMMaterialPropertyType): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialSlot.get_index"></a>

#### get_index

```python
def get_index() -> int
```

x.get_index() -> int32
Returns the index of this slot in the model.

Returns:
    int32:

<a id="unreal.DMMaterialSlot.get_description"></a>

#### get_description

```python
def get_description() -> Text
```

x.get_description() -> Text
Get Description

Returns:
    Text:

<a id="unreal.DMMaterialSlot.get_all_output_connector_types"></a>

#### get_all_output_connector_types

```python
def get_all_output_connector_types() -> Set[DMValueType]
```

x.get_all_output_connector_types() -> Set[DMValueType]
Returns all possible output connector types.

Returns:
    Set[DMValueType]:

<a id="unreal.DMMaterialSlot.find_layer"></a>

#### find_layer

```python
def find_layer(base_or_mask: DMMaterialStage) -> DMMaterialLayerObject
```

x.find_layer(base_or_mask) -> DMMaterialLayerObject
Find Layer

Args:
    base_or_mask (DMMaterialStage): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialSlot.change_material_property"></a>

#### change_material_property

```python
def change_material_property(property_from: DMMaterialPropertyType,
                             property_to: DMMaterialPropertyType) -> bool
```

x.change_material_property(property_from, property_to) -> bool
Changes the material property of all matching layers to another.

Args:
    property_from (DMMaterialPropertyType): 
    property_to (DMMaterialPropertyType): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.can_remove_layer"></a>

#### can_remove_layer

```python
def can_remove_layer(layer: DMMaterialLayerObject) -> bool
```

x.can_remove_layer(layer) -> bool
Can't be removed if it is the last remaining layer.

Args:
    layer (DMMaterialLayerObject): 

Returns:
    bool:

<a id="unreal.DMMaterialSlot.bp_get_layers"></a>

#### bp_get_layers

```python
def bp_get_layers() -> Array[DMMaterialLayerObject]
```

x.bp_get_layers() -> Array[DMMaterialLayerObject]
BP Get Layers

Returns:
    Array[DMMaterialLayerObject]:

<a id="unreal.DMMaterialSlot.add_layer_with_mask"></a>

#### add_layer_with_mask

```python
def add_layer_with_mask(material_property: DMMaterialPropertyType,
                        new_base: DMMaterialStage,
                        new_mask: DMMaterialStage) -> DMMaterialLayerObject
```

x.add_layer_with_mask(material_property, new_base, new_mask) -> DMMaterialLayerObject
Adds a new layer with the specified base and mask layers.

Args:
    material_property (DMMaterialPropertyType): 
    new_base (DMMaterialStage): 
    new_mask (DMMaterialStage): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialSlot.add_layer"></a>

#### add_layer

```python
def add_layer(material_property: DMMaterialPropertyType,
              new_base: DMMaterialStage) -> DMMaterialLayerObject
```

x.add_layer(material_property, new_base) -> DMMaterialLayerObject
Adds the default layer (with specified base) based on the given material property.

Args:
    material_property (DMMaterialPropertyType): 
    new_base (DMMaterialStage): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialSlot.add_default_layer"></a>

#### add_default_layer

```python
def add_default_layer(
        material_property: DMMaterialPropertyType) -> DMMaterialLayerObject
```

x.add_default_layer(material_property) -> DMMaterialLayerObject
Adds the default layer type for this slot based on the given material property.

Args:
    material_property (DMMaterialPropertyType): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialStage"></a>