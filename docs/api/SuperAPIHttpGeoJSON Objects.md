## SuperAPIHttpGeoJSON Objects

```python
class SuperAPIHttpGeoJSON(ActorComponent)
```

Super APIHttp Geo JSON

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: SuperAPI_Raster
- **File**: SuperAPIHttpGeoJSON.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_geo_json_file_fail_down`` (GeoJSONReceivedDelegate):  [Read-Write]
- ``on_geo_json_file_finish_down`` (GeoJSONReceivedDelegate):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.SuperAPIHttpGeoJSON.on_geo_json_file_finish_down"></a>

#### on\_geo\_json\_file\_finish\_down

```python
@property
def on_geo_json_file_finish_down() -> GeoJSONReceivedDelegate
```

(GeoJSONReceivedDelegate):  [Read-Write]

<a id="unreal.SuperAPIHttpGeoJSON.on_geo_json_file_finish_down"></a>

#### on\_geo\_json\_file\_finish\_down

```python
@on_geo_json_file_finish_down.setter
def on_geo_json_file_finish_down(value: GeoJSONReceivedDelegate) -> None
```

<a id="unreal.SuperAPIHttpGeoJSON.on_geo_json_file_fail_down"></a>

#### on\_geo\_json\_file\_fail\_down

```python
@property
def on_geo_json_file_fail_down() -> GeoJSONReceivedDelegate
```

(GeoJSONReceivedDelegate):  [Read-Write]

<a id="unreal.SuperAPIHttpGeoJSON.on_geo_json_file_fail_down"></a>

#### on\_geo\_json\_file\_fail\_down

```python
@on_geo_json_file_fail_down.setter
def on_geo_json_file_fail_down(value: GeoJSONReceivedDelegate) -> None
```

<a id="unreal.SuperAPIHttpGeoJSON.get_geo_json_file_by_http"></a>

#### get\_geo\_json\_file\_by\_http

```python
def get_geo_json_file_by_http(url: str) -> Tuple[str, bool]
```

x.get_geo_json_file_by_http(url) -> (geo_json_file=str, is_success=bool)
Get Geo JSONFile by Http

Args:
    url (str): 

Returns:
    tuple: 

    geo_json_file (str): 

    is_success (bool):

<a id="unreal.SuperAPIHttpShp"></a>