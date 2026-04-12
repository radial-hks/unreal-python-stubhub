## UrbanBuildSimpleImportTool Objects

```python
class UrbanBuildSimpleImportTool(BlueprintFunctionLibrary)
```

Urban Build Simple Import Tool

**C++ Source:**

- **Plugin**: AesBuilder
- **Module**: UrbanEntityBuilder
- **File**: UrbanBuildGeoSimpleTextRead.h

<a id="unreal.UrbanBuildSimpleImportTool.urban_bp_modeler_build_derived_data"></a>

#### urban\_bp\_modeler\_build\_derived\_data

```python
@classmethod
def urban_bp_modeler_build_derived_data(cls,
                                        entities: Array[UrbanEntity],
                                        build_system: UrbanBuildSystem,
                                        asset_name: str,
                                        tile_position: Vector2D = [
                                            0.000000, 0.000000
                                        ],
                                        identity_name: str = "",
                                        event_receiver: Object = None,
                                        save_asset: bool = True,
                                        debug_mode: bool = False,
                                        block_build: bool = False) -> None
```

X.urban_bp_modeler_build_derived_data(entities, build_system, asset_name, tile_position=[0.000000, 0.000000], identity_name="", event_receiver=None, save_asset=True, debug_mode=False, block_build=False) -> None
Urban BPModeler Build Derived Data

Args:
    entities (Array[UrbanEntity]): 
    build_system (UrbanBuildSystem): 
    asset_name (str): 
    tile_position (Vector2D): 
    identity_name (str): 
    event_receiver (Object): 
    save_asset (bool): 
    debug_mode (bool): 
    block_build (bool):

<a id="unreal.UrbanBuildSimpleImportTool.urban_bp_modeler_build"></a>

#### urban\_bp\_modeler\_build

```python
@classmethod
def urban_bp_modeler_build(cls,
                           entities: Array[UrbanEntity],
                           build_system: UrbanBuildSystem,
                           asset_name: str,
                           tile_position: Vector2D = [0.000000, 0.000000],
                           identity_name: str = "",
                           event_receiver: Object = None,
                           save_asset: bool = True,
                           debug_mode: bool = False,
                           block_build: bool = False) -> None
```

X.urban_bp_modeler_build(entities, build_system, asset_name, tile_position=[0.000000, 0.000000], identity_name="", event_receiver=None, save_asset=True, debug_mode=False, block_build=False) -> None
Urban BPModeler Build

Args:
    entities (Array[UrbanEntity]): 
    build_system (UrbanBuildSystem): 
    asset_name (str): 
    tile_position (Vector2D): 
    identity_name (str): 
    event_receiver (Object): 
    save_asset (bool): 
    debug_mode (bool): 
    block_build (bool):

<a id="unreal.UrbanBuildSimpleImportTool.urban_bp_build"></a>

#### urban\_bp\_build

```python
@classmethod
def urban_bp_build(cls,
                   build_system: UrbanBuildSystem,
                   assetname: str,
                   data_name: str,
                   tile_position: Vector2D = [0.000000, 0.000000],
                   identity_name: str = "",
                   event_receiver: Object = None,
                   save_asset: bool = True,
                   debug_mode: bool = False,
                   block_build: bool = False) -> None
```

X.urban_bp_build(build_system, assetname, data_name, tile_position=[0.000000, 0.000000], identity_name="", event_receiver=None, save_asset=True, debug_mode=False, block_build=False) -> None
Urban BPBuild

Args:
    build_system (UrbanBuildSystem): 
    assetname (str): 
    data_name (str): 
    tile_position (Vector2D): 
    identity_name (str): 
    event_receiver (Object): 
    save_asset (bool): 
    debug_mode (bool): 
    block_build (bool):

<a id="unreal.UrbanBuildSimpleImportTool.unregist_build_finished_event"></a>

#### unregist\_build\_finished\_event

```python
@classmethod
def unregist_build_finished_event(cls) -> None
```

X.unregist_build_finished_event() -> None
Unregist Build Finished Event

<a id="unreal.UrbanBuildSimpleImportTool.spawn_actor_no_outliner"></a>

#### spawn\_actor\_no\_outliner

```python
@classmethod
def spawn_actor_no_outliner(
        cls, world_context_object: Object, class_: Class, transform: Transform,
        collision: SpawnActorCollisionHandlingMethod) -> Actor
```

X.spawn_actor_no_outliner(world_context_object, class_, transform, collision) -> Actor
Spawn Actor No Outliner

Args:
    world_context_object (Object): 
    class_ (type(Class)): 
    transform (Transform): 
    collision (SpawnActorCollisionHandlingMethod): 

Returns:
    Actor:

<a id="unreal.UrbanBuildSimpleImportTool.simple_transform_map2_change_set"></a>

#### simple\_transform\_map2\_change\_set

```python
@classmethod
def simple_transform_map2_change_set(cls,
                                     map_data: Array[UrbanChangeSetOutType],
                                     geo_srs: str, map_position: Vector2D,
                                     entity_asset_name: str,
                                     property_name: str, key_tag: str,
                                     fake_resouce_path: str) -> None
```

