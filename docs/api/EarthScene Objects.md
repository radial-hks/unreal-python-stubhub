## EarthScene Objects

```python
class EarthScene(WorldSubsystem)
```

Earth Scene

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthCore
- **File**: EarthScene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_mgr`` (EarthEntityMgr):  [Read-Only]
- ``transaction_mgr`` (EarthTransactionMgr):  [Read-Only]

<a id="unreal.EarthScene.remove_entity_by_ids"></a>

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

<a id="unreal.EarthScene.remove_entity_by_class"></a>

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

<a id="unreal.EarthScene.has_scene_begun_play"></a>

#### has\_scene\_begun\_play

```python
def has_scene_begun_play() -> bool
```

x.has_scene_begun_play() -> bool
Has Scene Begun Play

Returns:
    bool:

<a id="unreal.EarthScene.get_transaction_mgr"></a>

#### get\_transaction\_mgr

```python
def get_transaction_mgr() -> EarthTransactionMgr
```

x.get_transaction_mgr() -> EarthTransactionMgr
Get Transaction Mgr

Returns:
    EarthTransactionMgr:

<a id="unreal.EarthScene.get_entity_type_to_class"></a>

#### get\_entity\_type\_to\_class

```python
def get_entity_type_to_class() -> Map[Name, Class]
```

x.get_entity_type_to_class() -> Map[Name, type(Class)]
Get Entity Type to Class

Returns:
    Map[Name, type(Class)]:

<a id="unreal.EarthScene.get_entity_class_by_type"></a>

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

<a id="unreal.EarthScene.get_entities_by_type_bp"></a>

#### get\_entities\_by\_type\_bp

```python
def get_entities_by_type_bp(entity_type: str) -> Array[IEarthEntity]
```

x.get_entities_by_type_bp(entity_type) -> Array[IEarthEntity]
Get Entities by Type BP

Args:
    entity_type (str): 

Returns:
    Array[IEarthEntity]:

<a id="unreal.EarthScene.get_entities_by_class_bp"></a>

#### get\_entities\_by\_class\_bp

```python
def get_entities_by_class_bp(entity_class: Class) -> Array[IEarthEntity]
```

x.get_entities_by_class_bp(entity_class) -> Array[IEarthEntity]
Get Entities by Class BP

Args:
    entity_class (type(Class)): 

Returns:
    Array[IEarthEntity]:

<a id="unreal.EarthScene.get_all_entities_bp"></a>

#### get\_all\_entities\_bp

```python
def get_all_entities_bp() -> Array[IEarthEntity]
```

x.get_all_entities_bp() -> Array[IEarthEntity]
Get All Entities BP

Returns:
    Array[IEarthEntity]:

<a id="unreal.EarthScene.create_wdp_entity"></a>

#### create\_wdp\_entity

```python
def create_wdp_entity(entity_class: Class) -> IEarthEntity
```

x.create_wdp_entity(entity_class) -> IEarthEntity
Create Wdp Entity

Args:
    entity_class (type(Class)): 

Returns:
    IEarthEntity:

<a id="unreal.EarthStandardActorEntity"></a>