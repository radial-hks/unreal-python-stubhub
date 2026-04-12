## EnvQueryResult Objects

```python
class EnvQueryResult(StructBase)
```

Env Query Result

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item_type`` (type(Class)):  [Read-Write] type of generated items
- ``option_index`` (int32):  [Read-Write] index of query option, that generated items
- ``query_id`` (int32):  [Read-Write] instance ID

<a id="unreal.EnvQueryResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(item_type: Class = None,
             option_index: int = 0,
             query_id: int = 0) -> None
```

<a id="unreal.EnvQueryResult.item_type"></a>

#### item\_type

```python
@property
def item_type() -> Class
```

(type(Class)):  [Read-Only] type of generated items

<a id="unreal.EnvQueryResult.option_index"></a>

#### option\_index

```python
@property
def option_index() -> int
```

(int32):  [Read-Only] index of query option, that generated items

<a id="unreal.EnvQueryResult.query_id"></a>

#### query\_id

```python
@property
def query_id() -> int
```

(int32):  [Read-Only] instance ID

<a id="unreal.AIDynamicParam"></a>