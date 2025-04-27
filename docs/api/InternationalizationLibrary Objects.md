## InternationalizationLibrary Objects

```python
class InternationalizationLibrary(BlueprintFunctionLibrary)
```

Kismet Internationalization Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetInternationalizationLibrary.h

<a id="unreal.InternationalizationLibrary.set_current_locale"></a>

#### set_current_locale

```python
@classmethod
def set_current_locale(cls,
                       culture: str,
                       save_to_config: bool = False) -> bool
```

X.set_current_locale(culture, save_to_config=False) -> bool
Set *only* the current locale (for internationalization).
note: Unless you're doing something advanced, you likely want SetCurrentLanguageAndLocale or SetCurrentCulture instead.

Args:
    culture (str): The locale to set, as an IETF language tag (eg, "zh-Hans-CN").
    save_to_config (bool): If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

Returns:
    bool: True if the locale was set, false otherwise.

<a id="unreal.InternationalizationLibrary.set_current_language_and_locale"></a>

#### set_current_language_and_locale

```python
@classmethod
def set_current_language_and_locale(cls,
                                    culture: str,
                                    save_to_config: bool = False) -> bool
```

X.set_current_language_and_locale(culture, save_to_config=False) -> bool
Set the current language (for localization) and locale (for internationalization).

Args:
    culture (str): The language and locale to set, as an IETF language tag (eg, "zh-Hans-CN").
    save_to_config (bool): If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

Returns:
    bool: True if the language and locale were set, false otherwise.

<a id="unreal.InternationalizationLibrary.set_current_language"></a>

#### set_current_language

```python
@classmethod
def set_current_language(cls,
                         culture: str,
                         save_to_config: bool = False) -> bool
```

X.set_current_language(culture, save_to_config=False) -> bool
Set *only* the current language (for localization).
note: Unless you're doing something advanced, you likely want SetCurrentLanguageAndLocale or SetCurrentCulture instead.

Args:
    culture (str): The language to set, as an IETF language tag (eg, "zh-Hans-CN").
    save_to_config (bool): If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

Returns:
    bool: True if the language was set, false otherwise.

<a id="unreal.InternationalizationLibrary.set_current_culture"></a>

#### set_current_culture

```python
@classmethod
def set_current_culture(cls,
                        culture: str,
                        save_to_config: bool = False) -> bool
```

X.set_current_culture(culture, save_to_config=False) -> bool
Set the current culture.
note: This function is a sledgehammer, and will set both the language and locale, as well as clear out any asset group cultures that may be set.

Args:
    culture (str): The culture to set, as an IETF language tag (eg, "zh-Hans-CN").
    save_to_config (bool): If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

Returns:
    bool: True if the culture was set, false otherwise.

<a id="unreal.InternationalizationLibrary.set_current_asset_group_culture"></a>

#### set_current_asset_group_culture

```python
@classmethod
def set_current_asset_group_culture(cls,
                                    asset_group: Name,
                                    culture: str,
                                    save_to_config: bool = False) -> bool
```

X.set_current_asset_group_culture(asset_group, culture, save_to_config=False) -> bool
Set the given asset group category culture from an IETF language tag (eg, "zh-Hans-CN").

Args:
    asset_group (Name): The asset group to set the culture for.
    culture (str): The culture to set, as an IETF language tag (eg, "zh-Hans-CN").
    save_to_config (bool): If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

Returns:
    bool: True if the culture was set, false otherwise.

<a id="unreal.InternationalizationLibrary.is_culture_right_to_left"></a>

#### is_culture_right_to_left

```python
@classmethod
def is_culture_right_to_left(cls, culture: str) -> bool
```

X.is_culture_right_to_left(culture) -> bool
Returns if the given culture reads left to right

Args:
    culture (str): The culture to get the display name of, as an IETF language tag (eg, "zh-Hans-CN")

Returns:
    bool: True if the given culture reads left to right.

<a id="unreal.InternationalizationLibrary.get_suitable_culture"></a>

#### get_suitable_culture

```python
@classmethod
def get_suitable_culture(cls,
                         available_cultures: Array[str],
                         culture_to_match: str,
                         fallback_culture: str = "en") -> str
```

X.get_suitable_culture(available_cultures, culture_to_match, fallback_culture="en") -> str
Given a list of available cultures, try and find the most suitable culture from the list based on culture prioritization.
  eg) If your list was [en, fr, de] and the given culture was "en-US", this function would return "en".
  eg) If your list was [zh, ar, pl] and the given culture was "en-US", this function would return the fallback culture.

