## MVVMEditorSubsystem Objects

```python
class MVVMEditorSubsystem(EditorSubsystem)
```

MVVMEditor Subsystem

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelEditor
- **File**: MVVMEditorSubsystem.h

<a id="unreal.MVVMEditorSubsystem.verify_view_model_rename"></a>

#### verify_view_model_rename

```python
def verify_view_model_rename(widget_blueprint: WidgetBlueprint,
                             view_model: Name,
                             new_view_model: Name) -> Optional[Text]
```

x.verify_view_model_rename(widget_blueprint, view_model, new_view_model) -> Text or None
Verify View Model Rename

Args:
    widget_blueprint (WidgetBlueprint): 
    view_model (Name): 
    new_view_model (Name): 

Returns:
    Text or None: 

    out_error (Text):

<a id="unreal.MVVMEditorSubsystem.request_view"></a>

#### request_view

```python
def request_view(widget_blueprint: WidgetBlueprint) -> MVVMBlueprintView
```

x.request_view(widget_blueprint) -> MVVMBlueprintView
Request View

Args:
    widget_blueprint (WidgetBlueprint): 

Returns:
    MVVMBlueprintView:

<a id="unreal.MVVMEditorSubsystem.reparent_view_model"></a>

#### reparent_view_model

```python
def reparent_view_model(widget_blueprint: WidgetBlueprint, view_model: Name,
                        new_view_model: Class) -> Optional[Text]
```

x.reparent_view_model(widget_blueprint, view_model, new_view_model) -> Text or None
Reparent View Model

Args:
    widget_blueprint (WidgetBlueprint): 
    view_model (Name): 
    new_view_model (type(Class)): 

Returns:
    Text or None: 

    out_error (Text):

<a id="unreal.MVVMEditorSubsystem.rename_view_model"></a>

#### rename_view_model

```python
def rename_view_model(widget_blueprint: WidgetBlueprint, view_model: Name,
                      new_view_model: Name) -> Optional[Text]
```

x.rename_view_model(widget_blueprint, view_model, new_view_model) -> Text or None
Rename View Model

Args:
    widget_blueprint (WidgetBlueprint): 
    view_model (Name): 
    new_view_model (Name): 

Returns:
    Text or None: 

    out_error (Text):

<a id="unreal.MVVMEditorSubsystem.remove_view_model"></a>

#### remove_view_model

```python
def remove_view_model(widget_blueprint: WidgetBlueprint,
                      view_model: Name) -> None
```

x.remove_view_model(widget_blueprint, view_model) -> None
Remove View Model

Args:
    widget_blueprint (WidgetBlueprint): 
    view_model (Name):

<a id="unreal.MVVMEditorSubsystem.remove_event"></a>

#### remove_event

```python
def remove_event(widget_blueprint: WidgetBlueprint,
                 event: MVVMBlueprintViewEvent) -> None
```

x.remove_event(widget_blueprint, event) -> None
Remove Event

Args:
    widget_blueprint (WidgetBlueprint): 
    event (MVVMBlueprintViewEvent):

<a id="unreal.MVVMEditorSubsystem.remove_condition"></a>

#### remove_condition

```python
def remove_condition(widget_blueprint: WidgetBlueprint,
                     condition: MVVMBlueprintViewCondition) -> None
```

x.remove_condition(widget_blueprint, condition) -> None
Remove Condition

Args:
    widget_blueprint (WidgetBlueprint): 
    condition (MVVMBlueprintViewCondition):

<a id="unreal.MVVMEditorSubsystem.remove_binding"></a>

#### remove_binding

```python
def remove_binding(widget_blueprint: WidgetBlueprint,
                   binding: MVVMBlueprintViewBinding) -> None
```

x.remove_binding(widget_blueprint, binding) -> None
Remove Binding

Args:
    widget_blueprint (WidgetBlueprint): 
    binding (MVVMBlueprintViewBinding):

<a id="unreal.MVVMEditorSubsystem.is_valid_conversion_function"></a>

#### is_valid_conversion_function

```python
def is_valid_conversion_function(
        widget_blueprint: WidgetBlueprint, function: Function,
        source: MVVMBlueprintPropertyPath,
        destination: MVVMBlueprintPropertyPath) -> bool
```

x.is_valid_conversion_function(widget_blueprint, function, source, destination) -> bool
Is Valid Conversion Function

Args:
    widget_blueprint (WidgetBlueprint): 
    function (Function): 
    source (MVVMBlueprintPropertyPath): 
    destination (MVVMBlueprintPropertyPath): 

Returns:
    bool:

<a id="unreal.MVVMEditorSubsystem.is_simple_conversion_function"></a>

#### is_simple_conversion_function

```python
def is_simple_conversion_function(function: Function) -> bool
```

x.is_simple_conversion_function(function) -> bool
Is Simple Conversion Function

Args:
    function (Function): 

Returns:
    bool:

<a id="unreal.MVVMEditorSubsystem.get_view"></a>

#### get_view

```python
def get_view(widget_blueprint: WidgetBlueprint) -> MVVMBlueprintView
```

x.get_view(widget_blueprint) -> MVVMBlueprintView
Get View

Args:
    widget_blueprint (WidgetBlueprint): 

