## DataLayerSubsystem Objects

```python
class DataLayerSubsystem(WorldSubsystem)
```

This class is deprecated, it has been replaced by DataLayerManager.

**C++ Source:**

- **Module**: Engine
- **File**: DataLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_data_layer_runtime_state_changed`` (OnDataLayerRuntimeStateChanged):  [Read-Write]

<a id="unreal.DataLayerSubsystem.on_data_layer_runtime_state_changed"></a>

#### on_data_layer_runtime_state_changed

```python
@property
def on_data_layer_runtime_state_changed() -> OnDataLayerRuntimeStateChanged
```

(OnDataLayerRuntimeStateChanged):  [Read-Write]

<a id="unreal.DataLayerSubsystem.on_data_layer_runtime_state_changed"></a>

#### on_data_layer_runtime_state_changed

```python
@on_data_layer_runtime_state_changed.setter
def on_data_layer_runtime_state_changed(
        value: OnDataLayerRuntimeStateChanged) -> None
```

<a id="unreal.DataLayerSubsystem.on_data_layer_state_changed"></a>

#### on_data_layer_state_changed

```python
@property
def on_data_layer_state_changed() -> OnDataLayerRuntimeStateChanged
```

deprecated: 'on_data_layer_state_changed' was renamed to 'on_data_layer_runtime_state_changed'.

<a id="unreal.DataLayerSubsystem.on_data_layer_state_changed"></a>

#### on_data_layer_state_changed

```python
@on_data_layer_state_changed.setter
def on_data_layer_state_changed(value: OnDataLayerRuntimeStateChanged) -> None
```

<a id="unreal.DataLayerSubsystem.set_data_layer_state_by_label"></a>

#### set_data_layer_state_by_label

```python
def set_data_layer_state_by_label(data_layer_label: Name,
                                  state: DataLayerStateType) -> None
```

x.set_data_layer_state_by_label(data_layer_label, state) -> None
Set Data Layer State by Label
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer_label (Name): 
    state (DataLayerStateType):

<a id="unreal.DataLayerSubsystem.set_data_layer_state"></a>

#### set_data_layer_state

```python
def set_data_layer_state(data_layer: ActorDataLayer,
                         state: DataLayerStateType) -> None
```

x.set_data_layer_state(data_layer, state) -> None
Set Data Layer State
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer (ActorDataLayer): 
    state (DataLayerStateType):

<a id="unreal.DataLayerSubsystem.set_data_layer_runtime_state_by_label"></a>

#### set_data_layer_runtime_state_by_label

```python
def set_data_layer_runtime_state_by_label(data_layer_label: Name,
                                          state: DataLayerRuntimeState,
                                          is_recursive: bool = False) -> None
```

x.set_data_layer_runtime_state_by_label(data_layer_label, state, is_recursive=False) -> None
Set Data Layer Runtime State by Label

Args:
    data_layer_label (Name): 
    state (DataLayerRuntimeState): 
    is_recursive (bool):

<a id="unreal.DataLayerSubsystem.set_data_layer_runtime_state"></a>

#### set_data_layer_runtime_state

```python
def set_data_layer_runtime_state(data_layer: ActorDataLayer,
                                 state: DataLayerRuntimeState,
                                 is_recursive: bool = False) -> None
```

x.set_data_layer_runtime_state(data_layer, state, is_recursive=False) -> None
Set Data Layer Runtime State

Args:
    data_layer (ActorDataLayer): 
    state (DataLayerRuntimeState): 
    is_recursive (bool):

<a id="unreal.DataLayerSubsystem.set_data_layer_instance_runtime_state"></a>

#### set_data_layer_instance_runtime_state

```python
def set_data_layer_instance_runtime_state(data_layer_asset: DataLayerAsset,
                                          state: DataLayerRuntimeState,
                                          is_recursive: bool = False) -> None
```

x.set_data_layer_instance_runtime_state(data_layer_asset, state, is_recursive=False) -> None
Set Data Layer Instance Runtime State
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer_asset (DataLayerAsset): 
    state (DataLayerRuntimeState): 
    is_recursive (bool):

<a id="unreal.DataLayerSubsystem.get_loaded_data_layer_names"></a>

#### get_loaded_data_layer_names

```python
def get_loaded_data_layer_names() -> Set[Name]
```

x.get_loaded_data_layer_names() -> Set[Name]
Get Loaded Data Layer Names
deprecated: GetLoadedDataLayerNames will be removed.

Returns:
    Set[Name]:

<a id="unreal.DataLayerSubsystem.get_data_layer_state_by_label"></a>

#### get_data_layer_state_by_label

```python
def get_data_layer_state_by_label(
        data_layer_label: Name) -> DataLayerStateType
```

x.get_data_layer_state_by_label(data_layer_label) -> DataLayerStateType
Get Data Layer State by Label
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer_label (Name): 

Returns:
    DataLayerStateType:

<a id="unreal.DataLayerSubsystem.get_data_layer_state"></a>

#### get_data_layer_state

```python
def get_data_layer_state(data_layer: ActorDataLayer) -> DataLayerStateType
```

x.get_data_layer_state(data_layer) -> DataLayerStateType
Get Data Layer State
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer (ActorDataLayer): 

