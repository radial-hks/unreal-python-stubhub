## MaterialAtom Objects

```python
class MaterialAtom(EntityAtomBase)
```

Material Atom

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpMaterial
- **File**: MaterialAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``changed_material_info`` (Array[ChangedMaterialInfo]):  [Read-Write]
- ``receives_decals`` (bool):  [Read-Write]

<a id="unreal.MaterialAtom.changed_material_info"></a>

#### changed\_material\_info

```python
@property
def changed_material_info() -> Array[ChangedMaterialInfo]
```

(Array[ChangedMaterialInfo]):  [Read-Only]

<a id="unreal.MaterialAtom.receives_decals"></a>

#### receives\_decals

```python
@property
def receives_decals() -> bool
```

(bool):  [Read-Only]

<a id="unreal.MaterialAtom.apply_material_to_component"></a>

#### apply\_material\_to\_component

```python
def apply_material_to_component(component: PrimitiveComponent,
                                material_index: int, mi_eid: int) -> bool
```

x.apply_material_to_component(component, material_index, mi_eid) -> bool
Apply Material to Component

Args:
    component (PrimitiveComponent): 
    material_index (int32): 
    mi_eid (int64): 

Returns:
    bool:

<a id="unreal.MaterialAtom.apply_material_from_data"></a>

#### apply\_material\_from\_data

```python
def apply_material_from_data() -> bool
```

x.apply_material_from_data() -> bool
Apply Material from Data

Returns:
    bool:

<a id="unreal.MIParamsAtom"></a>