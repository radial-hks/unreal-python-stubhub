## AesTilesHighlightParam Objects

```python
class AesTilesHighlightParam(AesTilesVisualApiParamBase)
```

Highlight

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``highlight`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesHighlightParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             highlight: bool = False,
             style_name: Name = "None") -> None
```

<a id="unreal.AesTilesHighlightParam.highlight"></a>

#### highlight

```python
@property
def highlight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesHighlightParam.highlight"></a>

#### highlight

```python
@highlight.setter
def highlight(value: bool) -> None
```

<a id="unreal.AesTilesHighlightParam.style_name"></a>

#### style\_name

```python
@property
def style_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesHighlightParam.style_name"></a>

#### style\_name

```python
@style_name.setter
def style_name(value: Name) -> None
```

<a id="unreal.AesTilesHighlightNodeIdParam"></a>