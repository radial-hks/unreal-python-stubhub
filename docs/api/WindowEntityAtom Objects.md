## WindowEntityAtom Objects

```python
class WindowEntityAtom(EntityAtomBase)
```

Window Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: WindowEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``layer_order`` (str):  [Read-Write]
- ``offset`` (Vector2D):  [Read-Write]
- ``size`` (Vector2D):  [Read-Write]
- ``url`` (str):  [Read-Write]

<a id="unreal.WindowEntityAtom.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write]

<a id="unreal.WindowEntityAtom.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.WindowEntityAtom.size"></a>

#### size

```python
@property
def size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WindowEntityAtom.size"></a>

#### size

```python
@size.setter
def size(value: Vector2D) -> None
```

<a id="unreal.WindowEntityAtom.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WindowEntityAtom.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.WindowEntityAtom.layer_order"></a>

#### layer\_order

```python
@property
def layer_order() -> str
```

(str):  [Read-Write]

<a id="unreal.WindowEntityAtom.layer_order"></a>

#### layer\_order

```python
@layer_order.setter
def layer_order(value: str) -> None
```

<a id="unreal.WindowEntityAtom.set_url"></a>

#### set\_url

```python
def set_url(newurl: str) -> bool
```

x.set_url(newurl) -> bool
Set Url

Args:
    newurl (str): 

Returns:
    bool:

<a id="unreal.WindowEntityAtom.set_size"></a>

#### set\_size

```python
def set_size(newsize: Vector2D) -> bool
```

x.set_size(newsize) -> bool
Set Size

Args:
    newsize (Vector2D): 

Returns:
    bool:

<a id="unreal.WindowEntityAtom.set_offset"></a>

#### set\_offset

```python
def set_offset(newoffset: Vector2D) -> bool
```

x.set_offset(newoffset) -> bool
Set Offset

Args:
    newoffset (Vector2D): 

Returns:
    bool:

<a id="unreal.WindowEntityPickAtom"></a>