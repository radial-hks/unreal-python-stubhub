## DMMaterialStageConnection Objects

```python
class DMMaterialStageConnection(StructBase)
```

Represents the channels(channel = float, texture, etc.) that connect to an input.

Multiple float channels can be combined to create a single put (e.g. R, G, B -> RGB)

Individual source channels, from potentially multiple sources, can be directed to specific
input channels (e.g. T1.R, T2.B, T3.G -> {T2.B, T1.R, T3.G, T2.B})

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMEDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channels`` (Array[DMMaterialStageConnectorChannel]):  [Read-Only] This struct represents the connections made to a single input connector.
  Can connect single outputs or combine them. Append nodes will be used to combine channels.
  Combining channels should only be used for float types!

<a id="unreal.DMMaterialStageConnection.__init__"></a>

#### __init__

```python
def __init__(channels: Array[DMMaterialStageConnectorChannel] = []) -> None
```

<a id="unreal.DMMaterialStageConnection.channels"></a>

#### channels

```python
@property
def channels() -> Array[DMMaterialStageConnectorChannel]
```

(Array[DMMaterialStageConnectorChannel]):  [Read-Only] This struct represents the connections made to a single input connector.
Can connect single outputs or combine them. Append nodes will be used to combine channels.
Combining channels should only be used for float types!

<a id="unreal.DMMaterialSlotOutputConnectorTypes"></a>