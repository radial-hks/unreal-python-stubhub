## InterchangePipelineConfigurationBase Objects

```python
class InterchangePipelineConfigurationBase(Object)
```

Interchange Pipeline Configuration Base

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangePipelineConfigurationBase.h

<a id="unreal.InterchangePipelineConfigurationBase.scripted_show_scene_pipeline_configuration_dialog"></a>

#### scripted_show_scene_pipeline_configuration_dialog

```python
def scripted_show_scene_pipeline_configuration_dialog(
    source_data: InterchangeSourceData, translator: InterchangeTranslatorBase,
    base_node_container: InterchangeBaseNodeContainer
) -> Tuple[InterchangePipelineConfigurationDialogResult,
           Array[InterchangeStackInfo], Array[InterchangePipelineBase]]
```

x.scripted_show_scene_pipeline_configuration_dialog(source_data, translator, base_node_container) -> (InterchangePipelineConfigurationDialogResult, pipeline_stacks=Array[InterchangeStackInfo], out_pipelines=Array[InterchangePipelineBase])
Non-virtual helper that allows Blueprint to implement an event-based function to implement ShowScenePipelineConfigurationDialog().

Args:
    source_data (InterchangeSourceData): 
    translator (InterchangeTranslatorBase): 
    base_node_container (InterchangeBaseNodeContainer): 

Returns:
    tuple: 

    pipeline_stacks (Array[InterchangeStackInfo]): 

    out_pipelines (Array[InterchangePipelineBase]):

<a id="unreal.InterchangePipelineConfigurationBase.scripted_show_reimport_pipeline_configuration_dialog"></a>

#### scripted_show_reimport_pipeline_configuration_dialog

```python
def scripted_show_reimport_pipeline_configuration_dialog(
    source_data: InterchangeSourceData, translator: InterchangeTranslatorBase,
    base_node_container: InterchangeBaseNodeContainer, reimport_asset: Object
) -> Tuple[InterchangePipelineConfigurationDialogResult,
           Array[InterchangeStackInfo], Array[InterchangePipelineBase]]
```

x.scripted_show_reimport_pipeline_configuration_dialog(source_data, translator, base_node_container, reimport_asset) -> (InterchangePipelineConfigurationDialogResult, pipeline_stacks=Array[InterchangeStackInfo], out_pipelines=Array[InterchangePipelineBase])
Non-virtual helper that allows Blueprint to implement an event-based function to implement ShowReimportPipelineConfigurationDialog().

Args:
    source_data (InterchangeSourceData): 
    translator (InterchangeTranslatorBase): 
    base_node_container (InterchangeBaseNodeContainer): 
    reimport_asset (Object): 

Returns:
    tuple: 

    pipeline_stacks (Array[InterchangeStackInfo]): 

    out_pipelines (Array[InterchangePipelineBase]):

<a id="unreal.InterchangePipelineConfigurationBase.scripted_show_pipeline_configuration_dialog"></a>

#### scripted_show_pipeline_configuration_dialog

```python
def scripted_show_pipeline_configuration_dialog(
    source_data: InterchangeSourceData, translator: InterchangeTranslatorBase,
    base_node_container: InterchangeBaseNodeContainer
) -> Tuple[InterchangePipelineConfigurationDialogResult,
           Array[InterchangeStackInfo], Array[InterchangePipelineBase]]
```

x.scripted_show_pipeline_configuration_dialog(source_data, translator, base_node_container) -> (InterchangePipelineConfigurationDialogResult, pipeline_stacks=Array[InterchangeStackInfo], out_pipelines=Array[InterchangePipelineBase])
Non-virtual helper that allows Blueprint to implement an event-based function to implement ShowPipelineConfigurationDialog().

Args:
    source_data (InterchangeSourceData): 
    translator (InterchangeTranslatorBase): 
    base_node_container (InterchangeBaseNodeContainer): 

Returns:
    tuple: 

    pipeline_stacks (Array[InterchangeStackInfo]): 

    out_pipelines (Array[InterchangePipelineBase]):

<a id="unreal.InterchangeEditorSettings"></a>