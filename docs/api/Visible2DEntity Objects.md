## Visible2DEntity Objects

```python
class Visible2DEntity(StructBase)
```

Visible 2DEntity

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Visible2DAtomAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``near_top`` (bool):  [Read-Write]
- ``occlusion`` (bool):  [Read-Write]
- ``overlap`` (bool):  [Read-Write]

<a id="unreal.Visible2DEntity.__init__"></a>

#### \_\_init\_\_

```python
def __init__(overlap: bool = False,
             near_top: bool = False,
             occlusion: bool = False) -> None
```

<a id="unreal.Visible2DEntity.overlap"></a>

#### overlap

```python
@property
def overlap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Visible2DEntity.overlap"></a>

#### overlap

```python
@overlap.setter
def overlap(value: bool) -> None
```

<a id="unreal.Visible2DEntity.near_top"></a>

#### near\_top

```python
@property
def near_top() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Visible2DEntity.near_top"></a>

#### near\_top

```python
@near_top.setter
def near_top(value: bool) -> None
```

<a id="unreal.Visible2DEntity.occlusion"></a>

#### occlusion

```python
@property
def occlusion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Visible2DEntity.occlusion"></a>

#### occlusion

```python
@occlusion.setter
def occlusion(value: bool) -> None
```

<a id="unreal.Visible2DInteraction"></a>