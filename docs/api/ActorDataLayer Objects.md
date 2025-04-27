## ActorDataLayer Objects

```python
class ActorDataLayer(StructBase)
```

This class is deprecated and only present for backward compatibility purposes.
Instead of using FActorDatalayer, directly save the DataLayerInstance FName if the DataLayer not exposed in data.
If the DataLayer is exposed in Data, then use DataLayerAssets.

**C++ Source:**

- **Module**: Engine
- **File**: ActorDataLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Only] The name of this layer

<a id="unreal.ActorDataLayer.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None") -> None
```

<a id="unreal.ActorDataLayer.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] The name of this layer

<a id="unreal.Vector_NetQuantize100"></a>