X.simple_transform_map2_change_set(map_data, geo_srs, map_position, entity_asset_name, property_name, key_tag, fake_resouce_path) -> None
Simple Transform Map 2Change Set

Args:
    map_data (Array[UrbanChangeSetOutType]): 
    geo_srs (str): 
    map_position (Vector2D): 
    entity_asset_name (str): 
    property_name (str): 
    key_tag (str): 
    fake_resouce_path (str):

<a id="unreal.UrbanBuildSimpleImportTool.simple_text2_change_set"></a>

#### simple\_text2\_change\_set

```python
@classmethod
def simple_text2_change_set(cls, text_file_path: str, entity_name: str,
                            fake_resouce_path: str) -> Vector2D
```

X.simple_text2_change_set(text_file_path, entity_name, fake_resouce_path) -> Vector2D
Simple Text 2Change Set

Args:
    text_file_path (str): 
    entity_name (str): 
    fake_resouce_path (str): 

Returns:
    Vector2D: 

    out_center (Vector2D):

<a id="unreal.UrbanBuildSimpleImportTool.simple_remove_changeset"></a>

#### simple\_remove\_changeset

```python
@classmethod
def simple_remove_changeset(cls,
                            path: str,
                            dependen_file: str,
                            part_of_file_name: str = "Delete") -> None
```

X.simple_remove_changeset(path, dependen_file, part_of_file_name="Delete") -> None
Simple Remove Changeset

Args:
    path (str): 
    dependen_file (str): 
    part_of_file_name (str):

<a id="unreal.UrbanBuildSimpleImportTool.simple_json2_change_set"></a>

#### simple\_json2\_change\_set

```python
@classmethod
def simple_json2_change_set(cls, json_file_path: str, entity_name: str,
                            fake_resouce_path: str) -> Vector2D
```

X.simple_json2_change_set(json_file_path, entity_name, fake_resouce_path) -> Vector2D
Simple Json 2Change Set

Args:
    json_file_path (str): 
    entity_name (str): 
    fake_resouce_path (str): 

Returns:
    Vector2D: 

    out_center (Vector2D):

<a id="unreal.UrbanBuildSimpleImportTool.simple_get_local_postion_from_geo_str"></a>

#### simple\_get\_local\_postion\_from\_geo\_str

```python
@classmethod
def simple_get_local_postion_from_geo_str(
        cls, geo_srs: str, map_position: Vector2D,
        geo_pos_str: Array[str]) -> Array[Vector]
```

X.simple_get_local_postion_from_geo_str(geo_srs, map_position, geo_pos_str) -> Array[Vector]
Simple Get Local Postion from Geo Str

Args:
    geo_srs (str): 
    map_position (Vector2D): 
    geo_pos_str (Array[str]): 

Returns:
    Array[Vector]:

<a id="unreal.UrbanBuildSimpleImportTool.simple_get_local_postion_from_geo"></a>

#### simple\_get\_local\_postion\_from\_geo

```python
@classmethod
def simple_get_local_postion_from_geo(
        cls, geo_srs: str, map_position: Vector2D,
        geo_pos: Array[Vector2D]) -> Array[Vector]
```

X.simple_get_local_postion_from_geo(geo_srs, map_position, geo_pos) -> Array[Vector]
Simple Get Local Postion from Geo

Args:
    geo_srs (str): 
    map_position (Vector2D): 
    geo_pos (Array[Vector2D]): 

Returns:
    Array[Vector]:

<a id="unreal.UrbanBuildSimpleImportTool.simple_foliage2_change_set"></a>

#### simple\_foliage2\_change\_set

```python
@classmethod
def simple_foliage2_change_set(cls, actor: Actor, geo_srs: str,
                               map_position: Vector2D, entity_asset_name: str,
                               property_name: str, path_tag: str,
                               fake_resouce_path: str) -> None
```

X.simple_foliage2_change_set(actor, geo_srs, map_position, entity_asset_name, property_name, path_tag, fake_resouce_path) -> None
Simple Foliage 2Change Set

Args:
    actor (Actor): 
    geo_srs (str): 
    map_position (Vector2D): 
    entity_asset_name (str): 
    property_name (str): 
    path_tag (str): 
    fake_resouce_path (str):

<a id="unreal.UrbanBuildSimpleImportTool.simple_change_way_tag_to_relation_by_path"></a>

#### simple\_change\_way\_tag\_to\_relation\_by\_path

```python
@classmethod
def simple_change_way_tag_to_relation_by_path(cls, path: str,
                                              move_tag_name: str) -> None
```

X.simple_change_way_tag_to_relation_by_path(path, move_tag_name) -> None
Simple Change Way Tag to Relation by Path

Args:
    path (str): 
    move_tag_name (str):

<a id="unreal.UrbanBuildSimpleImportTool.simple_change_way_tag_to_relation"></a>

