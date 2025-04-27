## TransformableComponentHandle Objects

```python
class TransformableComponentHandle(TransformableHandle)
```

Transformable Component Handle

**C++ Source:**

- **Module**: Constraints
- **File**: TransformableHandle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component`` (SceneComponent):  [Read-Write] The Component that this handle is pointing at.
- ``constraint_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] possible bindingID
- ``socket_name`` (Name):  [Read-Write] Optional socket name on Component.

<a id="unreal.TransformableComponentHandle.component"></a>

#### component

```python
@property
def component() -> SceneComponent
```

(SceneComponent):  [Read-Only] The Component that this handle is pointing at.

<a id="unreal.TransformableComponentHandle.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] Optional socket name on Component.

<a id="unreal.TickableTransformConstraint"></a>