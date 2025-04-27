## ValidateAssetsResults Objects

```python
class ValidateAssetsResults(StructBase)
```

Validate Assets Results

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: EditorValidatorSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_limit_reached`` (bool):  [Read-Only] True if FValidateAssetSettings::MaxAssetsToValidation was reached
- ``assets_details`` (Map[str, ValidateAssetsDetails]):  [Read-Only] Per asset details
  Indexed by object path
  Only returned if FValidateAssetsSettings::bCollectPerAssetDetails is true.
- ``num_checked`` (int32):  [Read-Only] Amount of tested assets
- ``num_invalid`` (int32):  [Read-Only] Amount of assets with errors
- ``num_requested`` (int32):  [Read-Only] Total amount of assets that were gathered to validate.
- ``num_skipped`` (int32):  [Read-Only] Amount of assets skipped
- ``num_unable_to_validate`` (int32):  [Read-Only] Amount of assets that could not be validated
- ``num_valid`` (int32):  [Read-Only] Amount of assets without errors or warnings
- ``num_warnings`` (int32):  [Read-Only] Amount of assets with warnings

<a id="unreal.ValidateAssetsResults.__init__"></a>

#### __init__

```python
def __init__(num_requested: int = 0,
             num_checked: int = 0,
             num_valid: int = 0,
             num_invalid: int = 0,
             num_skipped: int = 0,
             num_warnings: int = 0,
             num_unable_to_validate: int = 0,
             asset_limit_reached: bool = False,
             assets_details: Map[str, ValidateAssetsDetails] = {}) -> None
```

<a id="unreal.ValidateAssetsResults.num_requested"></a>

#### num_requested

```python
@property
def num_requested() -> int
```

(int32):  [Read-Only] Total amount of assets that were gathered to validate.

<a id="unreal.ValidateAssetsResults.num_checked"></a>

#### num_checked

```python
@property
def num_checked() -> int
```

(int32):  [Read-Only] Amount of tested assets

<a id="unreal.ValidateAssetsResults.num_valid"></a>

#### num_valid

```python
@property
def num_valid() -> int
```

(int32):  [Read-Only] Amount of assets without errors or warnings

<a id="unreal.ValidateAssetsResults.num_invalid"></a>

#### num_invalid

```python
@property
def num_invalid() -> int
```

(int32):  [Read-Only] Amount of assets with errors

<a id="unreal.ValidateAssetsResults.num_skipped"></a>

#### num_skipped

```python
@property
def num_skipped() -> int
```

(int32):  [Read-Only] Amount of assets skipped

<a id="unreal.ValidateAssetsResults.num_warnings"></a>

#### num_warnings

```python
@property
def num_warnings() -> int
```

(int32):  [Read-Only] Amount of assets with warnings

<a id="unreal.ValidateAssetsResults.num_unable_to_validate"></a>

#### num_unable_to_validate

```python
@property
def num_unable_to_validate() -> int
```

(int32):  [Read-Only] Amount of assets that could not be validated

<a id="unreal.ValidateAssetsResults.asset_limit_reached"></a>

#### asset_limit_reached

```python
@property
def asset_limit_reached() -> bool
```

(bool):  [Read-Only] True if FValidateAssetSettings::MaxAssetsToValidation was reached

<a id="unreal.ValidateAssetsResults.assets_details"></a>

#### assets_details

```python
@property
def assets_details() -> Map[str, ValidateAssetsDetails]
```

(Map[str, ValidateAssetsDetails]):  [Read-Only] Per asset details
Indexed by object path
Only returned if FValidateAssetsSettings::bCollectPerAssetDetails is true.

<a id="unreal.ValidateAssetsSettings"></a>