## WindowSubsystem Objects

```python
class WindowSubsystem(GameInstanceSubsystem)
```

Window Subsystem

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: WindowSubsystem.h

<a id="unreal.WindowSubsystem.register_screen_layer"></a>

#### register\_screen\_layer

```python
def register_screen_layer(layer_name: Name, z_order: int) -> bool
```

x.register_screen_layer(layer_name, z_order) -> bool
Register Screen Layer

Args:
    layer_name (Name): 
    z_order (int32): 

Returns:
    bool:

<a id="unreal.WindowSubsystem.get"></a>

#### get

```python
@classmethod
def get(cls) -> WindowSubsystem
```

X.get() -> WindowSubsystem
Get

Returns:
    WindowSubsystem:

<a id="unreal.WindowWidgetBase"></a>