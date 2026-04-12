## MatCollectionSetting Objects

```python
class MatCollectionSetting(StructBase)
```

Mat Collection Setting

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: TOD_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_value`` (MatCollectionSetting_BaseValue):  [Read-Write]
- ``mat_para_col`` (MaterialParameterCollection):  [Read-Write]

<a id="unreal.MatCollectionSetting.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mat_para_col: MaterialParameterCollection = None,
             base_value: MatCollectionSetting_BaseValue = [{}, {}]) -> None
```

<a id="unreal.MatCollectionSetting.mat_para_col"></a>

#### mat\_para\_col

```python
@property
def mat_para_col() -> MaterialParameterCollection
```

(MaterialParameterCollection):  [Read-Write]

<a id="unreal.MatCollectionSetting.mat_para_col"></a>

#### mat\_para\_col

```python
@mat_para_col.setter
def mat_para_col(value: MaterialParameterCollection) -> None
```

<a id="unreal.MatCollectionSetting.base_value"></a>

#### base\_value

```python
@property
def base_value() -> MatCollectionSetting_BaseValue
```

(MatCollectionSetting_BaseValue):  [Read-Write]

<a id="unreal.MatCollectionSetting.base_value"></a>

#### base\_value

```python
@base_value.setter
def base_value(value: MatCollectionSetting_BaseValue) -> None
```

<a id="unreal.MatCollectionSetting_Array"></a>