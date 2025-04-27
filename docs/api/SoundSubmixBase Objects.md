## SoundSubmixBase Objects

```python
class SoundSubmixBase(Object)
```

Sound Submix Base

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_disable`` (bool):  [Read-Write] Auto-manage enabling and disabling the submix as a CPU optimization. It will be disabled if the submix and all child submixes are silent. It will re-enable if a sound is sent to the submix or a child submix is audible.
- ``auto_disable_time`` (float):  [Read-Write] The minimum amount of time to wait before automatically disabling a submix if it is silent. Will immediately re-enable if source audio is sent to it.
- ``child_submixes`` (Array[SoundSubmixBase]):  [Read-Only] Child submixes to this sound mix

<a id="unreal.SoundSubmixBase.auto_disable"></a>

#### auto_disable

```python
@property
def auto_disable() -> bool
```

(bool):  [Read-Only] Auto-manage enabling and disabling the submix as a CPU optimization. It will be disabled if the submix and all child submixes are silent. It will re-enable if a sound is sent to the submix or a child submix is audible.

<a id="unreal.SoundSubmixBase.auto_disable_time"></a>

#### auto_disable_time

```python
@property
def auto_disable_time() -> float
```

(float):  [Read-Write] The minimum amount of time to wait before automatically disabling a submix if it is silent. Will immediately re-enable if source audio is sent to it.

<a id="unreal.SoundSubmixBase.auto_disable_time"></a>

#### auto_disable_time

```python
@auto_disable_time.setter
def auto_disable_time(value: float) -> None
```

<a id="unreal.SoundSubmixBase.child_submixes"></a>

#### child_submixes

```python
@property
def child_submixes() -> Array[SoundSubmixBase]
```

(Array[SoundSubmixBase]):  [Read-Only] Child submixes to this sound mix

<a id="unreal.SoundSubmixBase.find_dynamic_ancestor"></a>

#### find_dynamic_ancestor

```python
def find_dynamic_ancestor() -> SoundSubmixBase
```

x.find_dynamic_ancestor() -> SoundSubmixBase
Searching upwards from this Submix to the root looking for the first Submix marked Dynamic
If this Submix is Dynamic this will be returned.

Returns:
    SoundSubmixBase:

<a id="unreal.SoundSubmixBase.dynamic_disconnect"></a>

#### dynamic_disconnect

```python
def dynamic_disconnect(world_context_object: Object) -> bool
```

x.dynamic_disconnect(world_context_object) -> bool
Dynamically Disconnect from a parent.

Args:
    world_context_object (Object): UObject that's used to GetWorld

Returns:
    bool:

<a id="unreal.SoundSubmixBase.dynamic_connect"></a>

#### dynamic_connect

```python
def dynamic_connect(world_context_object: Object,
                    parent: SoundSubmixBase) -> bool
```

x.dynamic_connect(world_context_object, parent) -> bool
Dynamically Connects to a parent submix.

Args:
    world_context_object (Object): UObject that's used to GetWorld
    parent (SoundSubmixBase): Parent Submix to connect to

Returns:
    bool:

<a id="unreal.SoundSubmixWithParentBase"></a>