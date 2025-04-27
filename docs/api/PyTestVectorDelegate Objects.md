## PyTestVectorDelegate Objects

```python
class PyTestVectorDelegate(Object)
```

This class along with UPyTestStructDelegate verify that 2 UObjects with the same delegate name/type, do not collide.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PyTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_name_collision_test_delegate`` (OnNameCollisionDelegate):  [Read-Write] Called when a new item is selected in the combobox.

<a id="unreal.PyTestVectorDelegate.on_name_collision_test_delegate"></a>

#### on_name_collision_test_delegate

```python
@property
def on_name_collision_test_delegate() -> OnNameCollisionDelegate
```

(OnNameCollisionDelegate):  [Read-Write] Called when a new item is selected in the combobox.

<a id="unreal.PyTestVectorDelegate.on_name_collision_test_delegate"></a>

#### on_name_collision_test_delegate

```python
@on_name_collision_test_delegate.setter
def on_name_collision_test_delegate(value: OnNameCollisionDelegate) -> None
```

<a id="unreal.PyTestTypeHint"></a>