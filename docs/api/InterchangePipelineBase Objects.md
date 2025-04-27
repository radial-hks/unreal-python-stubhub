## InterchangePipelineBase Objects

```python
class InterchangePipelineBase(Object)
```

Pipeline implementation:

1. ExecutePipeline - Create the factory nodes from the translated nodes. This is where the logic is execute to create the unreal asset via the factory node. Called after the translation
2. ExecutePostFactoryPipeline - Called after the factory has create the unreal asset with the associate factory node, but before calling PostEditChange.
3. ExecutePostImportPipeline - Called after the asset PostEditChange is done. If the asset use the async build framework, the asset build should be completed.
4. ExecutePostBroadcastPipeline - Called after the asset was registered to the registry manager and all broadcast calls have been done.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangePipelineBase.h

<a id="unreal.InterchangePipelineBase.scripted_set_reimport_source_index"></a>

#### scripted_set_reimport_source_index

```python
def scripted_set_reimport_source_index(reimport_object_class: Class,
                                       source_file_index: int) -> None
```

x.scripted_set_reimport_source_index(reimport_object_class, source_file_index) -> None
Non-virtual helper that allows Blueprint to implement an event-based function.
the Interchange framework calls this function, not the virtual one that is called by the default implementation.

Args:
    reimport_object_class (type(Class)): 
    source_file_index (int32):

<a id="unreal.InterchangePipelineBase.scripted_get_pipeline_display_name"></a>

#### scripted_get_pipeline_display_name

```python
def scripted_get_pipeline_display_name() -> str
```

x.scripted_get_pipeline_display_name() -> str
This function is call when we want to list pipeline in the import dialog. If not override the default behavior of this function will search if
the pipeline have a FString UPROPERTY named "PipelineDisplayName" and return the property value. If there is no FString UPROPERTY call "PipelineDisplayName" it will
return the name of the pipeline asset (UObject::GetName).

When creating a pipeline (c++, python or blueprint) you can simply add a UPROPERTY name "PipelineDisplayName" to your pipeline, you do not need to override the function.
Use the same category has your other options and put it on the top.
The meta tag StandAlonePipelineProperty will hide your PROPERTY if your pipeline is a sub object of another pipeline when showing the import dialog.
The meta tag PipelineInternalEditionData make sure the property will be show only when we edit the pipeline object (hidden when showing the import dialog).


UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Textures", meta = (StandAlonePipelineProperty = "True", PipelineInternalEditionData = "True"))
FString PipelineDisplayName;

Returns:
    str:

<a id="unreal.InterchangePipelineBase.scripted_execute_post_import_pipeline"></a>

#### scripted_execute_post_import_pipeline

```python
def scripted_execute_post_import_pipeline(
        base_node_container: InterchangeBaseNodeContainer,
        factory_node_key: str, created_asset: Object,
        is_a_reimport: bool) -> None
```

x.scripted_execute_post_import_pipeline(base_node_container, factory_node_key, created_asset, is_a_reimport) -> None
ScriptedExecutePostImportPipeline is called after an asset is completely imported, after PostEditChange has already been called.
This can be useful if you need build data for one asset to finish setting up another asset.
example: A PhysicsAsset needs skeletal mesh render data to be built properly.
note: the FTaskPostImport calls this function not the virtual one that is call by the default implementation.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    factory_node_key (str): 
    created_asset (Object): 
    is_a_reimport (bool):

<a id="unreal.InterchangePipelineBase.scripted_execute_post_factory_pipeline"></a>

#### scripted_execute_post_factory_pipeline

```python
def scripted_execute_post_factory_pipeline(
        base_node_container: InterchangeBaseNodeContainer,
        factory_node_key: str, created_asset: Object,
        is_a_reimport: bool) -> None
```

x.scripted_execute_post_factory_pipeline(base_node_container, factory_node_key, created_asset, is_a_reimport) -> None
ScriptedExecutePostFactoryPipeline is called after the factory creates an Unreal asset, but before it calls PostEditChange.
note: The FTaskPreCompletion task calls this function, not the virtual one that is called by the default implementation.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    factory_node_key (str): 
    created_asset (Object): 
    is_a_reimport (bool):

<a id="unreal.InterchangePipelineBase.scripted_execute_post_broadcast_pipeline"></a>

#### scripted_execute_post_broadcast_pipeline

```python
def scripted_execute_post_broadcast_pipeline(
        base_node_container: InterchangeBaseNodeContainer,
        factory_node_key: str, created_asset: Object,
        is_a_reimport: bool) -> None
```

x.scripted_execute_post_broadcast_pipeline(base_node_container, factory_node_key, created_asset, is_a_reimport) -> None
ScriptedExecutePostBroadcastPipeline is called after an asset is completely imported and the broadcast have been called.
This can be useful if you need to unload the asset for any reason (Level reference by level instance need to be unload).
note: the FTaskCompletion_GameThread calls this function not the virtual one that is call by the default implementation.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    factory_node_key (str): 
    created_asset (Object): 
    is_a_reimport (bool):

<a id="unreal.InterchangePipelineBase.scripted_execute_pipeline"></a>

#### scripted_execute_pipeline

```python
def scripted_execute_pipeline(
        base_node_container: InterchangeBaseNodeContainer,
        source_datas: Array[InterchangeSourceData],
        content_base_path: str) -> None
```

x.scripted_execute_pipeline(base_node_container, source_datas, content_base_path) -> None
ScriptedExecutePipeline, is call after the translation and before we parse the graph to call the factory.
This is where factory node should be created by the pipeline.
Each factory node represent an unreal asset create that will be create by an interchange factory.
note: the FTaskPipeline is calling this function not the virtual one that is call by the default implementation.

Args:
    base_node_container (InterchangeBaseNodeContainer): 
    source_datas (Array[InterchangeSourceData]): 
    content_base_path (str):

<a id="unreal.InterchangePipelineBase.scripted_execute_export_pipeline"></a>

#### scripted_execute_export_pipeline

```python
def scripted_execute_export_pipeline(
        base_node_container: InterchangeBaseNodeContainer) -> None
```

x.scripted_execute_export_pipeline(base_node_container) -> None
Non-virtual helper that allows Blueprint to implement an event-based function.
The Interchange manager calls this function, not the virtual one that is called by the default implementation.

Args:
    base_node_container (InterchangeBaseNodeContainer):

<a id="unreal.InterchangePipelineBase.find_or_add_property_states"></a>

#### find_or_add_property_states

```python
def find_or_add_property_states(
        property_path: Name) -> InterchangePipelinePropertyStates
```

x.find_or_add_property_states(property_path) -> InterchangePipelinePropertyStates
Return a mutable property states reference. Add the property states if it doesn't exist.

Args:
    property_path (Name): 

Returns:
    InterchangePipelinePropertyStates:

<a id="unreal.InterchangePipelineBase.does_property_states_exist"></a>

#### does_property_states_exist

```python
def does_property_states_exist(property_path: Name) -> bool
```

x.does_property_states_exist(property_path) -> bool
Return true if the property has valid states, or false if no states were set for the property.

Args:
    property_path (Name): 

Returns:
    bool:

<a id="unreal.InterchangeTranslatorSettings"></a>