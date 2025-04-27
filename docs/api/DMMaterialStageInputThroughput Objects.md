## DMMaterialStageInputThroughput Objects

```python
class DMMaterialStageInputThroughput(DMMaterialStageInput)
```

DMMaterial Stage Input Throughput

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSIThroughput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``sub_stage`` (DMMaterialSubStage):  [Read-Only]

<a id="unreal.DMMaterialStageInputThroughput.sub_stage"></a>

#### sub_stage

```python
@property
def sub_stage() -> DMMaterialSubStage
```

(DMMaterialSubStage):  [Read-Only]

<a id="unreal.DMMaterialStageInputThroughput.get_sub_stage"></a>

#### get_sub_stage

```python
def get_sub_stage() -> DMMaterialSubStage
```

x.get_sub_stage() -> DMMaterialSubStage
Get Sub Stage

Returns:
    DMMaterialSubStage:

<a id="unreal.DMMaterialStageInputThroughput.get_material_stage_throughput_class"></a>

#### get_material_stage_throughput_class

```python
def get_material_stage_throughput_class() -> Class
```

x.get_material_stage_throughput_class() -> type(Class)
Get Material Stage Throughput Class

Returns:
    type(Class):

<a id="unreal.DMMaterialStageInputThroughput.get_material_stage_throughput"></a>

#### get_material_stage_throughput

```python
def get_material_stage_throughput() -> DMMaterialStageThroughput
```

x.get_material_stage_throughput() -> DMMaterialStageThroughput
Get Material Stage Throughput

Returns:
    DMMaterialStageThroughput:

<a id="unreal.DMMaterialStageInputExpression"></a>