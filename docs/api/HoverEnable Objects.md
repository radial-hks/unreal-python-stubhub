## HoverEnable Objects

```python
class HoverEnable(ParamsBase)
```

Hover Enable

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpSelectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Write]
- ``entity_type`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.HoverEnable.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_type: Name = "None", enable: bool = False) -> None
```

<a id="unreal.HoverEnable.entity_type"></a>

#### entity\_type

```python
@property
def entity_type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.HoverEnable.entity_type"></a>

#### entity\_type

```python
@entity_type.setter
def entity_type(value: Name) -> None
```

<a id="unreal.HoverEnable.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HoverEnable.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.HoverBaseColor"></a>