Returns:
    MVVMBlueprintView:

<a id="unreal.MVVMEditorSubsystem.get_conversion_function_node"></a>

#### get_conversion_function_node

```python
def get_conversion_function_node(
        widget_blueprint: WidgetBlueprint, binding: MVVMBlueprintViewBinding,
        source_to_destination: bool) -> K2Node_CallFunction
```

x.get_conversion_function_node(widget_blueprint, binding, source_to_destination) -> K2Node_CallFunction
Get Conversion Function Node

Args:
    widget_blueprint (WidgetBlueprint): 
    binding (MVVMBlueprintViewBinding): 
    source_to_destination (bool): 

Returns:
    K2Node_CallFunction:

<a id="unreal.MVVMEditorSubsystem.get_conversion_function_graph"></a>

#### get_conversion_function_graph

```python
def get_conversion_function_graph(widget_blueprint: WidgetBlueprint,
                                  binding: MVVMBlueprintViewBinding,
                                  source_to_destination: bool) -> EdGraph
```

x.get_conversion_function_graph(widget_blueprint, binding, source_to_destination) -> EdGraph
Get Conversion Function Graph

Args:
    widget_blueprint (WidgetBlueprint): 
    binding (MVVMBlueprintViewBinding): 
    source_to_destination (bool): 

Returns:
    EdGraph:

<a id="unreal.MVVMEditorSubsystem.get_conversion_function"></a>

#### get_conversion_function

```python
def get_conversion_function(widget_blueprint: WidgetBlueprint,
                            binding: MVVMBlueprintViewBinding,
                            source_to_destination: bool) -> Function
```

x.get_conversion_function(widget_blueprint, binding, source_to_destination) -> Function
Get Conversion Function

Args:
    widget_blueprint (WidgetBlueprint): 
    binding (MVVMBlueprintViewBinding): 
    source_to_destination (bool): 

Returns:
    Function:

<a id="unreal.MVVMEditorSubsystem.get_child_view_models"></a>

#### get_child_view_models

```python
def get_child_view_models(class_: Class,
                          accessor: Class) -> Array[MVVMAvailableBinding]
```

x.get_child_view_models(class_, accessor) -> Array[MVVMAvailableBinding]
Get Child View Models

Args:
    class_ (type(Class)): 
    accessor (type(Class)): 

Returns:
    Array[MVVMAvailableBinding]:

<a id="unreal.MVVMEditorSubsystem.get_available_conversion_functions"></a>

#### get_available_conversion_functions

```python
def get_available_conversion_functions(
        widget_blueprint: WidgetBlueprint, source: MVVMBlueprintPropertyPath,
        destination: MVVMBlueprintPropertyPath) -> Array[Function]
```

x.get_available_conversion_functions(widget_blueprint, source, destination) -> Array[Function]
Get Available Conversion Functions

Args:
    widget_blueprint (WidgetBlueprint): 
    source (MVVMBlueprintPropertyPath): 
    destination (MVVMBlueprintPropertyPath): 

Returns:
    Array[Function]:

<a id="unreal.MVVMEditorSubsystem.add_view_model"></a>

#### add_view_model

```python
def add_view_model(widget_blueprint: WidgetBlueprint,
                   view_model: Class) -> Guid
```

x.add_view_model(widget_blueprint, view_model) -> Guid
Add View Model

Args:
    widget_blueprint (WidgetBlueprint): 
    view_model (type(Class)): 

Returns:
    Guid:

<a id="unreal.MVVMEditorSubsystem.add_instanced_view_model"></a>

#### add_instanced_view_model

```python
def add_instanced_view_model(widget_blueprint: WidgetBlueprint) -> Guid
```

x.add_instanced_view_model(widget_blueprint) -> Guid
Add Instanced View Model

Args:
    widget_blueprint (WidgetBlueprint): 

Returns:
    Guid:

<a id="unreal.MVVMEditorSubsystem.add_event"></a>

#### add_event

```python
def add_event(widget_blueprint: WidgetBlueprint) -> MVVMBlueprintViewEvent
```

x.add_event(widget_blueprint) -> MVVMBlueprintViewEvent
Add Event

Args:
    widget_blueprint (WidgetBlueprint): 

Returns:
    MVVMBlueprintViewEvent:

<a id="unreal.MVVMEditorSubsystem.add_condition"></a>

#### add_condition

```python
def add_condition(
        widget_blueprint: WidgetBlueprint) -> MVVMBlueprintViewCondition
```

x.add_condition(widget_blueprint) -> MVVMBlueprintViewCondition
Add Condition

Args:
    widget_blueprint (WidgetBlueprint): 

Returns:
    MVVMBlueprintViewCondition:

<a id="unreal.MVVMEditorSubsystem.add_binding"></a>

#### add_binding

```python
def add_binding(widget_blueprint: WidgetBlueprint) -> MVVMBlueprintViewBinding
```

x.add_binding(widget_blueprint) -> MVVMBlueprintViewBinding
Add Binding

Args:
    widget_blueprint (WidgetBlueprint): 

Returns:
    MVVMBlueprintViewBinding:

<a id="unreal.MVVMViewModelBindingExecTest"></a>