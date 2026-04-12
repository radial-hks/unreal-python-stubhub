## EarthEntity Objects

```python
class EarthEntity(Object)
```

brief: Wdp场景中对象的基类，对应Unreal中的UObject

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthCore
- **File**: EarthEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EarthEntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.EarthEntity.entity_atoms"></a>

#### entity\_atoms

```python
@property
def entity_atoms() -> Array[EarthEntityAtomBase]
```

(Array[EarthEntityAtomBase]):  [Read-Only]

<a id="unreal.EarthEntity.update_graphics"></a>

#### update\_graphics

```python
def update_graphics(
        atom_changed_data: Map[Class, EarthAtomChangedProperty]) -> bool
```

x.update_graphics(atom_changed_data) -> bool
Update Graphics

Args:
    atom_changed_data (Map[type(Class), EarthAtomChangedProperty]): 

Returns:
    bool:

<a id="unreal.EarthEntity.should_redraw"></a>

#### should\_redraw

```python
def should_redraw(
        atom_changed_data: Map[Class, EarthAtomChangedProperty]) -> bool
```

x.should_redraw(atom_changed_data) -> bool
Should Redraw

Args:
    atom_changed_data (Map[type(Class), EarthAtomChangedProperty]): 

Returns:
    bool:

<a id="unreal.EarthEntity.pre_entity_removed"></a>

#### pre\_entity\_removed

```python
def pre_entity_removed() -> None
```

x.pre_entity_removed() -> None
Pre Entity Removed

<a id="unreal.EarthEntity.pre_delete_entity_operation"></a>

#### pre\_delete\_entity\_operation

```python
def pre_delete_entity_operation() -> None
```

x.pre_delete_entity_operation() -> None
Pre Delete Entity Operation

<a id="unreal.EarthEntity.post_entity_created"></a>

#### post\_entity\_created

```python
def post_entity_created() -> None
```

x.post_entity_created() -> None
Post Entity Created

<a id="unreal.EarthEntity.notify2d_entity_mouse_event"></a>

#### notify2d\_entity\_mouse\_event

```python
def notify2d_entity_mouse_event(
        mouse_pos: Vector2D, event_type: Earth2DEntityMouseEventType) -> None
```

x.notify2d_entity_mouse_event(mouse_pos, event_type) -> None
Notify 2DEntity Mouse Event

Args:
    mouse_pos (Vector2D): 
    event_type (Earth2DEntityMouseEventType):

<a id="unreal.EarthEntity.handle_entity_operations"></a>

#### handle\_entity\_operations

```python
def handle_entity_operations(
        operations: EarthJsonObjectWrapper,
        operate_entity_time: EarthOperateEntityTime) -> bool
```

x.handle_entity_operations(operations, operate_entity_time) -> bool
Handle Entity Operations

Args:
    operations (EarthJsonObjectWrapper): 
    operate_entity_time (EarthOperateEntityTime): 

Returns:
    bool:

<a id="unreal.EarthEntity.get_entity_type"></a>

#### get\_entity\_type

```python
def get_entity_type() -> Name
```

x.get_entity_type() -> Name
Get Entity Type

Returns:
    Name:

<a id="unreal.EarthEntity.get_entity_instance_flags"></a>

#### get\_entity\_instance\_flags

```python
def get_entity_instance_flags() -> EarthEntityInstanceFlags
```

x.get_entity_instance_flags() -> EarthEntityInstanceFlags
Get Entity Instance Flags

Returns:
    EarthEntityInstanceFlags:

<a id="unreal.EarthEntity.get_entity_id"></a>

#### get\_entity\_id

```python
def get_entity_id() -> int
```

x.get_entity_id() -> int64
Get Entity Id

Returns:
    int64:

<a id="unreal.EarthEntity.get_entity_define_flags"></a>

#### get\_entity\_define\_flags

```python
def get_entity_define_flags() -> EarthEntityDefineFlags
```

x.get_entity_define_flags() -> EarthEntityDefineFlags
Get Entity Define Flags

Returns:
    EarthEntityDefineFlags:

<a id="unreal.EarthEntity.get_entity_class"></a>

#### get\_entity\_class

```python
def get_entity_class() -> Class
```

x.get_entity_class() -> type(Class)
Get Entity Class

Returns:
    type(Class):

<a id="unreal.EarthEntity.get_entity_category"></a>

#### get\_entity\_category

```python
def get_entity_category() -> EarthCategory
```

x.get_entity_category() -> EarthCategory
Get Entity Category

Returns:
    EarthCategory:

<a id="unreal.EarthEntity.get_entity_atoms_class"></a>

#### get\_entity\_atoms\_class

```python
def get_entity_atoms_class() -> Set[Class]
```

x.get_entity_atoms_class() -> Set[type(Class)]
~ Begin Wdp Entity Interface

Returns:
    Set[type(Class)]:

<a id="unreal.EarthEntity.get_entity_atom_by_class"></a>

#### get\_entity\_atom\_by\_class

```python
def get_entity_atom_by_class(atom_class: Class) -> EarthEntityAtomBase
```

x.get_entity_atom_by_class(atom_class) -> EarthEntityAtomBase
Get Entity Atom by Class

Args:
    atom_class (type(Class)): 

Returns:
    EarthEntityAtomBase:

<a id="unreal.EarthEntity.get_bounding_box"></a>

#### get\_bounding\_box

```python
def get_bounding_box() -> Box
```

x.get_bounding_box() -> Box
Get Bounding Box

Returns:
    Box:

<a id="unreal.EarthEntity.get_all_entity_atoms"></a>

#### get\_all\_entity\_atoms

```python
def get_all_entity_atoms() -> Array[EarthEntityAtomBase]
```

x.get_all_entity_atoms() -> Array[EarthEntityAtomBase]
Get All Entity Atoms

Returns:
    Array[EarthEntityAtomBase]:

<a id="unreal.EarthEntity.entity_init"></a>

#### entity\_init

```python
def entity_init(entity_init_params: EarthEntityInitParams) -> bool
```

x.entity_init(entity_init_params) -> bool
Entity Init

Args:
    entity_init_params (EarthEntityInitParams): 

Returns:
    bool:

<a id="unreal.EarthEntity.destroy_graphics"></a>

#### destroy\_graphics

```python
def destroy_graphics() -> bool
```

x.destroy_graphics() -> bool
Destroy Graphics

Returns:
    bool:

<a id="unreal.EarthEntity.create_graphics"></a>

#### create\_graphics

```python
def create_graphics() -> bool
```

x.create_graphics() -> bool
Create Graphics

Returns:
    bool:

<a id="unreal.EarthEntityAtomBase"></a>