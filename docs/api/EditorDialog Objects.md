## EditorDialog Objects

```python
class EditorDialog(BlueprintFunctionLibrary)
```

Utility class to create simple pop-up dialogs to notify the user of task completion,
or to ask them to make simple Yes/No/Retry/Cancel type decisions.

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorDialogLibrary.h

<a id="unreal.EditorDialog.show_suppressable_warning_dialog"></a>

#### show_suppressable_warning_dialog

```python
@classmethod
def show_suppressable_warning_dialog(cls,
                                     title: Text,
                                     message: Text,
                                     ini_setting_name: str,
                                     ini_setting_file_name_override: str = "",
                                     default_value: bool = True) -> bool
```

X.show_suppressable_warning_dialog(title, message, ini_setting_name, ini_setting_file_name_override="", default_value=True) -> bool
Open a modal suppressable warning window, if suppressed will return the default value

Args:
    title (Text): The title of the created dialog window
    message (Text): Text of the message to show
    ini_setting_name (str): The name of the entry in the INI where the state of the "Disable this warning" check box is stored
    ini_setting_file_name_override (str): The name of the INI where the state of the InIniSettingName flag is stored (defaults to GEditorPerProjectIni)
    default_value (bool): If the warning is suppressed, the function will log and return DefaultValue

Returns:
    bool: The result of the users decision, or DefaultValue if suppressed.

<a id="unreal.EditorDialog.show_objects_details_view"></a>

#### show_objects_details_view

```python
@classmethod
def show_objects_details_view(
    cls,
    title: Text,
    out_objects: Array[Object],
    options: EditorDialogLibraryObjectDetailsViewOptions = [
        True, True, False, 0, 0, 0.600000
    ]
) -> bool
```

X.show_objects_details_view(title, out_objects, options=[True, True, False, 0, 0, 0.600000]) -> bool
Open a modal message box dialog containing a details view for inspecting / modifying multiples UObjects.

Args:
    title (Text): The title of the created dialog window
    out_objects (Array[Object]): Array of object instances which are supposed to be viewed
    options (EditorDialogLibraryObjectDetailsViewOptions): Optional settings to customize the look of the details view

Returns:
    bool: The result of the users decision, true=Ok, false=Cancel, or false if running in unattended mode.

<a id="unreal.EditorDialog.show_object_details_view"></a>

#### show_object_details_view

```python
@classmethod
def show_object_details_view(
    cls,
    title: Text,
    out_object: Object,
    options: EditorDialogLibraryObjectDetailsViewOptions = [
        True, True, False, 0, 0, 0.600000
    ]
) -> bool
```

X.show_object_details_view(title, out_object, options=[True, True, False, 0, 0, 0.600000]) -> bool
Open a modal message box dialog containing a details view for inspecting / modifying a UObject.

Args:
    title (Text): The title of the created dialog window
    out_object (Object): Object instance of ClassOfObject which is supposed to be viewed
    options (EditorDialogLibraryObjectDetailsViewOptions): Optional settings to customize the look of the details view

Returns:
    bool: The result of the users decision, true=Ok, false=Cancel, or false if running in unattended mode.

<a id="unreal.EditorDialog.show_message"></a>

#### show_message

```python
@classmethod
def show_message(
    cls,
    title: Text,
    message: Text,
    message_type: AppMsgType,
    default_value: AppReturnType = AppReturnType.NO,
    message_category: AppMsgCategory = AppMsgCategory.WARNING
) -> AppReturnType
```

X.show_message(title, message, message_type, default_value=AppReturnType.NO, message_category=AppMsgCategory.WARNING) -> AppReturnType
Open a modal message box dialog with the given message. If running in "-unattended" mode it will immediately
return the value specified by DefaultValue. If not running in "-unattended" mode then it will block execution
until the user makes a decision, at which point their decision will be returned.

Args:
    title (Text): The title of the created dialog window
    message (Text): Text of the message to show
    message_type (AppMsgType): Specifies which buttons the dialog should have
    default_value (AppReturnType): If the application is Unattended, the function will log and return DefaultValue
    message_category (AppMsgCategory): The category of the message (affects the icon used)

Returns:
    AppReturnType: The result of the users decision, or DefaultValue if running in unattended mode.

<a id="unreal.EditorFilterLibrary"></a>