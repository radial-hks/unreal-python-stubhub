## TypedElementPrimitiveCustomDataInterface Objects

```python
class TypedElementPrimitiveCustomDataInterface(Interface)
```

Typed Element Primitive Custom Data Interface

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementPrimitiveCustomDataInterface.h

<a id="unreal.TypedElementPrimitiveCustomDataInterface.set_custom_data_value"></a>

#### set_custom_data_value

```python
def set_custom_data_value(element_handle: ScriptTypedElementHandle,
                          custom_data_index: int,
                          custom_data_value: float,
                          mark_render_state_dirty: bool = False) -> None
```

x.set_custom_data_value(element_handle, custom_data_index, custom_data_value, mark_render_state_dirty=False) -> None
Sets a single Primitive's CustomData value

Args:
    element_handle (ScriptTypedElementHandle): 
    custom_data_index (int32): 
    custom_data_value (float): 
    mark_render_state_dirty (bool):

<a id="unreal.TypedElementPrimitiveCustomDataInterface.set_custom_data"></a>

#### set_custom_data

```python
def set_custom_data(element_handle: ScriptTypedElementHandle,
                    custom_data_floats: Array[float],
                    mark_render_state_dirty: bool = False) -> None
```

x.set_custom_data(element_handle, custom_data_floats, mark_render_state_dirty=False) -> None
Sets all Primitive's CustomData values

Args:
    element_handle (ScriptTypedElementHandle): 
    custom_data_floats (Array[float]): 
    mark_render_state_dirty (bool):

<a id="unreal.TypedElementSelectionInterface"></a>