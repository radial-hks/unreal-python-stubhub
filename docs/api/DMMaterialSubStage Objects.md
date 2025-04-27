## DMMaterialSubStage Objects

```python
class DMMaterialSubStage(DMMaterialStage)
```

A stage that is a subobject of another stage, such as when an input throughput has its own inputs.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialSubStage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_change_source`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]
- ``input_connection_map`` (Array[DMMaterialStageConnection]):  [Read-Only] How our inputs connect to the inputs of this stage's source
- ``inputs`` (Array[DMMaterialStageInput]):  [Read-Only]
- ``parent_stage`` (DMMaterialStage):  [Read-Only]
- ``source`` (DMMaterialStageSource):  [Read-Only]

<a id="unreal.DMMaterialSubStage.parent_stage"></a>

#### parent_stage

```python
@property
def parent_stage() -> DMMaterialStage
```

(DMMaterialStage):  [Read-Only]

<a id="unreal.DMMaterialSubStage.set_parent_component"></a>

#### set_parent_component

```python
def set_parent_component(parent_component: DMMaterialComponent) -> None
```

x.set_parent_component(parent_component) -> None
Sets which object directly owns this component in the hierarchy.

Args:
    parent_component (DMMaterialComponent):

<a id="unreal.DMMaterialSubStage.get_parent_stage"></a>

#### get_parent_stage

```python
def get_parent_stage() -> DMMaterialStage
```

x.get_parent_stage() -> DMMaterialStage
Returns the parent stage of this stage, which is probably not its direct parent.

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialSubStage.get_parent_most_stage"></a>

#### get_parent_most_stage

```python
def get_parent_most_stage() -> DMMaterialStage
```

x.get_parent_most_stage() -> DMMaterialStage
Recursively calls GetParentStage() to find the outer stage.

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialSubStage.create_material_sub_stage"></a>

#### create_material_sub_stage

```python
@classmethod
def create_material_sub_stage(
        cls, parent_stage: DMMaterialStage) -> DMMaterialSubStage
```

X.create_material_sub_stage(parent_stage) -> DMMaterialSubStage
Create Material Sub Stage

Args:
    parent_stage (DMMaterialStage): 

Returns:
    DMMaterialSubStage:

<a id="unreal.DMMaterialPropertyAmbientOcclusion"></a>