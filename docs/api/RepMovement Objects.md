## RepMovement Objects

```python
class RepMovement(StructBase)
```

Replicated movement data of our RootComponent.
Struct used for efficient replication as velocity and location are generally replicated together (this saves a repindex)
and velocity.Z is commonly zero (most position replications are for walking pawns).

**C++ Source:**

- **Module**: Engine
- **File**: ReplicatedState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location_quantization_level`` (VectorQuantization):  [Read-Write] Allows tuning the compression level for the replicated location vector. You should only need to change this from the default if you see visual artifacts.
- ``rotation_quantization_level`` (RotatorQuantization):  [Read-Write] Allows tuning the compression level for replicated rotation. You should only need to change this from the default if you see visual artifacts.
- ``velocity_quantization_level`` (VectorQuantization):  [Read-Write] Allows tuning the compression level for the replicated velocity vectors. You should only need to change this from the default if you see visual artifacts.

<a id="unreal.RepMovement.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.WidgetChild"></a>