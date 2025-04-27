## LightingChannels Objects

```python
class LightingChannels(StructBase)
```

Specifies which lighting channels are relevant

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel0`` (bool):  [Read-Write] Default channel for all primitives and lights.
- ``channel1`` (bool):  [Read-Write] First custom channel
- ``channel2`` (bool):  [Read-Write] Second custom channel

<a id="unreal.LightingChannels.__init__"></a>

#### __init__

```python
def __init__(channel0: bool = False,
             channel1: bool = False,
             channel2: bool = False) -> None
```

<a id="unreal.LightingChannels.channel0"></a>

#### channel0

```python
@property
def channel0() -> bool
```

(bool):  [Read-Only] Default channel for all primitives and lights.

<a id="unreal.LightingChannels.channel1"></a>

#### channel1

```python
@property
def channel1() -> bool
```

(bool):  [Read-Only] First custom channel

<a id="unreal.LightingChannels.channel2"></a>

#### channel2

```python
@property
def channel2() -> bool
```

(bool):  [Read-Only] Second custom channel

<a id="unreal.GeometryCollectionDamagePropagationData"></a>