Returns:
    DataLayerStateType:

<a id="unreal.DataLayerSubsystem.get_data_layer_runtime_state_by_label"></a>

#### get_data_layer_runtime_state_by_label

```python
def get_data_layer_runtime_state_by_label(
        data_layer_label: Name) -> DataLayerRuntimeState
```

x.get_data_layer_runtime_state_by_label(data_layer_label) -> DataLayerRuntimeState
Get Data Layer Runtime State by Label
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceRuntimeState in DataLayerManager

Args:
    data_layer_label (Name): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerSubsystem.get_data_layer_runtime_state"></a>

#### get_data_layer_runtime_state

```python
def get_data_layer_runtime_state(
        data_layer: ActorDataLayer) -> DataLayerRuntimeState
```

x.get_data_layer_runtime_state(data_layer) -> DataLayerRuntimeState
Get Data Layer Runtime State
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceRuntimeState in DataLayerManager

Args:
    data_layer (ActorDataLayer): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerSubsystem.get_data_layer_instance_runtime_state"></a>

#### get_data_layer_instance_runtime_state

```python
def get_data_layer_instance_runtime_state(
        data_layer_asset: DataLayerAsset) -> DataLayerRuntimeState
```

x.get_data_layer_instance_runtime_state(data_layer_asset) -> DataLayerRuntimeState
Get Data Layer Instance Runtime State
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer_asset (DataLayerAsset): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerSubsystem.get_data_layer_instance_from_asset"></a>

#### get_data_layer_instance_from_asset

```python
def get_data_layer_instance_from_asset(
        data_layer_asset: DataLayerAsset) -> DataLayerInstance
```

x.get_data_layer_instance_from_asset(data_layer_asset) -> DataLayerInstance
Get Data Layer Instance from Asset
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer_asset (DataLayerAsset): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerSubsystem.get_data_layer_instance_effective_runtime_state"></a>

#### get_data_layer_instance_effective_runtime_state

```python
def get_data_layer_instance_effective_runtime_state(
        data_layer_asset: DataLayerAsset) -> DataLayerRuntimeState
```

x.get_data_layer_instance_effective_runtime_state(data_layer_asset) -> DataLayerRuntimeState
Get Data Layer Instance Effective Runtime State
deprecated: DataLayerSubsystem is deprecated, use the equivalent function in DataLayerManager

Args:
    data_layer_asset (DataLayerAsset): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerSubsystem.get_data_layer_from_name"></a>

#### get_data_layer_from_name

```python
def get_data_layer_from_name(data_layer_name: Name) -> DataLayerInstance
```

x.get_data_layer_from_name(data_layer_name) -> DataLayerInstance
Get Data Layer from Name
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceFromAsset in DataLayerManager

Args:
    data_layer_name (Name): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerSubsystem.get_data_layer_from_label"></a>

#### get_data_layer_from_label

```python
def get_data_layer_from_label(data_layer_label: Name) -> DataLayerInstance
```

x.get_data_layer_from_label(data_layer_label) -> DataLayerInstance
Get Data Layer from Label
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceFromAsset in DataLayerManager

Args:
    data_layer_label (Name): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerSubsystem.get_data_layer_effective_runtime_state_by_label"></a>

#### get_data_layer_effective_runtime_state_by_label

```python
def get_data_layer_effective_runtime_state_by_label(
        data_layer_label: Name) -> DataLayerRuntimeState
```

x.get_data_layer_effective_runtime_state_by_label(data_layer_label) -> DataLayerRuntimeState
Get Data Layer Effective Runtime State by Label
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceEffectiveRuntimeState in DataLayerManager

Args:
    data_layer_label (Name): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerSubsystem.get_data_layer_effective_runtime_state"></a>

#### get_data_layer_effective_runtime_state

```python
def get_data_layer_effective_runtime_state(
        data_layer: ActorDataLayer) -> DataLayerRuntimeState
```

x.get_data_layer_effective_runtime_state(data_layer) -> DataLayerRuntimeState
Get Data Layer Effective Runtime State
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceEffectiveRuntimeState in DataLayerManager

Args:
    data_layer (ActorDataLayer): 

Returns:
    DataLayerRuntimeState:

<a id="unreal.DataLayerSubsystem.get_data_layer"></a>

#### get_data_layer

```python
def get_data_layer(data_layer: ActorDataLayer) -> DataLayerInstance
```

x.get_data_layer(data_layer) -> DataLayerInstance
Get Data Layer
deprecated: DataLayerSubsystem is deprecated, use GetDataLayerInstanceFromAsset in DataLayerManager

Args:
    data_layer (ActorDataLayer): 

Returns:
    DataLayerInstance:

<a id="unreal.DataLayerSubsystem.get_active_data_layer_names"></a>

#### get_active_data_layer_names

```python
def get_active_data_layer_names() -> Set[Name]
```

x.get_active_data_layer_names() -> Set[Name]
Get Active Data Layer Names
deprecated: GetActiveDataLayerNames will be removed.

Returns:
    Set[Name]:

<a id="unreal.DeprecatedDataLayerInstance"></a>