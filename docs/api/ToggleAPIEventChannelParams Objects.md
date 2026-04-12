## ToggleAPIEventChannelParams Objects

```python
class ToggleAPIEventChannelParams(ParamsBase)
```

Toggle APIEvent Channel Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpAPISystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``api_events`` (Array[APIEventSwitch]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.ToggleAPIEventChannelParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(api_events: Array[APIEventSwitch] = []) -> None
```

<a id="unreal.ToggleAPIEventChannelParams.api_events"></a>

#### api\_events

```python
@property
def api_events() -> Array[APIEventSwitch]
```

(Array[APIEventSwitch]):  [Read-Write]

<a id="unreal.ToggleAPIEventChannelParams.api_events"></a>

#### api\_events

```python
@api_events.setter
def api_events(value: Array[APIEventSwitch]) -> None
```

<a id="unreal.WdpStartShowCoordParams"></a>