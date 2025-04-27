## DMMaterialStageThroughput Objects

```python
class DMMaterialStageThroughput(DMMaterialStageSource)
```

A node which take one or more inputs and produces an output (e.g. Multiply)

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageThroughput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageThroughput.name"></a>

#### name

```python
@property
def name() -> Text
```

(Text):  [Read-Only]

<a id="unreal.DMMaterialStageThroughput.input_required"></a>

#### input_required

```python
@property
def input_required() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialStageThroughput.allow_nested_inputs"></a>

#### allow_nested_inputs

```python
@property
def allow_nested_inputs() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialStageThroughput.input_connectors"></a>

#### input_connectors

```python
@property
def input_connectors() -> Array[DMMaterialStageConnector]
```

(Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageThroughput.is_input_required"></a>

#### is_input_required

```python
def is_input_required() -> bool
```

x.is_input_required() -> bool
Returns true if input is required to successfully compile this node.

Returns:
    bool:

<a id="unreal.DMMaterialStageThroughput.get_input_connectors"></a>

#### get_input_connectors

```python
def get_input_connectors() -> Array[DMMaterialStageConnector]
```

x.get_input_connectors() -> Array[DMMaterialStageConnector]
Get Input Connectors

Returns:
    Array[DMMaterialStageConnector]:

<a id="unreal.DMMaterialStageThroughput.get_description"></a>

#### get_description

```python
def get_description() -> Text
```

x.get_description() -> Text
Get Description

Returns:
    Text:

<a id="unreal.DMMaterialStageThroughput.can_input_connect_to"></a>

#### can_input_connect_to

```python
def can_input_connect_to(throughput_input_index: int,
                         output_connector: DMMaterialStageConnector,
                         output_channel: int,
                         check_single_float: bool = False) -> bool
```

x.can_input_connect_to(throughput_input_index, output_connector, output_channel, check_single_float=False) -> bool
Whether the given output connector can connect to this node.

Args:
    throughput_input_index (int32): 
    output_connector (DMMaterialStageConnector): 
    output_channel (int32): 
    check_single_float (bool): If the initial compatibility check fails, it will again check against a single float.

Returns:
    bool:

<a id="unreal.DMMaterialStageThroughput.can_input_accept_type"></a>

#### can_input_accept_type

```python
def can_input_accept_type(throughput_input_index: int,
                          value_type: DMValueType) -> bool
```

x.can_input_accept_type(throughput_input_index, value_type) -> bool
Can Input Accept Type

Args:
    throughput_input_index (int32): 
    value_type (DMValueType): 

Returns:
    bool:

<a id="unreal.DMMaterialStageThroughput.allows_nested_inputs"></a>

#### allows_nested_inputs

```python
def allows_nested_inputs() -> bool
```

x.allows_nested_inputs() -> bool
Returns true if this node's inputs can have their own inputs.

Returns:
    bool:

<a id="unreal.DMMaterialStageBlend"></a>