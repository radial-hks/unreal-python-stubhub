## MVVMViewModelContextResolver Objects

```python
class MVVMViewModelContextResolver(Object)
```

Shared data to find or create a ViewModel at runtime.

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMViewModelContextResolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allowed_view_model_classes`` (Array[SoftClassPath]):  [Read-Write] Viewmodel class that the resolver supports.
- ``denied_view_model_classes`` (Array[SoftClassPath]):  [Read-Write] Viewmodel class that the resolver explicitly does not support.

<a id="unreal.MVVMViewModelContextResolver.k2_destroy_instance"></a>

#### k2_destroy_instance

```python
def k2_destroy_instance(view_model: Object, view: MVVMView) -> None
```

x.k2_destroy_instance(view_model, view) -> None
K2 Destroy Instance

Args:
    view_model (Object): 
    view (MVVMView):

<a id="unreal.MVVMViewModelContextResolver.k2_create_instance"></a>

#### k2_create_instance

```python
def k2_create_instance(expected_type: Class,
                       user_widget: UserWidget) -> NotifyFieldValueChanged
```

x.k2_create_instance(expected_type, user_widget) -> NotifyFieldValueChanged
K2 Create Instance

Args:
    expected_type (type(Class)): 
    user_widget (UserWidget): 

Returns:
    NotifyFieldValueChanged:

<a id="unreal.UIFrameworkPlayerComponent"></a>