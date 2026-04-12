## WdpScene Objects

```python
class WdpScene(WorldSubsystem)
```

Wdp Scene

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: WdpScene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_mgr`` (WdpEntityMgr):  [Read-Only]
- ``transaction_mgr`` (WdpTransactionMgr):  [Read-Only]

<a id="unreal.WdpScene.save_wdp_scene"></a>

#### save\_wdp\_scene

```python
def save_wdp_scene() -> Optional[WdpJsonObjectWrapper]
```

x.save_wdp_scene() -> WdpJsonObjectWrapper or None
Save Wdp Scene

Returns:
    WdpJsonObjectWrapper or None: 

    out_scene_json_object (WdpJsonObjectWrapper):

<a id="unreal.WdpScene.remove_entity_by_ids"></a>

#### remove\_entity\_by\_ids

```python
def remove_entity_by_ids(ids: Array[int]) -> bool
```

x.remove_entity_by_ids(ids) -> bool
Remove Entity by Ids

Args:
    ids (Array[int64]): 

Returns:
    bool:

<a id="unreal.WdpScene.remove_entity_by_id"></a>

#### remove\_entity\_by\_id

```python
def remove_entity_by_id(id: int) -> bool
```

x.remove_entity_by_id(id) -> bool
Remove Entity by Id

Args:
    id (int64): 

Returns:
    bool:

<a id="unreal.WdpScene.remove_entity_by_class"></a>

#### remove\_entity\_by\_class

```python
def remove_entity_by_class(entity_class: Class) -> bool
```

x.remove_entity_by_class(entity_class) -> bool
Remove Entity by Class

Args:
    entity_class (type(Class)): 

Returns:
    bool:

<a id="unreal.WdpScene.load_wdp_scene"></a>

#### load\_wdp\_scene

```python
def load_wdp_scene(scene_json_object: WdpJsonObjectWrapper) -> bool
```

x.load_wdp_scene(scene_json_object) -> bool
Load Wdp Scene

Args:
    scene_json_object (WdpJsonObjectWrapper): 

Returns:
    bool:

<a id="unreal.WdpScene.has_scene_begun_play"></a>

#### has\_scene\_begun\_play

```python
def has_scene_begun_play() -> bool
```

x.has_scene_begun_play() -> bool
Has Scene Begun Play

Returns:
    bool:

<a id="unreal.WdpScene.get_transaction_mgr"></a>

#### get\_transaction\_mgr

```python
def get_transaction_mgr() -> WdpTransactionMgr
```

x.get_transaction_mgr() -> WdpTransactionMgr
Get Transaction Mgr

Returns:
    WdpTransactionMgr:

<a id="unreal.WdpScene.get_entity_type_to_class"></a>

#### get\_entity\_type\_to\_class

```python
def get_entity_type_to_class() -> Map[Name, Class]
```

x.get_entity_type_to_class() -> Map[Name, type(Class)]
Get Entity Type to Class

Returns:
    Map[Name, type(Class)]:

<a id="unreal.WdpScene.get_entity_class_by_type"></a>

#### get\_entity\_class\_by\_type

```python
def get_entity_class_by_type(entity_type: str) -> Class
```

x.get_entity_class_by_type(entity_type) -> type(Class)
Get Entity Class by Type

Args:
    entity_type (str): 

Returns:
    type(Class):

<a id="unreal.WdpScene.get_entity_by_id_bp"></a>

#### get\_entity\_by\_id\_bp

```python
def get_entity_by_id_bp(id: int) -> IWdpEntity
```

x.get_entity_by_id_bp(id) -> IWdpEntity
Get Entity by Id BP

Args:
    id (int64): 

Returns:
    IWdpEntity:

<a id="unreal.WdpScene.get_entities_by_type_bp"></a>

#### get\_entities\_by\_type\_bp

```python
def get_entities_by_type_bp(entity_type: str) -> Array[IWdpEntity]
```

x.get_entities_by_type_bp(entity_type) -> Array[IWdpEntity]
Get Entities by Type BP

Args:
    entity_type (str): 

Returns:
    Array[IWdpEntity]:

<a id="unreal.WdpScene.get_entities_by_class_bp"></a>

#### get\_entities\_by\_class\_bp

```python
def get_entities_by_class_bp(entity_class: Class) -> Array[IWdpEntity]
```

x.get_entities_by_class_bp(entity_class) -> Array[IWdpEntity]
Get Entities by Class BP

Args:
    entity_class (type(Class)): 

Returns:
    Array[IWdpEntity]:

<a id="unreal.WdpScene.get_all_entities_bp"></a>

#### get\_all\_entities\_bp

```python
def get_all_entities_bp() -> Array[IWdpEntity]
```

x.get_all_entities_bp() -> Array[IWdpEntity]
Get All Entities BP

Returns:
    Array[IWdpEntity]:

<a id="unreal.WdpScene.create_wdp_entity"></a>

#### create\_wdp\_entity

```python
def create_wdp_entity(entity_class: Class) -> IWdpEntity
```

x.create_wdp_entity(entity_class) -> IWdpEntity
Create Wdp Entity

Args:
    entity_class (type(Class)): 

Returns:
    IWdpEntity:

<a id="unreal.WdpScene.create_wdp_actor_entity"></a>

#### create\_wdp\_actor\_entity

```python
def create_wdp_actor_entity(entity_class: Class) -> IWdpEntity
```

x.create_wdp_actor_entity(entity_class) -> IWdpEntity
Create Wdp Actor Entity

Args:
    entity_class (type(Class)): 

Returns:
    IWdpEntity:

<a id="unreal.WdpScene.clear_scene"></a>

#### clear\_scene

```python
def clear_scene(entity_type_to_filter: Set[Name]) -> bool
```

x.clear_scene(entity_type_to_filter) -> bool
Clear Scene

Args:
    entity_type_to_filter (Set[Name]): 

Returns:
    bool:

<a id="unreal.WdpStandardEntity"></a>