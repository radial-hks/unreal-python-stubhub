## ValidateAssetsSettings Objects

```python
class ValidateAssetsSettings(StructBase)
```

Validate Assets Settings

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: EditorValidatorSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``capture_asset_load_logs`` (bool):  [Read-Write] If true, captures log warnings and errors from loading assets for validation and reports them as validation results
- ``capture_logs_during_validation`` (bool):  [Read-Write] If true, captures log warnings and errors from other operations that happen during validation and adds them to validation results
- ``capture_warnings_during_validation_as_errors`` (bool):  [Read-Write] If true, captured log warnings during validation are added to the validation results as errors (requires bCaptureLogsDuringValidation)
- ``collect_per_asset_details`` (bool):  [Read-Write] If true, will add an FValidateAssetsDetails for each asset to the results
- ``load_assets_for_validation`` (bool):  [Read-Write] If false, unloaded assets will get skipped from validation.
- ``max_assets_to_validate`` (int32):  [Read-Write] Maximum number of assets to attempt to validate
- ``show_if_no_failures`` (bool):  [Read-Write] If true, will add notifications for files with no validation and display even if everything passes
- ``skip_excluded_directories`` (bool):  [Read-Write] If true, will not validate files in excluded directories
- ``validate_referencers_of_deleted_assets`` (bool):  [Read-Write] Should we validate referencers of deleted assets in changelists
- ``validation_usecase`` (DataValidationUsecase):  [Read-Write] The usecase requiring datavalidation

<a id="unreal.ValidateAssetsSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        skip_excluded_directories: bool = False,
        show_if_no_failures: bool = False,
        collect_per_asset_details: bool = False,
        validation_usecase: DataValidationUsecase = DataValidationUsecase.NONE,
        load_assets_for_validation: bool = False,
        capture_asset_load_logs: bool = False,
        capture_logs_during_validation: bool = False,
        capture_warnings_during_validation_as_errors: bool = False,
        max_assets_to_validate: int = 0,
        validate_referencers_of_deleted_assets: bool = False) -> None
```

<a id="unreal.ValidateAssetsSettings.skip_excluded_directories"></a>

#### skip\_excluded\_directories

```python
@property
def skip_excluded_directories() -> bool
```

(bool):  [Read-Write] If true, will not validate files in excluded directories

<a id="unreal.ValidateAssetsSettings.skip_excluded_directories"></a>

#### skip\_excluded\_directories

```python
@skip_excluded_directories.setter
def skip_excluded_directories(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.show_if_no_failures"></a>

#### show\_if\_no\_failures

```python
@property
def show_if_no_failures() -> bool
```

(bool):  [Read-Write] If true, will add notifications for files with no validation and display even if everything passes

<a id="unreal.ValidateAssetsSettings.show_if_no_failures"></a>

#### show\_if\_no\_failures

```python
@show_if_no_failures.setter
def show_if_no_failures(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.collect_per_asset_details"></a>

#### collect\_per\_asset\_details

```python
@property
def collect_per_asset_details() -> bool
```

(bool):  [Read-Write] If true, will add an FValidateAssetsDetails for each asset to the results

<a id="unreal.ValidateAssetsSettings.collect_per_asset_details"></a>

#### collect\_per\_asset\_details

```python
@collect_per_asset_details.setter
def collect_per_asset_details(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.validation_usecase"></a>

#### validation\_usecase

```python
@property
def validation_usecase() -> DataValidationUsecase
```

(DataValidationUsecase):  [Read-Write] The usecase requiring datavalidation

<a id="unreal.ValidateAssetsSettings.validation_usecase"></a>

#### validation\_usecase

```python
@validation_usecase.setter
def validation_usecase(value: DataValidationUsecase) -> None
```

<a id="unreal.ValidateAssetsSettings.load_assets_for_validation"></a>

#### load\_assets\_for\_validation

```python
@property
def load_assets_for_validation() -> bool
```

(bool):  [Read-Write] If false, unloaded assets will get skipped from validation.

<a id="unreal.ValidateAssetsSettings.load_assets_for_validation"></a>

#### load\_assets\_for\_validation

```python
@load_assets_for_validation.setter
def load_assets_for_validation(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.capture_asset_load_logs"></a>

#### capture\_asset\_load\_logs

```python
@property
def capture_asset_load_logs() -> bool
```

(bool):  [Read-Write] If true, captures log warnings and errors from loading assets for validation and reports them as validation results

<a id="unreal.ValidateAssetsSettings.capture_asset_load_logs"></a>

#### capture\_asset\_load\_logs

```python
@capture_asset_load_logs.setter
def capture_asset_load_logs(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.capture_logs_during_validation"></a>

#### capture\_logs\_during\_validation

```python
@property
def capture_logs_during_validation() -> bool
```

(bool):  [Read-Write] If true, captures log warnings and errors from other operations that happen during validation and adds them to validation results

<a id="unreal.ValidateAssetsSettings.capture_logs_during_validation"></a>

#### capture\_logs\_during\_validation

```python
@capture_logs_during_validation.setter
def capture_logs_during_validation(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.capture_warnings_during_validation_as_errors"></a>

#### capture\_warnings\_during\_validation\_as\_errors

```python
@property
def capture_warnings_during_validation_as_errors() -> bool
```

(bool):  [Read-Write] If true, captured log warnings during validation are added to the validation results as errors (requires bCaptureLogsDuringValidation)

<a id="unreal.ValidateAssetsSettings.capture_warnings_during_validation_as_errors"></a>

#### capture\_warnings\_during\_validation\_as\_errors

```python
@capture_warnings_during_validation_as_errors.setter
def capture_warnings_during_validation_as_errors(value: bool) -> None
```

<a id="unreal.ValidateAssetsSettings.max_assets_to_validate"></a>

#### max\_assets\_to\_validate

```python
@property
def max_assets_to_validate() -> int
```

(int32):  [Read-Write] Maximum number of assets to attempt to validate

<a id="unreal.ValidateAssetsSettings.max_assets_to_validate"></a>

#### max\_assets\_to\_validate

```python
@max_assets_to_validate.setter
def max_assets_to_validate(value: int) -> None
```

<a id="unreal.ValidateAssetsSettings.validate_referencers_of_deleted_assets"></a>

#### validate\_referencers\_of\_deleted\_assets

```python
@property
def validate_referencers_of_deleted_assets() -> bool
```

(bool):  [Read-Write] Should we validate referencers of deleted assets in changelists

<a id="unreal.ValidateAssetsSettings.validate_referencers_of_deleted_assets"></a>

#### validate\_referencers\_of\_deleted\_assets

```python
@validate_referencers_of_deleted_assets.setter
def validate_referencers_of_deleted_assets(value: bool) -> None
```

<a id="unreal.InterchangeAnimationPayLoadKey"></a>