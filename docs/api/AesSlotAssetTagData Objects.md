## AesSlotAssetTagData Objects

```python
class AesSlotAssetTagData(StructBase)
```

插槽资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesSlotAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_asset`` (AesAssetChildMetaData):  [Read-Write] 子资产引用，可以为空
- ``ratio`` (float):  [Read-Write] 资产出现比例

<a id="unreal.AesSlotAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    ratio: float = 0.000000,
    child_asset: AesAssetChildMetaData = [[
        "None", 0, 0, "None", False, {}, "", [""]
    ], True, True, AesAssetTransformControlType.NONE, 0.000000, 0.000000,
                                          0.000000,
                                          [0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          [0.000000, 0.000000, 0.000000],
                                          [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]], [],
                                          []]
) -> None
```

<a id="unreal.AesSlotAssetTagData.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write] 资产出现比例

<a id="unreal.AesSlotAssetTagData.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.AesSlotAssetTagData.child_asset"></a>

#### child\_asset

```python
@property
def child_asset() -> AesAssetChildMetaData
```

(AesAssetChildMetaData):  [Read-Write] 子资产引用，可以为空

<a id="unreal.AesSlotAssetTagData.child_asset"></a>

#### child\_asset

```python
@child_asset.setter
def child_asset(value: AesAssetChildMetaData) -> None
```

<a id="unreal.AesSlotAssetData"></a>