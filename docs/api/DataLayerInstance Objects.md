## DataLayerInstance Objects

```python
class DataLayerInstance(Object)
```

Data Layer Instance

**C++ Source:**

- **Module**: Engine
- **File**: DataLayerInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial_runtime_state`` (DataLayerRuntimeState):  [Read-Write] Initial runtime state of this data layer instance. Only supported if it's runtime and not client/server only.
- ``is_initially_loaded_in_editor`` (bool):  [Read-Write] Determines the default value of the data layer's loaded state in editor if it hasn't been changed in data layer outliner by the user
- ``is_initially_visible`` (bool):  [Read-Write] Whether actors associated with the Data Layer should be initially visible in the viewport when loading the map
- ``override_block_on_slow_streaming`` (OverrideBlockOnSlowStreaming):  [Read-Write]

<a id="unreal.DataLayerInstance.is_visible"></a>

#### is_visible

```python
def is_visible() -> bool
```

x.is_visible() -> bool
Is Visible

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_server_only"></a>

#### is_server_only

```python
def is_server_only() -> bool
```

x.is_server_only() -> bool
Is Server Only

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_runtime"></a>

#### is_runtime

```python
def is_runtime() -> bool
```

x.is_runtime() -> bool
Is Runtime

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_initially_visible"></a>

#### is_initially_visible

```python
def is_initially_visible() -> bool
```

x.is_initially_visible() -> bool
Is Initially Visible

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_effective_visible"></a>

#### is_effective_visible

```python
def is_effective_visible() -> bool
```

x.is_effective_visible() -> bool
Is Effective Visible

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_client_only"></a>

#### is_client_only

```python
def is_client_only() -> bool
```

x.is_client_only() -> bool
Is Client Only

Returns:
    bool:

<a id="unreal.DataLayerInstance.get_type"></a>

#### get_type

```python
def get_type() -> DataLayerType
```

x.get_type() -> DataLayerType
Get Type

Returns:
    DataLayerType:

<a id="unreal.DataLayerInstance.get_initial_runtime_state"></a>

#### get_initial_runtime_state

```python
def get_initial_runtime_state() -> DataLayerRuntimeState
```

x.get_initial_runtime_state() -> DataLayerRuntimeState
Get Initial Runtime State

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerInstance.get_debug_color"></a>

#### get_debug_color

```python
def get_debug_color() -> Color
```

x.get_debug_color() -> Color
Get Debug Color

Returns:
    Color:

<a id="unreal.DataLayerInstance.get_data_layer_short_name"></a>

#### get_data_layer_short_name

```python
def get_data_layer_short_name() -> str
```

x.get_data_layer_short_name() -> str
Get Data Layer Short Name

Returns:
    str:

<a id="unreal.DataLayerInstance.get_data_layer_full_name"></a>

#### get_data_layer_full_name

```python
def get_data_layer_full_name() -> str
```

x.get_data_layer_full_name() -> str
Get Data Layer Full Name

Returns:
    str:

<a id="unreal.DataLayerInstance.get_asset"></a>

#### get_asset

```python
def get_asset() -> DataLayerAsset
```

x.get_asset() -> DataLayerAsset
Get Asset

Returns:
    DataLayerAsset:

<a id="unreal.DataLayerInstanceWithAsset"></a>