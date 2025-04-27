## MVVMView_Source Objects

```python
class MVVMView_Source(StructBase)
```

Instance FMVVMViewClass_Source for the UUserWdiget

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMView.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``assigned_to_user_widget_property`` (bool):  [Read-Only] The source was set to a UserWidget property.
- ``bindings_initialized`` (bool):  [Read-Only] The source bindings are initialized.
- ``class_key`` (MVVMViewClass_SourceKey):  [Read-Only] The key of this source in the ViewClass.
- ``registered_count`` (int32):  [Read-Only] Number of bindings connected to the source.
- ``set_manually`` (bool):  [Read-Only] The source was set manually via SetViewModel.
- ``source`` (Object):  [Read-Only] The source object. The source implement the INotifyFieldValueChanged interface.
- ``source_initialized`` (bool):  [Read-Only] The source is created.

<a id="unreal.MVVMView_Source.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InterchangeTestFunction"></a>