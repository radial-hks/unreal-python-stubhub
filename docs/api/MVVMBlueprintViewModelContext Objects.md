## MVVMBlueprintViewModelContext Objects

```python
class MVVMBlueprintViewModelContext(StructBase)
```

MVVMBlueprint View Model Context

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewModelContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``create_getter_function`` (bool):  [Read-Write] Generate a public getter for this viewmodel.
  note: Always false when using a Instanced viewmodel.
- ``create_setter_function`` (bool):  [Read-Write] Generate a public setter for this viewmodel.
  note: Always true when the Creation Type is Manual.
- ``creation_type`` (MVVMBlueprintViewModelContextCreationType):  [Read-Write] When the view is spawn, create an instance of the viewmodel.
- ``expose_instance_in_editor`` (bool):  [Read-Write] Expose the viewmodel instance on every instance of the user widget for modification in editor.
- ``force_execute_bindings_on_set_source`` (bool):  [Read-Write] When a viewmodel is set manually and the viewmodel already initialized, then always execute the bindings associated with that viewmodel.
  For performance and to keep the same pattern in all UMG, the bindings are usually skip if the new viewmodel value match the previous viewmodel value.
  This behavior can be desired if the widget is inside a pool or a binding has a side effect with another widget.
- ``global_view_model_collection_update`` (bool):  [Read-Write] Auto update the instance when the viewmodel is added/removed/modifed from the global viewmodel collection.
- ``global_view_model_identifier`` (Name):  [Read-Write] Identifier of an already registered viewmodel.
- ``instanced_view_model`` (MVVMBlueprintInstancedViewModelBase):  [Read-Write]
- ``notify_field_value_class`` (type(Class)):  [Read-Write]
- ``optional`` (bool):  [Read-Write] Optional. Will not warn if the instance is not set or found.
  note: Always true when the Creation Type is Manual.
- ``resolver`` (MVVMViewModelContextResolver):  [Read-Write]
- ``view_model_context_id`` (Guid):  [Read-Only] When the view is spawn, create an instance of the viewmodel.
- ``view_model_name`` (Name):  [Read-Write] Property name that will be generated.
- ``view_model_property_path`` (str):  [Read-Write] The Path to get the viewmodel instance.

<a id="unreal.MVVMBlueprintViewModelContext.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMViewClass_EventKey"></a>