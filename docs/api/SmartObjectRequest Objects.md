## SmartObjectRequest Objects

```python
class SmartObjectRequest(StructBase)
```

Struct used to find a smart object within a specific search range and with optional filtering

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter`` (SmartObjectRequestFilter):  [Read-Write] Struct used to filter out some results (all results allowed by default)
- ``query_box`` (Box):  [Read-Write] Box defining the search range

<a id="unreal.SmartObjectRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    query_box: Box = [[0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000], False],
    filter: SmartObjectRequestFilter = [[[]], SmartObjectClaimPriority.NORMAL,
                                        [], [], True, False, False]
) -> None
```

<a id="unreal.SmartObjectRequest.query_box"></a>

#### query\_box

```python
@property
def query_box() -> Box
```

(Box):  [Read-Write] Box defining the search range

<a id="unreal.SmartObjectRequest.query_box"></a>

#### query\_box

```python
@query_box.setter
def query_box(value: Box) -> None
```

<a id="unreal.SmartObjectRequest.filter"></a>

#### filter

```python
@property
def filter() -> SmartObjectRequestFilter
```

(SmartObjectRequestFilter):  [Read-Write] Struct used to filter out some results (all results allowed by default)

<a id="unreal.SmartObjectRequest.filter"></a>

#### filter

```python
@filter.setter
def filter(value: SmartObjectRequestFilter) -> None
```

<a id="unreal.SmartObjectRequestResult"></a>