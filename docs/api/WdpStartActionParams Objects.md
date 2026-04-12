## WdpStartActionParams Objects

```python
class WdpStartActionParams(ParamsBase)
```

Wdp Start Action Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpActionManagerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_name`` (str):  [Read-Write]
- ``action_params`` (WdpJsonObjectWrapper):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WdpStartActionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(action_name: str = "",
             action_params: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.WdpStartActionParams.action_name"></a>

#### action\_name

```python
@property
def action_name() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpStartActionParams.action_name"></a>

#### action\_name

```python
@action_name.setter
def action_name(value: str) -> None
```

<a id="unreal.WdpStartActionParams.action_params"></a>

#### action\_params

```python
@property
def action_params() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.WdpStartActionParams.action_params"></a>

#### action\_params

```python
@action_params.setter
def action_params(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.WdpEndActionParams"></a>