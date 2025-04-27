## EditorValidatorSubsystem Objects

```python
class EditorValidatorSubsystem(EditorSubsystem)
```

UEditorValidatorSubsystem manages all the asset validation in the engine.

The first validation handled is UObject::IsDataValid and its overridden functions.
Those validations require custom classes and are most suited to project-specific
classes.

The next validation set is of all registered UEditorValidationBases. These validators
have a function to determine if they can validate a given asset, and if they are
currently enabled. They are good candidates for validating engine classes or
very specific project logic.

Finally, this subsystem may be subclassed to change the overally behavior of
validation in your project. If a subclass exist in your project module, it will
supercede the engine validation subsystem.

**C++ Source:**

- **Plugin**: DataValidation
- **Module**: DataValidation
- **File**: EditorValidatorSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``validate_on_save`` (bool):  [Read-Write] Whether it should validate assets on save inside the editor
  deprecated: Use bValidateOnSave on UDataValidationSettings instead.

<a id="unreal.EditorValidatorSubsystem.validate_on_save"></a>

#### validate_on_save

```python
@property
def validate_on_save() -> bool
```

(bool):  [Read-Write] Whether it should validate assets on save inside the editor
deprecated: Use bValidateOnSave on UDataValidationSettings instead.

<a id="unreal.EditorValidatorSubsystem.validate_on_save"></a>

#### validate_on_save

```python
@validate_on_save.setter
def validate_on_save(value: bool) -> None
```

<a id="unreal.EditorValidatorSubsystem.validate_changelists"></a>

#### validate_changelists

```python
def validate_changelists(
    changelists: Array[DataValidationChangelist],
    settings: ValidateAssetsSettings
) -> Tuple[DataValidationResult, ValidateAssetsResults]
```

x.validate_changelists(changelists, settings) -> (DataValidationResult, out_results=ValidateAssetsResults)
Validate Changelists

Args:
    changelists (Array[DataValidationChangelist]): 
    settings (ValidateAssetsSettings): 

Returns:
    ValidateAssetsResults: 

    out_results (ValidateAssetsResults):

<a id="unreal.EditorValidatorSubsystem.validate_changelist"></a>

#### validate_changelist

```python
def validate_changelist(
    changelist: DataValidationChangelist, settings: ValidateAssetsSettings
) -> Tuple[DataValidationResult, ValidateAssetsResults]
```

x.validate_changelist(changelist, settings) -> (DataValidationResult, out_results=ValidateAssetsResults)
Called to validate assets from either the UI or a commandlet.
Loads the specified assets and runs all registered validators on them.
Populates the message log with errors and warnings with clickable links.

Args:
    changelist (DataValidationChangelist): 
    settings (ValidateAssetsSettings): Structure passing context and settings for ValidateAssetsWithSettings

Returns:
    ValidateAssetsResults: Validation results for the changelist object itself

    out_results (ValidateAssetsResults): More detailed information about the results of the validate assets command

<a id="unreal.EditorValidatorSubsystem.validate_assets_with_settings"></a>

#### validate_assets_with_settings

```python
def validate_assets_with_settings(
        asset_data_list: Array[AssetData],
        settings: ValidateAssetsSettings) -> Tuple[int, ValidateAssetsResults]
```

x.validate_assets_with_settings(asset_data_list, settings) -> (int32, out_results=ValidateAssetsResults)
Called to validate assets from either the UI or a commandlet.
Loads the specified assets and runs all registered validators on them.
Populates the message log with errors and warnings with clickable links.

Args:
    asset_data_list (Array[AssetData]): 
    settings (ValidateAssetsSettings): Structure passing context and settings for ValidateAssetsWithSettings

Returns:
    ValidateAssetsResults: Number of assets with validation failures or warnings

    out_results (ValidateAssetsResults): More detailed information about the results of the validate assets command

<a id="unreal.EditorValidatorSubsystem.remove_validator"></a>

#### remove_validator

```python
def remove_validator(validator: EditorValidatorBase) -> None
```

x.remove_validator(validator) -> None
* Removes a validator
* Should be called during module shutdown if a validator was added.

Args:
    validator (EditorValidatorBase):

<a id="unreal.EditorValidatorSubsystem.is_object_valid"></a>

#### is_object_valid

```python
def is_object_valid(
    object: Object, validation_usecase: DataValidationUsecase
) -> Tuple[DataValidationResult, Array[Text], Array[Text]]
```

x.is_object_valid(object, validation_usecase) -> (DataValidationResult, validation_errors=Array[Text], validation_warnings=Array[Text])
Runs registered validators on the provided object.
Does not add anything to any FMessageLog tabs.

Args:
    object (Object): 
    validation_usecase (DataValidationUsecase): 

Returns:
    tuple: Returns Valid if the object contains valid data; returns Invalid if the object contains invalid data; returns NotValidated if no validations was performed on the object

    validation_errors (Array[Text]): 

    validation_warnings (Array[Text]):

<a id="unreal.EditorValidatorSubsystem.is_asset_valid"></a>

#### is_asset_valid

```python
def is_asset_valid(
    asset_data: AssetData, validation_usecase: DataValidationUsecase
) -> Tuple[DataValidationResult, Array[Text], Array[Text]]
```

x.is_asset_valid(asset_data, validation_usecase) -> (DataValidationResult, validation_errors=Array[Text], validation_warnings=Array[Text])
Loads the object referred to by the provided AssetData and runs registered validators on it.
Does not add anything to any FMessageLog tabs.

Args:
    asset_data (AssetData): 
    validation_usecase (DataValidationUsecase): 

Returns:
    tuple: Returns Valid if the object pointed to by AssetData contains valid data; returns Invalid if the object contains invalid data or does not exist; returns NotValidated if no validations was performed on the object

    validation_errors (Array[Text]): 

    validation_warnings (Array[Text]):

<a id="unreal.EditorValidatorSubsystem.add_validator"></a>

#### add_validator

```python
def add_validator(validator: EditorValidatorBase) -> None
```

x.add_validator(validator) -> None
* Adds a validator to the list, making sure it is a unique instance

Args:
    validator (EditorValidatorBase):

<a id="unreal.EditorValidator_Localization"></a>