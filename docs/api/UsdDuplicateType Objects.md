## UsdDuplicateType Objects

```python
class UsdDuplicateType(EnumBase)
```

Describes the different types of "prim duplication" operations we support with UsdUtils::DuplicatePrims

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDDuplicateType.h

<a id="unreal.UsdDuplicateType.FLATTEN_COMPOSED_PRIM"></a>

#### FLATTEN_COMPOSED_PRIM

0: Generate a flattened duplicate of the composed prim onto the current edit target

<a id="unreal.UsdDuplicateType.SINGLE_LAYER_SPECS"></a>

#### SINGLE_LAYER_SPECS

1: Duplicate the prim's specs on the current edit target only

<a id="unreal.UsdDuplicateType.ALL_LOCAL_LAYER_SPECS"></a>

#### ALL_LOCAL_LAYER_SPECS

2: Duplicate each of the prim's specs across the entire stage

<a id="unreal.UsdSaveDialogBehavior"></a>