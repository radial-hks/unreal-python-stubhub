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

#### is\_visible

```python
def is_visible() -> bool
```

x.is_visible() -> bool
Is Visible

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_server_only"></a>

#### is\_server\_only

```python
def is_server_only() -> bool
```

x.is_server_only() -> bool
Is Server Only

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_runtime"></a>

#### is\_runtime

```python
def is_runtime() -> bool
```

x.is_runtime() -> bool
Is Runtime

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_initially_visible"></a>

#### is\_initially\_visible

```python
def is_initially_visible() -> bool
```

x.is_initially_visible() -> bool
Is Initially Visible

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_effective_visible"></a>

#### is\_effective\_visible

```python
def is_effective_visible() -> bool
```

x.is_effective_visible() -> bool
Is Effective Visible

Returns:
    bool:

<a id="unreal.DataLayerInstance.is_client_only"></a>

#### is\_client\_only

```python
def is_client_only() -> bool
```

x.is_client_only() -> bool
Is Client Only

Returns:
    bool:

<a id="unreal.DataLayerInstance.get_type"></a>

#### get\_type

```python
def get_type() -> DataLayerType
```

x.get_type() -> DataLayerType
Get Type

Returns:
    DataLayerType:

<a id="unreal.DataLayerInstance.get_initial_runtime_state"></a>

#### get\_initial\_runtime\_state

```python
def get_initial_runtime_state() -> DataLayerRuntimeState
```

x.get_initial_runtime_state() -> DataLayerRuntimeState
Get Initial Runtime State

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerInstance.get_debug_color"></a>

#### get\_debug\_color

```python
def get_debug_color() -> Color
```

x.get_debug_color() -> Color
Get Debug Color

Returns:
    Color:

<a id="unreal.DataLayerInstance.get_data_layer_short_name"></a>

#### get\_data\_layer\_short\_name

```python
def get_data_layer_short_name() -> str
```

x.get_data_layer_short_name() -> str
Get Data Layer Short Name

Returns:
    str:

<a id="unreal.DataLayerInstance.get_data_layer_full_name"></a>

#### get\_data\_layer\_full\_name

```python
def get_data_layer_full_name() -> str
```

x.get_data_layer_full_name() -> str
Get Data Layer Full Name

Returns:
    str:

<a id="unreal.DataLayerInstance.get_asset"></a>

#### get\_asset

```python
def get_asset() -> DataLayerAsset
```

x.get_asset() -> DataLayerAsset
Get Asset

Returns:
    DataLayerAsset:

<a id="unreal.DataLayerInstanceWithAsset"></a>