#### simple\_change\_way\_tag\_to\_relation

```python
@classmethod
def simple_change_way_tag_to_relation(cls, file_name: str,
                                      target_file_name: str,
                                      move_tag_name: str) -> None
```

X.simple_change_way_tag_to_relation(file_name, target_file_name, move_tag_name) -> None
Simple Change Way Tag to Relation

Args:
    file_name (str): 
    target_file_name (str): 
    move_tag_name (str):

<a id="unreal.UrbanBuildSimpleImportTool.regist_build_finished_event"></a>

#### regist\_build\_finished\_event

```python
@classmethod
def regist_build_finished_event(
        cls, on_build_finished: OnBuildFinishedDelegate) -> None
```

X.regist_build_finished_event(on_build_finished) -> None
Regist Build Finished Event

Args:
    on_build_finished (OnBuildFinishedDelegate):

<a id="unreal.UrbanBuildSimpleImportTool.joy_file_io_get_files"></a>

#### joy\_file\_io\_get\_files

```python
@classmethod
def joy_file_io_get_files(cls, root_folder_full_path: str,
                          ext: str) -> Optional[Array[str]]
```

X.joy_file_io_get_files(root_folder_full_path, ext) -> Array[str] or None
Joy File IO Get Files

Args:
    root_folder_full_path (str): 
    ext (str): 

Returns:
    Array[str] or None: 

    files (Array[str]):

<a id="unreal.UrbanBuildSimpleImportTool.export_landmark_to_shp"></a>

#### export\_landmark\_to\_shp

```python
@classmethod
def export_landmark_to_shp(cls, entities: Array[UrbanEntity],
                           build_config: str, save_path: str,
                           file_name: str) -> Array[UrbanEntity]
```

X.export_landmark_to_shp(entities, build_config, save_path, file_name) -> Array[UrbanEntity]
Export Landmark to Shp

Args:
    entities (Array[UrbanEntity]): 
    build_config (str): 
    save_path (str): 
    file_name (str): 

Returns:
    Array[UrbanEntity]: 

    entities (Array[UrbanEntity]):

<a id="unreal.UrbanBuildSimpleImportTool.destroy_components_by_class_array"></a>

#### destroy\_components\_by\_class\_array

```python
@classmethod
def destroy_components_by_class_array(
        cls, actor: Actor, component_class_array: Array[Class]) -> None
```

X.destroy_components_by_class_array(actor, component_class_array) -> None
Destroy Components by Class Array

Args:
    actor (Actor): 
    component_class_array (Array[type(Class)]):

<a id="unreal.UrbanBuildSimpleImportTool.destroy_components_by_class"></a>

#### destroy\_components\_by\_class

```python
@classmethod
def destroy_components_by_class(cls, actor: Actor,
                                component_class: Class) -> None
```

X.destroy_components_by_class(actor, component_class) -> None
Destroy Components by Class

Args:
    actor (Actor): 
    component_class (type(Class)):

<a id="unreal.UrbanBuildSimpleImportTool.delete_resource_data"></a>

#### delete\_resource\_data

```python
@classmethod
def delete_resource_data(cls, data_asset: UrbanBuildDataAsset,
                         name: Name) -> bool
```

X.delete_resource_data(data_asset, name) -> bool
Delete Resource Data

Args:
    data_asset (UrbanBuildDataAsset): 
    name (Name): 

Returns:
    bool:

<a id="unreal.UrbanBuildSimpleImportTool.create_enum_from_data_table"></a>

#### create\_enum\_from\_data\_table

```python
@classmethod
def create_enum_from_data_table(cls, data_table: DataTable) -> UserDefinedEnum
```

X.create_enum_from_data_table(data_table) -> UserDefinedEnum
Create Enum from Data Table

Args:
    data_table (DataTable): 

Returns:
    UserDefinedEnum: 

    out_enum (UserDefinedEnum):

<a id="unreal.UrbanBuildSimpleImportTool.convert_int64_to_int32"></a>

#### convert\_int64\_to\_int32

```python
@classmethod
def convert_int64_to_int32(cls, int64: str) -> str
```

X.convert_int64_to_int32(int64) -> str
Convert Int 64To Int 32

Args:
    int64 (str): 

Returns:
    str:

<a id="unreal.UrbanBuildSimpleImportTool.add_or_set_resource_data"></a>

#### add\_or\_set\_resource\_data

```python
@classmethod
def add_or_set_resource_data(
        cls, data_asset: UrbanBuildDataAsset, name: Name,
        data: UrbanResourceStruct) -> Optional[UrbanResourceStruct]
```

X.add_or_set_resource_data(data_asset, name, data) -> UrbanResourceStruct or None
Add or Set Resource Data

Args:
    data_asset (UrbanBuildDataAsset): 
    name (Name): 
    data (UrbanResourceStruct): 

Returns:
    UrbanResourceStruct or None: 

    data (UrbanResourceStruct):

<a id="unreal.UrbanDownSampleBP"></a>