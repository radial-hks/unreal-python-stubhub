## DataLayer Objects

```python
class DataLayer(Object)
```

Data Layer

**C++ Source:**

- **Module**: Engine
- **File**: DataLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_color`` (Color):  [Read-Write]
- ``initial_runtime_state`` (DataLayerRuntimeState):  [Read-Write]
- ``is_initially_loaded_in_editor`` (bool):  [Read-Write] Determines the default value of the data layer's loaded state in editor if it hasn't been changed in data layer outliner by the user
- ``is_initially_visible`` (bool):  [Read-Write] Whether actors associated with the Data Layer should be initially visible in the viewport when loading the map
- ``is_runtime`` (bool):  [Read-Write] Whether the Data Layer affects actor runtime loading

<a id="unreal.DataLayer.is_visible"></a>

#### is_visible

```python
def is_visible() -> bool
```

x.is_visible() -> bool
Is Visible

Returns:
    bool:

<a id="unreal.DataLayer.is_runtime"></a>

#### is_runtime

```python
def is_runtime() -> bool
```

x.is_runtime() -> bool
Is Runtime

Returns:
    bool:

<a id="unreal.DataLayer.is_initially_visible"></a>

#### is_initially_visible

```python
def is_initially_visible() -> bool
```

x.is_initially_visible() -> bool
Is Initially Visible

Returns:
    bool:

<a id="unreal.DataLayer.is_initially_active"></a>

#### is_initially_active

```python
def is_initially_active() -> bool
```

x.is_initially_active() -> bool
Is Initially Active
deprecated: Use GetInitialRuntimeState instead

Returns:
    bool:

<a id="unreal.DataLayer.is_effective_visible"></a>

#### is_effective_visible

```python
def is_effective_visible() -> bool
```

x.is_effective_visible() -> bool
Is Effective Visible

Returns:
    bool:

<a id="unreal.DataLayer.is_dynamically_loaded"></a>

#### is_dynamically_loaded

```python
def is_dynamically_loaded() -> bool
```

x.is_dynamically_loaded() -> bool
Is Dynamically Loaded
deprecated: Use IsRuntime instead

Returns:
    bool:

<a id="unreal.DataLayer.get_initial_state"></a>

#### get_initial_state

```python
def get_initial_state() -> DataLayerStateType
```

x.get_initial_state() -> DataLayerStateType
Get Initial State
deprecated: Use GetInitialRuntimeState instead

Returns:
    DataLayerStateType:

<a id="unreal.DataLayer.get_initial_runtime_state"></a>

#### get_initial_runtime_state

```python
def get_initial_runtime_state() -> DataLayerRuntimeState
```

x.get_initial_runtime_state() -> DataLayerRuntimeState
Get Initial Runtime State

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayer.get_debug_color"></a>

#### get_debug_color

```python
def get_debug_color() -> Color
```

x.get_debug_color() -> Color
Get Debug Color

Returns:
    Color:

<a id="unreal.DataLayer.get_data_layer_label"></a>

#### get_data_layer_label

```python
def get_data_layer_label() -> Name
```

x.get_data_layer_label() -> Name
Get Data Layer Label

Returns:
    Name:

<a id="unreal.DataLayer.equals"></a>

#### equals

```python
def equals(actor_data_layer: ActorDataLayer) -> bool
```

x.equals(actor_data_layer) -> bool
Equals

Args:
    actor_data_layer (ActorDataLayer): 

Returns:
    bool:

<a id="unreal.DataLayerInstancePrivate"></a>