Args:
    available_cultures (Array[str]): List of available cultures to filter against (see GetLocalizedCultures).
    culture_to_match (str): Culture to try and match (see GetCurrentLanguage).
    fallback_culture (str): The culture to return if there is no suitable match in the list (typically your native culture, see GetNativeCulture).

Returns:
    str: The culture as an IETF language tag (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_native_culture"></a>

#### get_native_culture

```python
@classmethod
def get_native_culture(cls, text_category: LocalizedTextSourceCategory) -> str
```

X.get_native_culture(text_category) -> str
Get the native culture for the given localization category.

Args:
    text_category (LocalizedTextSourceCategory): 

Returns:
    str: The culture as an IETF language tag (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_localized_cultures"></a>

#### get_localized_cultures

```python
@classmethod
def get_localized_cultures(cls,
                           include_game: bool = True,
                           include_engine: bool = False,
                           include_editor: bool = False,
                           include_additional: bool = False) -> Array[str]
```

X.get_localized_cultures(include_game=True, include_engine=False, include_editor=False, include_additional=False) -> Array[str]
Get the list of cultures that have localization data available for them.

Args:
    include_game (bool): Check for localized game resources.
    include_engine (bool): Check for localized engine resources.
    include_editor (bool): Check for localized editor resources.
    include_additional (bool): Check for localized additional (eg, plugin) resources.

Returns:
    Array[str]: The list of cultures as IETF language tags (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_current_locale"></a>

#### get_current_locale

```python
@classmethod
def get_current_locale(cls) -> str
```

X.get_current_locale() -> str
Get the current locale (for internationalization) as an IETF language tag:
 - A two-letter ISO 639-1 language code (eg, "zh").
 - An optional four-letter ISO 15924 script code (eg, "Hans").
 - An optional two-letter ISO 3166-1 country code (eg, "CN").

Returns:
    str: The locale as an IETF language tag (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_current_language"></a>

#### get_current_language

```python
@classmethod
def get_current_language(cls) -> str
```

X.get_current_language() -> str
Get the current language (for localization) as an IETF language tag:
 - A two-letter ISO 639-1 language code (eg, "zh").
 - An optional four-letter ISO 15924 script code (eg, "Hans").
 - An optional two-letter ISO 3166-1 country code (eg, "CN").

Returns:
    str: The language as an IETF language tag (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_current_culture"></a>

#### get_current_culture

```python
@classmethod
def get_current_culture(cls) -> str
```

X.get_current_culture() -> str
Get the current culture as an IETF language tag:
 - A two-letter ISO 639-1 language code (eg, "zh").
 - An optional four-letter ISO 15924 script code (eg, "Hans").
 - An optional two-letter ISO 3166-1 country code (eg, "CN").
note: This function exists for legacy API parity with SetCurrentCulture and is equivalent to GetCurrentLanguage.

Returns:
    str: The culture as an IETF language tag (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_current_asset_group_culture"></a>

#### get_current_asset_group_culture

```python
@classmethod
def get_current_asset_group_culture(cls, asset_group: Name) -> str
```

X.get_current_asset_group_culture(asset_group) -> str
Get the given asset group category culture.
note: Returns the current language if the group category doesn't have a culture override.

Args:
    asset_group (Name): The asset group to get the culture for.

Returns:
    str: The culture as an IETF language tag (eg, "zh-Hans-CN").

<a id="unreal.InternationalizationLibrary.get_culture_display_name"></a>

#### get_culture_display_name

```python
@classmethod
def get_culture_display_name(cls, culture: str, localized: bool = True) -> str
```

X.get_culture_display_name(culture, localized=True) -> str
Get the display name of the given culture.

Args:
    culture (str): The culture to get the display name of, as an IETF language tag (eg, "zh-Hans-CN")
    localized (bool): True to get the localized display name (the name of the culture in its own language), or False to get the display name in the current language.

Returns:
    str: The display name of the culture, or the given culture code on failure.

<a id="unreal.InternationalizationLibrary.clear_current_asset_group_culture"></a>

#### clear_current_asset_group_culture

```python
@classmethod
def clear_current_asset_group_culture(cls,
                                      asset_group: Name,
                                      save_to_config: bool = False) -> None
```

X.clear_current_asset_group_culture(asset_group, save_to_config=False) -> None
Clear the given asset group category culture.

Args:
    asset_group (Name): The asset group to clear the culture for.
    save_to_config (bool): If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload.

<a id="unreal.MaterialLibrary"></a>