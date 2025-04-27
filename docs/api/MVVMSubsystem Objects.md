## MVVMSubsystem Objects

```python
class MVVMSubsystem(EngineSubsystem)
```

MVVMSubsystem

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMSubsystem.h

<a id="unreal.MVVMSubsystem.k2_get_view_from_user_widget"></a>

#### k2_get_view_from_user_widget

```python
def k2_get_view_from_user_widget(user_widget: UserWidget) -> MVVMView
```

x.k2_get_view_from_user_widget(user_widget) -> MVVMView
K2 Get View from User Widget

Args:
    user_widget (UserWidget): 

Returns:
    MVVMView:

<a id="unreal.MVVMSubsystem.get_view_from_user_widget"></a>

#### get_view_from_user_widget

```python
def get_view_from_user_widget(user_widget: UserWidget) -> MVVMView
```

deprecated: 'get_view_from_user_widget' was renamed to 'k2_get_view_from_user_widget'.

<a id="unreal.MVVMSubsystem.k2_get_available_bindings"></a>

#### k2_get_available_bindings

```python
def k2_get_available_bindings(class_: Class,
                              accessor: Class) -> Array[MVVMAvailableBinding]
```

x.k2_get_available_bindings(class_, accessor) -> Array[MVVMAvailableBinding]


Args:
    class_ (type(Class)): 
    accessor (type(Class)): 

Returns:
    Array[MVVMAvailableBinding]: The list of all the AvailableBindings that are available for the Class.

<a id="unreal.MVVMSubsystem.get_available_bindings"></a>

#### get_available_bindings

```python
def get_available_bindings(class_: Class,
                           accessor: Class) -> Array[MVVMAvailableBinding]
```

deprecated: 'get_available_bindings' was renamed to 'k2_get_available_bindings'.

<a id="unreal.MVVMSubsystem.k2_get_available_binding"></a>

#### k2_get_available_binding

```python
def k2_get_available_binding(class_: Class, binding_name: MVVMBindingName,
                             accessor: Class) -> MVVMAvailableBinding
```

x.k2_get_available_binding(class_, binding_name, accessor) -> MVVMAvailableBinding


Args:
    class_ (type(Class)): 
    binding_name (MVVMBindingName): 
    accessor (type(Class)): 

Returns:
    MVVMAvailableBinding: The AvailableBinding from a BindingName.

<a id="unreal.MVVMSubsystem.get_available_binding"></a>

#### get_available_binding

```python
def get_available_binding(class_: Class, binding_name: MVVMBindingName,
                          accessor: Class) -> MVVMAvailableBinding
```

deprecated: 'get_available_binding' was renamed to 'k2_get_available_binding'.

<a id="unreal.MVVMSubsystem.k2_compare_float_values"></a>

#### k2_compare_float_values

```python
def k2_compare_float_values(operation: MVVMConditionOperation,
                            value: float,
                            compare_value: float,
                            compare_max_value: float = 0.000000) -> bool
```

x.k2_compare_float_values(operation, value, compare_value, compare_max_value=0.000000) -> bool
K2 Compare Float Values

Args:
    operation (MVVMConditionOperation): 
    value (float): 
    compare_value (float): 
    compare_max_value (float): 

Returns:
    bool:

<a id="unreal.MVVMSubsystem.get_global_view_model_collection"></a>

#### get_global_view_model_collection

```python
def get_global_view_model_collection() -> MVVMViewModelCollectionObject
```

x.get_global_view_model_collection() -> MVVMViewModelCollectionObject
Get Global View Model Collection
deprecated: Function 'GetGlobalViewModelCollection' is deprecated.

Returns:
    MVVMViewModelCollectionObject:

<a id="unreal.MVVMSubsystem.does_widget_tree_contained_widget"></a>

#### does_widget_tree_contained_widget

```python
def does_widget_tree_contained_widget(widget_tree: WidgetTree,
                                      view_widget: Widget) -> bool
```

x.does_widget_tree_contained_widget(widget_tree, view_widget) -> bool
Does Widget Tree Contained Widget

Args:
    widget_tree (WidgetTree): 
    view_widget (Widget): 

Returns:
    bool:

<a id="unreal.MVVMViewModelBase"></a>