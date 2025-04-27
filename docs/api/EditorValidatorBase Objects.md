## EditorValidatorBase Objects

```python
class EditorValidatorBase(Object)
```

* The EditorValidatorBase is a class which verifies that an asset meets a specific ruleset.
* It should be used when checking engine-level classes, as UObject::IsDataValid requires
* overriding the base class. You can create project-specific version of the validator base,
* with custom logging and enabled logic.
*
* C++ and Blueprint validators will be gathered on editor start, while python validators need
* to register themselves

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: EditorValidatorBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``only_print_custom_message`` (bool):  [Read-Write] Whether we should also print out the source validator when printing validation errors.

<a id="unreal.EditorValidatorBase.k2_validate_loaded_asset"></a>

#### k2_validate_loaded_asset

```python
def k2_validate_loaded_asset(asset: Object) -> DataValidationResult
```

x.k2_validate_loaded_asset(asset) -> DataValidationResult
Override this in blueprint to validate assets

Args:
    asset (Object): 

Returns:
    DataValidationResult:

<a id="unreal.EditorValidatorBase.validate_loaded_asset"></a>

#### validate_loaded_asset

```python
def validate_loaded_asset(asset: Object) -> DataValidationResult
```

deprecated: 'validate_loaded_asset' was renamed to 'k2_validate_loaded_asset'.

<a id="unreal.EditorValidatorBase.k2_can_validate_asset"></a>

#### k2_can_validate_asset

```python
def k2_can_validate_asset(asset: Object) -> bool
```

x.k2_can_validate_asset(asset) -> bool
Override this to determine whether or not you can validate a given asset with this validator

Args:
    asset (Object): 

Returns:
    bool:

<a id="unreal.EditorValidatorBase.can_validate_asset"></a>

#### can_validate_asset

```python
def can_validate_asset(asset: Object) -> bool
```

deprecated: 'can_validate_asset' was renamed to 'k2_can_validate_asset'.

<a id="unreal.EditorValidatorBase.k2_can_validate"></a>

#### k2_can_validate

```python
def k2_can_validate(usecase: DataValidationUsecase) -> bool
```

x.k2_can_validate(usecase) -> bool
Override this to determine whether or not you can use this validator given this usecase

Args:
    usecase (DataValidationUsecase): 

Returns:
    bool:

<a id="unreal.EditorValidatorBase.can_validate"></a>

#### can_validate

```python
def can_validate(usecase: DataValidationUsecase) -> bool
```

deprecated: 'can_validate' was renamed to 'k2_can_validate'.

<a id="unreal.EditorValidatorBase.get_validation_result"></a>

#### get_validation_result

```python
def get_validation_result() -> DataValidationResult
```

x.get_validation_result() -> DataValidationResult
Get Validation Result

Returns:
    DataValidationResult:

<a id="unreal.EditorValidatorBase.asset_warning"></a>

#### asset_warning

```python
def asset_warning(asset: Object, message: Text) -> None
```

x.asset_warning(asset, message) -> None
Adds a message to this validation but doesn't mark it as failed.

Args:
    asset (Object): 
    message (Text):

<a id="unreal.EditorValidatorBase.asset_passes"></a>

#### asset_passes

```python
def asset_passes(asset: Object) -> None
```

x.asset_passes(asset) -> None
Marks the validation as successful. Failure to call this will report the validator as not having checked the asset.

Args:
    asset (Object):

<a id="unreal.EditorValidatorBase.asset_fails"></a>

#### asset_fails

```python
def asset_fails(asset: Object, message: Text) -> None
```

x.asset_fails(asset, message) -> None
Marks the validation as failed and adds an error message.

Args:
    asset (Object): 
    message (Text):

<a id="unreal.EditorValidator_Material"></a>