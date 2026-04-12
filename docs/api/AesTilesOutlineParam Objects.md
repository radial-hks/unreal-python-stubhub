## AesTilesOutlineParam Objects

```python
class AesTilesOutlineParam(AesTilesVisualApiParamBase)
```

Outline

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``outline`` (bool):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesOutlineParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             outline: bool = False,
             style_name: Name = "None") -> None
```

<a id="unreal.AesTilesOutlineParam.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesOutlineParam.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.AesTilesOutlineParam.style_name"></a>

#### style\_name

```python
@property
def style_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesOutlineParam.style_name"></a>

#### style\_name

```python
@style_name.setter
def style_name(value: Name) -> None
```

<a id="unreal.AesTilesOutlineNodeIdParam"></a>