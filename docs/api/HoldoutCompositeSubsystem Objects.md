## HoldoutCompositeSubsystem Objects

```python
class HoldoutCompositeSubsystem(WorldSubsystem)
```

Composite subsytem used as an interface to the (private) scene view extension.

**C++ Source:**

- **Plugin**: HoldoutComposite
- **Module**: HoldoutComposite
- **File**: HoldoutCompositeSubsystem.h

<a id="unreal.HoldoutCompositeSubsystem.unregister_primitive"></a>

#### unregister_primitive

```python
def unregister_primitive(primitive_component: PrimitiveComponent,
                         holdout_state: bool = False) -> None
```

x.unregister_primitive(primitive_component, holdout_state=False) -> None
Unregister a single primitive from compositing.

Args:
    primitive_component (PrimitiveComponent): 
    holdout_state (bool):

<a id="unreal.HoldoutCompositeSubsystem.register_primitive"></a>

#### register_primitive

```python
def register_primitive(primitive_component: PrimitiveComponent,
                       holdout_state: bool = True) -> None
```

x.register_primitive(primitive_component, holdout_state=True) -> None
Register a single primitive for compositing.

Args:
    primitive_component (PrimitiveComponent): 
    holdout_state (bool):

<a id="unreal.AnimationEditorPreviewActor"></a>