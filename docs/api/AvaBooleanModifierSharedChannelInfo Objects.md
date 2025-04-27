## AvaBooleanModifierSharedChannelInfo Objects

```python
class AvaBooleanModifierSharedChannelInfo(StructBase)
```

Ava Boolean Modifier Shared Channel Info

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaBooleanModifierShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_count`` (int32):  [Read-Only] The number of channel currently active
- ``channel_intersect_count`` (int32):  [Read-Only] The number of modifier intersecting with this modifier
- ``channel_modifier_count`` (int32):  [Read-Only] The number of modifier on that channel, the more there are, the more impact on performance
- ``channel_target_count`` (int32):  [Read-Only] The number of modifier on that channel that are masked by other mask modifier
- ``channel_tool_count`` (int32):  [Read-Only] The number of modifier on that channel that are used to mask other non mask modifier

<a id="unreal.AvaBooleanModifierSharedChannelInfo.__init__"></a>

#### __init__

```python
def __init__(channel_count: int = 0,
             channel_modifier_count: int = 0,
             channel_tool_count: int = 0,
             channel_target_count: int = 0,
             channel_intersect_count: int = 0) -> None
```

<a id="unreal.AvaBooleanModifierSharedChannelInfo.channel_count"></a>

#### channel_count

```python
@property
def channel_count() -> int
```

(int32):  [Read-Only] The number of channel currently active

<a id="unreal.AvaBooleanModifierSharedChannelInfo.channel_modifier_count"></a>

#### channel_modifier_count

```python
@property
def channel_modifier_count() -> int
```

(int32):  [Read-Only] The number of modifier on that channel, the more there are, the more impact on performance

<a id="unreal.AvaBooleanModifierSharedChannelInfo.channel_tool_count"></a>

#### channel_tool_count

```python
@property
def channel_tool_count() -> int
```

(int32):  [Read-Only] The number of modifier on that channel that are used to mask other non mask modifier

<a id="unreal.AvaBooleanModifierSharedChannelInfo.channel_target_count"></a>

#### channel_target_count

```python
@property
def channel_target_count() -> int
```

(int32):  [Read-Only] The number of modifier on that channel that are masked by other mask modifier

<a id="unreal.AvaBooleanModifierSharedChannelInfo.channel_intersect_count"></a>

#### channel_intersect_count

```python
@property
def channel_intersect_count() -> int
```

(int32):  [Read-Only] The number of modifier intersecting with this modifier

<a id="unreal.AvaMaterialParameterMap"></a>