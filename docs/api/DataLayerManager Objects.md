## DataLayerManager Objects

```python
class DataLayerManager(Object)
```

Data Layer Manager

**C++ Source:**

- **Module**: Engine
- **File**: DataLayerManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_data_layer_instance_runtime_state_changed`` (OnDataLayerInstanceRuntimeStateChanged):  [Read-Write] Called when a Data Layer instance runtime state has changed.

<a id="unreal.DataLayerManager.on_data_layer_instance_runtime_state_changed"></a>

#### on_data_layer_instance_runtime_state_changed

```python
@property
def on_data_layer_instance_runtime_state_changed(
) -> OnDataLayerInstanceRuntimeStateChanged
```

(OnDataLayerInstanceRuntimeStateChanged):  [Read-Write] Called when a Data Layer instance runtime state has changed.

<a id="unreal.DataLayerManager.on_data_layer_instance_runtime_state_changed"></a>

#### on_data_layer_instance_runtime_state_changed

```python
@on_data_layer_instance_runtime_state_changed.setter
def on_data_layer_instance_runtime_state_changed(
        value: OnDataLayerInstanceRuntimeStateChanged) -> None
```

<a id="unreal.DataLayerManager.set_data_layer_runtime_state"></a>

#### set_data_layer_runtime_state

```python
def set_data_layer_runtime_state(data_layer_asset: DataLayerAsset,
                                 state: DataLayerRuntimeState,
                                 is_recursive: bool = False) -> bool
```

x.set_data_layer_runtime_state(data_layer_asset, state, is_recursive=False) -> bool
Finds a matching Data Layer instance referencing the provided Data Layer asset and changes its runtime state (if any).
If recursive is set to true, the runtime state will also be applied to all child Data Layer instances.
Note:
- Changing the runtime state of a Client-Only Data Layer instance must be done on the client side or else it will have no effect.
- Changing the runtime state of a Server-Only Data Layer instance can only be done on the server side or else it will have no effect.
- Changing the runtime state of a runtime Data Layer instance (with no Load Filter set on the asset) must be done on the server side
  or else it will have no effect. The runtime state will then be replicated on the client.
(see Data Layer asset Load Filter for more details)

Args:
    data_layer_asset (DataLayerAsset): 
    state (DataLayerRuntimeState): 
    is_recursive (bool): 

Returns:
    bool:

<a id="unreal.DataLayerManager.set_data_layer_instance_runtime_state"></a>

#### set_data_layer_instance_runtime_state

```python
def set_data_layer_instance_runtime_state(
        data_layer_instance: DataLayerInstance,
        state: DataLayerRuntimeState,
        is_recursive: bool = False) -> bool
```

x.set_data_layer_instance_runtime_state(data_layer_instance, state, is_recursive=False) -> bool
Changes the Data Layer instance runtime state.
If recursive is set to true, the runtime state will also be applied to all child Data Layer instances.
Note:
- Changing the runtime state of a Client-Only Data Layer instance must be done on the client side or else it will have no effect.
- Changing the runtime state of a Server-Only Data Layer instance can only be done on the server side or else it will have no effect.
- Changing the runtime state of a runtime Data Layer instance (with no Load Filter set on the asset) must be done on the server side
  or else it will have no effect. The runtime state will then be replicated on the client.
(see Data Layer asset Load Filter for more details)

Args:
    data_layer_instance (DataLayerInstance): 
    state (DataLayerRuntimeState): 
    is_recursive (bool): 

Returns:
    bool:

<a id="unreal.DataLayerManager.get_data_layer_instances"></a>

#### get_data_layer_instances

```python
def get_data_layer_instances() -> Array[DataLayerInstance]
```

x.get_data_layer_instances() -> Array[DataLayerInstance]
Returns all Data Layer instances.

Returns:
    Array[DataLayerInstance]:

<a id="unreal.DataLayerManager.get_data_layer_instance_runtime_state"></a>

#### get_data_layer_instance_runtime_state

```python
def get_data_layer_instance_runtime_state(
        data_layer_instance: DataLayerInstance) -> DataLayerRuntimeState
```

x.get_data_layer_instance_runtime_state(data_layer_instance) -> DataLayerRuntimeState
Returns the Data Layer instance runtime state.

Args:
    data_layer_instance (DataLayerInstance): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerManager.get_data_layer_instance_from_name"></a>

#### get_data_layer_instance_from_name

```python
def get_data_layer_instance_from_name(
        data_layer_instance_name: Name) -> DataLayerInstance
```

x.get_data_layer_instance_from_name(data_layer_instance_name) -> DataLayerInstance
Returns the Data Layer instance matching the provided Data Layer instance name (if any).

Args:
    data_layer_instance_name (Name): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerManager.get_data_layer_instance_from_asset"></a>

#### get_data_layer_instance_from_asset

```python
def get_data_layer_instance_from_asset(
        data_layer_asset: DataLayerAsset) -> DataLayerInstance
```

x.get_data_layer_instance_from_asset(data_layer_asset) -> DataLayerInstance
Returns the Data Layer instance referencing the provided Data Layer asset (if any).

Args:
    data_layer_asset (DataLayerAsset): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerManager.get_data_layer_instance_effective_runtime_state"></a>

#### get_data_layer_instance_effective_runtime_state

```python
def get_data_layer_instance_effective_runtime_state(
        data_layer_instance: DataLayerInstance) -> DataLayerRuntimeState
```

x.get_data_layer_instance_effective_runtime_state(data_layer_instance) -> DataLayerRuntimeState
Finds a matching Data Layer instance referencing the provided Data Layer asset and returns the Data Layer Instance runtime state.

Args:
    data_layer_instance (DataLayerInstance): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DialogueSoundWaveProxy"></a>