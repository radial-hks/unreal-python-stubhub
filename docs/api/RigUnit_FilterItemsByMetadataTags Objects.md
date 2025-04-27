## RigUnit_FilterItemsByMetadataTags Objects

```python
class RigUnit_FilterItemsByMetadataTags(RigUnit)
```

Filters an item array by a list of tags

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inclusive`` (bool):  [Read-Write] If set to true only items with ALL of tags will be returned,
  if set to false items with ANY of the tags will be removed
- ``items`` (Array[RigElementKey]):  [Read-Write] The items to filter
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``result`` (Array[RigElementKey]):  [Read-Write] The results of the filter
- ``tags`` (Array[Name]):  [Read-Write] The tags to find

<a id="unreal.RigUnit_FilterItemsByMetadataTags.__init__"></a>

#### __init__

```python
def __init__(items: Array[RigElementKey] = [],
             tags: Array[Name] = [],
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             inclusive: bool = False,
             result: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_FilterItemsByMetadataTags.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items to filter

<a id="unreal.RigUnit_FilterItemsByMetadataTags.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_FilterItemsByMetadataTags.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] The tags to find

<a id="unreal.RigUnit_FilterItemsByMetadataTags.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.RigUnit_FilterItemsByMetadataTags.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_FilterItemsByMetadataTags.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_FilterItemsByMetadataTags.inclusive"></a>

#### inclusive

```python
@property
def inclusive() -> bool
```

(bool):  [Read-Write] If set to true only items with ALL of tags will be returned,
if set to false items with ANY of the tags will be removed

<a id="unreal.RigUnit_FilterItemsByMetadataTags.inclusive"></a>

#### inclusive

```python
@inclusive.setter
def inclusive(value: bool) -> None
```

<a id="unreal.RigUnit_FilterItemsByMetadataTags.result"></a>

#### result

```python
@property
def result() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The results of the filter

<a id="unreal.RigDispatch_GetModuleMetadata"></a>