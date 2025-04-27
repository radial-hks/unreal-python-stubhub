## MVVMView Objects

```python
class MVVMView(UserWidgetExtension)
```

Instance UMVVMClassExtension_View for the UUserWdiget

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMView.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bindings_initialized`` (bool):  [Read-Only] Is the Initialize method called.
- ``constructed`` (bool):  [Read-Only] Is the Construct method called.
- ``events_initialized`` (bool):  [Read-Only] Is the Initialize method called.
- ``extensions`` (Array[MVVMViewExtension]):  [Read-Only]
- ``has_default_tick_binding`` (bool):  [Read-Only] Is the view is registered to the binding subsystem for tick.
- ``log_binding`` (bool):  [Read-Write] Should log when a binding is executed.
- ``number_of_source_with_tick_binding`` (uint8):  [Read-Only] The number of source has at least one binding that need to be ticked every frame.
- ``sources`` (Array[MVVMView_Source]):  [Read-Only]
- ``sources_initialized`` (bool):  [Read-Only] Is the Initialize method called.
- ``valid_sources`` (uint64):  [Read-Only] Bitfield that represents the valid sources.

<a id="unreal.MVVMView.uninitialize_sources"></a>

#### uninitialize_sources

```python
def uninitialize_sources() -> None
```

x.uninitialize_sources() -> None
Uninitialize the sources if they are already initialized.
It will uninitialized the bindings.

<a id="unreal.MVVMView.uninitialize_events"></a>

#### uninitialize_events

```python
def uninitialize_events() -> None
```

x.uninitialize_events() -> None
Uninitialize the events if they are already initialized.

<a id="unreal.MVVMView.uninitialize_bindings"></a>

#### uninitialize_bindings

```python
def uninitialize_bindings() -> None
```

x.uninitialize_bindings() -> None
Uninitialize the bindings if they are already initialized.

<a id="unreal.MVVMView.set_view_model_by_class"></a>

#### set_view_model_by_class

```python
def set_view_model_by_class(new_value: NotifyFieldValueChanged) -> bool
```

x.set_view_model_by_class(new_value) -> bool
Set the first viewmodel matching the exact specified type. If none is found, set the first viewmodel matching a child of the specified type
The viewmodel needs to be settable and it should have a valid name.
If the view is initialized, all bindings that uses that viewmodel will be re-executed with the new viewmodel instance.

Args:
    new_value (NotifyFieldValueChanged): 

Returns:
    bool:

<a id="unreal.MVVMView.set_view_model"></a>

#### set_view_model

```python
def set_view_model(view_model_name: Name,
                   view_model: NotifyFieldValueChanged) -> bool
```

x.set_view_model(view_model_name, view_model) -> bool
Set the viewmodel of the specified name.
The viewmodel needs to be settable and the type should match (child of the defined viewmodel).
If the view is initialized, all bindings that uses that viewmodel will be re-executed with the new viewmodel instance.

Args:
    view_model_name (Name): 
    view_model (NotifyFieldValueChanged): 

Returns:
    bool:

<a id="unreal.MVVMView.initialize_sources"></a>

#### initialize_sources

```python
def initialize_sources() -> None
```

x.initialize_sources() -> None
Initialize the sources if they are not already initialized.
Initializing the sources will also initialize the bindings if the option bInitializeBindingsOnConstruct is enabled.
note: A sources can be a viewmodel or any other object used by a binding.

<a id="unreal.MVVMView.initialize_events"></a>

#### initialize_events

```python
def initialize_events() -> None
```

x.initialize_events() -> None
Initialize the events if they are not already initialized.

<a id="unreal.MVVMView.initialize_bindings"></a>

#### initialize_bindings

```python
def initialize_bindings() -> None
```

x.initialize_bindings() -> None
Initialize the bindings if they are not already initialized.
Initializing the bindings will execute them.

<a id="unreal.MVVMView.get_view_model"></a>

#### get_view_model

```python
def get_view_model(view_model_name: Name) -> NotifyFieldValueChanged
```

x.get_view_model(view_model_name) -> NotifyFieldValueChanged
Find and return the viewmodel with the specified name.

Args:
    view_model_name (Name): 

Returns:
    NotifyFieldValueChanged:

<a id="unreal.MVVMView.execute_view_model_bindings"></a>

#### execute_view_model_bindings

```python
def execute_view_model_bindings(view_model_name: Name) -> bool
```

x.execute_view_model_bindings(view_model_name) -> bool
Execute all the bindings that use the viewmodel.

Args:
    view_model_name (Name): 

Returns:
    bool:

<a id="unreal.MVVMView.are_sources_initialized"></a>

#### are_sources_initialized

```python
def are_sources_initialized() -> bool
```

x.are_sources_initialized() -> bool
The sources were initialized, manually or automatically.

Returns:
    bool:

<a id="unreal.MVVMView.are_events_initialized"></a>

#### are_events_initialized

```python
def are_events_initialized() -> bool
```

x.are_events_initialized() -> bool
The events were initialized, manually or automatically.

Returns:
    bool:

<a id="unreal.MVVMView.are_bindings_initialized"></a>

#### are_bindings_initialized

```python
def are_bindings_initialized() -> bool
```

x.are_bindings_initialized() -> bool
The bindings were initialized, manually or automatically.

Returns:
    bool:

<a id="unreal.MVVMViewExtension"></a>