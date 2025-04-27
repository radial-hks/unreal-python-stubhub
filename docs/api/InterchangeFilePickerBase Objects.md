## InterchangeFilePickerBase Objects

```python
class InterchangeFilePickerBase(Object)
```

Interchange File Picker Base

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeFilePickerBase.h

<a id="unreal.InterchangeFilePickerBase.scripted_file_picker_for_translator_type"></a>

#### scripted_file_picker_for_translator_type

```python
def scripted_file_picker_for_translator_type(
    translator_type: InterchangeTranslatorType
) -> Optional[Tuple[InterchangeFilePickerParameters, Array[str]]]
```

x.scripted_file_picker_for_translator_type(translator_type) -> (parameters=InterchangeFilePickerParameters, out_filenames=Array[str]) or None
Non-virtual helper that allows Blueprint to implement an event-based function to implement FilePickerForTranslatorType().

Args:
    translator_type (InterchangeTranslatorType): 

Returns:
    tuple or None: 

    parameters (InterchangeFilePickerParameters): 

    out_filenames (Array[str]):

<a id="unreal.InterchangeFilePickerBase.scripted_file_picker_for_translator_asset_type"></a>

#### scripted_file_picker_for_translator_asset_type

```python
def scripted_file_picker_for_translator_asset_type(
    translator_asset_type: InterchangeTranslatorAssetType
) -> Optional[Tuple[InterchangeFilePickerParameters, Array[str]]]
```

x.scripted_file_picker_for_translator_asset_type(translator_asset_type) -> (parameters=InterchangeFilePickerParameters, out_filenames=Array[str]) or None
Non-virtual helper that allows Blueprint to implement an event-based function to implement FilePickerForTranslatorAssetType().

Args:
    translator_asset_type (InterchangeTranslatorAssetType): 

Returns:
    tuple or None: 

    parameters (InterchangeFilePickerParameters): 

    out_filenames (Array[str]):

<a id="unreal.InterchangePipelineConfigurationBase"></a>