## ProviderPollResult Objects

```python
class ProviderPollResult(StructBase)
```

Provider Poll Result

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkMessageBusFinder.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_valid_provider`` (bool):  [Read-Only] Whether the provider is valid (compatible with the current version of LiveLink)
- ``machine_name`` (str):  [Read-Write] The name of the machine the provider is running on
- ``name`` (str):  [Read-Write] The name of the provider

<a id="unreal.ProviderPollResult.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             machine_name: str = "",
             is_valid_provider: bool = False) -> None
```

<a id="unreal.ProviderPollResult.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Only] The name of the provider

<a id="unreal.ProviderPollResult.machine_name"></a>

#### machine_name

```python
@property
def machine_name() -> str
```

(str):  [Read-Only] The name of the machine the provider is running on

<a id="unreal.ProviderPollResult.is_valid_provider"></a>

#### is_valid_provider

```python
@property
def is_valid_provider() -> bool
```

(bool):  [Read-Only] Whether the provider is valid (compatible with the current version of LiveLink)

<a id="unreal.AnimNode_LiveLinkPose"></a>