## WdpEntity Objects

```python
class WdpEntity(Object)
```

brief: Wdp场景中对象的基类，对应Unreal中的UObject

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: WdpEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.WdpEntity.entity_atoms"></a>

#### entity\_atoms

```python
@property
def entity_atoms() -> Array[EntityAtomBase]
```

(Array[EntityAtomBase]):  [Read-Only]

<a id="unreal.WdpEntity.update_graphics"></a>

#### update\_graphics

```python
def update_graphics(
        atom_changed_data: Map[Class, AtomChangedProperty]) -> bool
```

x.update_graphics(atom_changed_data) -> bool
Update Graphics

Args:
    atom_changed_data (Map[type(Class), AtomChangedProperty]): 

Returns:
    bool:

<a id="unreal.WdpEntity.should_redraw"></a>

#### should\_redraw

```python
def should_redraw(atom_changed_data: Map[Class, AtomChangedProperty]) -> bool
```

x.should_redraw(atom_changed_data) -> bool
Should Redraw

Args:
    atom_changed_data (Map[type(Class), AtomChangedProperty]): 

Returns:
    bool:

<a id="unreal.WdpEntity.pre_entity_removed"></a>

#### pre\_entity\_removed

```python
def pre_entity_removed() -> None
```

x.pre_entity_removed() -> None
Pre Entity Removed

<a id="unreal.WdpEntity.pre_delete_entity_operation"></a>

#### pre\_delete\_entity\_operation

```python
def pre_delete_entity_operation() -> None
```

x.pre_delete_entity_operation() -> None
Pre Delete Entity Operation

<a id="unreal.WdpEntity.post_entity_created"></a>

#### post\_entity\_created

```python
def post_entity_created() -> None
```

x.post_entity_created() -> None
Post Entity Created

<a id="unreal.WdpEntity.notify2d_entity_mouse_event"></a>

#### notify2d\_entity\_mouse\_event

```python
def notify2d_entity_mouse_event(
    mouse_pos: Vector2D,
    event_type: E2DEntityMouseEventType,
    button_type: E2DEntityMouseButtonType = E2DEntityMouseButtonType.
    LEFT_MOUSE_BUTTON
) -> None
```

x.notify2d_entity_mouse_event(mouse_pos, event_type, button_type=E2DEntityMouseButtonType.LEFT_MOUSE_BUTTON) -> None
Notify 2DEntity Mouse Event

Args:
    mouse_pos (Vector2D): 
    event_type (E2DEntityMouseEventType): 
    button_type (E2DEntityMouseButtonType):

<a id="unreal.WdpEntity.handle_entity_operations"></a>

#### handle\_entity\_operations

```python
def handle_entity_operations(operations: WdpJsonObjectWrapper,
                             operate_entity_time: OperateEntityTime) -> bool
```

x.handle_entity_operations(operations, operate_entity_time) -> bool
Handle Entity Operations

Args:
    operations (WdpJsonObjectWrapper): 
    operate_entity_time (OperateEntityTime): 

Returns:
    bool:

<a id="unreal.WdpEntity.get_entity_type"></a>

#### get\_entity\_type

```python
def get_entity_type() -> Name
```

x.get_entity_type() -> Name
Get Entity Type

Returns:
    Name:

<a id="unreal.WdpEntity.get_entity_instance_flags"></a>

#### get\_entity\_instance\_flags

```python
def get_entity_instance_flags() -> EntityInstanceFlags
```

x.get_entity_instance_flags() -> EntityInstanceFlags
Get Entity Instance Flags

Returns:
    EntityInstanceFlags:

<a id="unreal.WdpEntity.get_entity_id"></a>

#### get\_entity\_id

```python
def get_entity_id() -> int
```

x.get_entity_id() -> int64
Get Entity Id

Returns:
    int64:

<a id="unreal.WdpEntity.get_entity_define_flags"></a>

#### get\_entity\_define\_flags

```python
def get_entity_define_flags() -> EntityDefineFlags
```

x.get_entity_define_flags() -> EntityDefineFlags
Get Entity Define Flags

Returns:
    EntityDefineFlags:

<a id="unreal.WdpEntity.get_entity_class"></a>

#### get\_entity\_class

```python
def get_entity_class() -> Class
```

x.get_entity_class() -> type(Class)
Get Entity Class

Returns:
    type(Class):

<a id="unreal.WdpEntity.get_entity_category"></a>

#### get\_entity\_category

```python
def get_entity_category() -> WdpCategory
```

x.get_entity_category() -> WdpCategory
Get Entity Category

Returns:
    WdpCategory:

<a id="unreal.WdpEntity.get_entity_atoms_class"></a>

#### get\_entity\_atoms\_class

```python
def get_entity_atoms_class() -> Set[Class]
```

x.get_entity_atoms_class() -> Set[type(Class)]
~ Begin Wdp Entity Interface

Returns:
    Set[type(Class)]:

<a id="unreal.WdpEntity.get_entity_atom_by_class"></a>

#### get\_entity\_atom\_by\_class

```python
def get_entity_atom_by_class(atom_class: Class) -> EntityAtomBase
```

x.get_entity_atom_by_class(atom_class) -> EntityAtomBase
Get Entity Atom by Class

Args:
    atom_class (type(Class)): 

Returns:
    EntityAtomBase:

<a id="unreal.WdpEntity.get_bounding_box"></a>

#### get\_bounding\_box

```python
def get_bounding_box() -> Box
```

x.get_bounding_box() -> Box
Get Bounding Box

Returns:
    Box:

<a id="unreal.WdpEntity.get_all_entity_atoms"></a>

#### get\_all\_entity\_atoms

```python
def get_all_entity_atoms() -> Array[EntityAtomBase]
```

x.get_all_entity_atoms() -> Array[EntityAtomBase]
Get All Entity Atoms

Returns:
    Array[EntityAtomBase]:

<a id="unreal.WdpEntity.entity_init"></a>

#### entity\_init

```python
def entity_init(entity_init_params: EntityInitParams) -> bool
```

x.entity_init(entity_init_params) -> bool
Entity Init

Args:
    entity_init_params (EntityInitParams): 

Returns:
    bool:

<a id="unreal.WdpEntity.destroy_graphics"></a>

#### destroy\_graphics

```python
def destroy_graphics() -> bool
```

x.destroy_graphics() -> bool
Destroy Graphics

Returns:
    bool:

<a id="unreal.WdpEntity.create_graphics"></a>

#### create\_graphics

```python
def create_graphics() -> bool
```

x.create_graphics() -> bool
Create Graphics

Returns:
    bool:

<a id="unreal.IWdpEntity"></a>