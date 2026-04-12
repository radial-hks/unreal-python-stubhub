## WdpSceneAPI Objects

```python
class WdpSceneAPI(StandardApiClassBase)
```

Wdp Scene API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

<a id="unreal.WdpSceneAPI.update_entities"></a>

#### update\_entities

```python
def update_entities(
        create_entity_params: UpdateEntityParams) -> Optional[ResultBase]
```

x.update_entities(create_entity_params) -> ResultBase or None
Update Entities

Args:
    create_entity_params (UpdateEntityParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSceneAPI.save_scene"></a>

#### save\_scene

```python
def save_scene(in_: SaveSceneParams) -> Optional[ResultBase]
```

x.save_scene(in_) -> ResultBase or None
Save Scene

Args:
    in_ (SaveSceneParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSceneAPI.remove_entity_by_types"></a>

#### remove\_entity\_by\_types

```python
def remove_entity_by_types(
        remove_entity_params: RemoveEntityByTypesParams
) -> Optional[ResultBase]
```

x.remove_entity_by_types(remove_entity_params) -> ResultBase or None
Remove Entity by Types

Args:
    remove_entity_params (RemoveEntityByTypesParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSceneAPI.remove_entity_by_eids"></a>

#### remove\_entity\_by\_eids

```python
def remove_entity_by_eids(
        remove_entity_params: RemoveEntityParams) -> Optional[ResultBase]
```

x.remove_entity_by_eids(remove_entity_params) -> ResultBase or None
Remove Entity by Eids

Args:
    remove_entity_params (RemoveEntityParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSceneAPI.merge_scene"></a>

#### merge\_scene

```python
def merge_scene(in_: MergeSceneParams) -> Optional[ResultBase]
```

x.merge_scene(in_) -> ResultBase or None
Merge Scene

Args:
    in_ (MergeSceneParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSceneAPI.load_scene"></a>

#### load\_scene

```python
def load_scene(in_: SaveSceneParams) -> Optional[ResultBase]
```

x.load_scene(in_) -> ResultBase or None
Load Scene

Args:
    in_ (SaveSceneParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSceneAPI.get_entity_type_by_eids"></a>

#### get\_entity\_type\_by\_eids

```python
def get_entity_type_by_eids(
        get_entity_type_params: EidArrayParams) -> Optional[EntityTypesResult]
```

x.get_entity_type_by_eids(get_entity_type_params) -> EntityTypesResult or None
Get Entity Type by Eids

Args:
    get_entity_type_params (EidArrayParams): 

Returns:
    EntityTypesResult or None: 

    out_result (EntityTypesResult):

<a id="unreal.WdpSceneAPI.get_entities_data"></a>

#### get\_entities\_data

```python
def get_entities_data(in_: GetEntityDataParams) -> Optional[EntityDataResult]
```

x.get_entities_data(in_) -> EntityDataResult or None
Get Entities Data

Args:
    in_ (GetEntityDataParams): 

Returns:
    EntityDataResult or None: 

    out_result (EntityDataResult):

<a id="unreal.WdpSceneAPI.get_entities_bound"></a>

#### get\_entities\_bound

```python
def get_entities_bound(
        in_: GetEntityDataParams) -> Optional[EntityBoundResult]
```

x.get_entities_bound(in_) -> EntityBoundResult or None
Get Entities Bound

Args:
    in_ (GetEntityDataParams): 

Returns:
    EntityBoundResult or None: 

    out_result (EntityBoundResult):

<a id="unreal.WdpSceneAPI.get_all_entities_data"></a>

#### get\_all\_entities\_data

```python
def get_all_entities_data(
        in_: GetAllEntityParams) -> Optional[EntityDataByTypeResult]
```

x.get_all_entities_data(in_) -> EntityDataByTypeResult or None
Get All Entities Data

Args:
    in_ (GetAllEntityParams): 

Returns:
    EntityDataByTypeResult or None: 

    out_result (EntityDataByTypeResult):

<a id="unreal.WdpSceneAPI.get_all_entities"></a>

#### get\_all\_entities

```python
def get_all_entities(in_: GetAllEntityParams) -> Optional[AllEntitiesResult]
```

x.get_all_entities(in_) -> AllEntitiesResult or None
Get All Entities

Args:
    in_ (GetAllEntityParams): 

Returns:
    AllEntitiesResult or None: 

    out_result (AllEntitiesResult):

<a id="unreal.WdpSceneAPI.create_entities_with_param_template"></a>

#### create\_entities\_with\_param\_template

```python
def create_entities_with_param_template(
    create_entity_params: CreateEntityParamsWithTemplate
) -> Optional[IntEidArrayResult]
```

x.create_entities_with_param_template(create_entity_params) -> IntEidArrayResult or None
Create Entities with Param Template

Args:
    create_entity_params (CreateEntityParamsWithTemplate): 

Returns:
    IntEidArrayResult or None: 

    out_result (IntEidArrayResult):

<a id="unreal.WdpSceneAPI.create_entities"></a>

#### create\_entities

```python
def create_entities(
        create_entity_params: CreateEntityParams
) -> Optional[IntEidArrayResult]
```

x.create_entities(create_entity_params) -> IntEidArrayResult or None
APIs

Args:
    create_entity_params (CreateEntityParams): 

Returns:
    IntEidArrayResult or None: 

    out_result (IntEidArrayResult):

<a id="unreal.WdpSceneAPI.clear_scene"></a>

#### clear\_scene

```python
def clear_scene(in_: ClearSceneParams) -> Optional[ResultBase]
```

x.clear_scene(in_) -> ResultBase or None
Clear Scene

Args:
    in_ (ClearSceneParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI"></a>