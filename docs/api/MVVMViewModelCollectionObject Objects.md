## MVVMViewModelCollectionObject Objects

```python
class MVVMViewModelCollectionObject(Object)
```

MVVMView Model Collection Object

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMViewModelCollection.h

<a id="unreal.MVVMViewModelCollectionObject.remove_view_model"></a>

#### remove_view_model

```python
def remove_view_model(context: MVVMViewModelContext) -> bool
```

x.remove_view_model(context) -> bool
Remove View Model

Args:
    context (MVVMViewModelContext): 

Returns:
    bool:

<a id="unreal.MVVMViewModelCollectionObject.remove_all_view_model_instance"></a>

#### remove_all_view_model_instance

```python
def remove_all_view_model_instance(view_model: MVVMViewModelBase) -> int
```

x.remove_all_view_model_instance(view_model) -> int32
Remove All View Model Instance

Args:
    view_model (MVVMViewModelBase): 

Returns:
    int32:

<a id="unreal.MVVMViewModelCollectionObject.find_view_model_instance"></a>

#### find_view_model_instance

```python
def find_view_model_instance(
        context: MVVMViewModelContext) -> MVVMViewModelBase
```

x.find_view_model_instance(context) -> MVVMViewModelBase
Find View Model Instance

Args:
    context (MVVMViewModelContext): 

Returns:
    MVVMViewModelBase:

<a id="unreal.MVVMViewModelCollectionObject.find_first_view_model_instance_of_type"></a>

#### find_first_view_model_instance_of_type

```python
def find_first_view_model_instance_of_type(
        view_model_class: Class) -> MVVMViewModelBase
```

x.find_first_view_model_instance_of_type(view_model_class) -> MVVMViewModelBase
Finds a View Model of the given type.
If the collection contains multiple instances of the same type then this will return the first one found.

Args:
    view_model_class (type(Class)): 

Returns:
    MVVMViewModelBase:

<a id="unreal.MVVMViewModelCollectionObject.add_view_model_instance"></a>

#### add_view_model_instance

```python
def add_view_model_instance(context: MVVMViewModelContext,
                            view_model: MVVMViewModelBase) -> bool
```

x.add_view_model_instance(context, view_model) -> bool
Add View Model Instance

Args:
    context (MVVMViewModelContext): 
    view_model (MVVMViewModelBase): 

Returns:
    bool:

<a id="unreal.MVVMViewModelContextResolver"></a>