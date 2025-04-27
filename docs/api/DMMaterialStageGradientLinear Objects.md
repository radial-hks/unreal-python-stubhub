## DMMaterialStageGradientLinear Objects

```python
class DMMaterialStageGradientLinear(DMMaterialStageGradient)
```

DMMaterial Stage Gradient Linear

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSGLinear.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``material_function`` (MaterialFunctionInterface):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``tiling`` (LinearGradientTileType):  [Read-Write]

<a id="unreal.DMMaterialStageGradientLinear.tiling"></a>

#### tiling

```python
@property
def tiling() -> LinearGradientTileType
```

(LinearGradientTileType):  [Read-Write]

<a id="unreal.DMMaterialStageGradientLinear.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: LinearGradientTileType) -> None
```

<a id="unreal.DMMaterialStageGradientLinear.set_tiling_type"></a>

#### set_tiling_type

```python
def set_tiling_type(type: LinearGradientTileType) -> None
```

x.set_tiling_type(type) -> None
Set Tiling Type

Args:
    type (LinearGradientTileType):

<a id="unreal.DMMaterialStageGradientLinear.get_tiling_type"></a>

#### get_tiling_type

```python
def get_tiling_type() -> LinearGradientTileType
```

x.get_tiling_type() -> LinearGradientTileType
Get Tiling Type

Returns:
    LinearGradientTileType:

<a id="unreal.DMMaterialStageGradientRadial"></a>