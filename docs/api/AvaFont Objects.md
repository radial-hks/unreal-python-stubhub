## AvaFont Objects

```python
class AvaFont(StructBase)
```

Ava Font

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheText
- **File**: AvaFont.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current_font`` (Font):  [Read-Write] Deprecated - used to reference the font used by FAvaFont.
  Older assets still have the font stored in this field. Calling GetFont() will move the font to the currently used MotionDesignFontObject property
  deprecated: MotionDesignFontObject is the property currently handling the font.

<a id="unreal.AvaFont.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AvaFont.current_font"></a>

#### current_font

```python
@property
def current_font() -> Font
```

(Font):  [Read-Write] Deprecated - used to reference the font used by FAvaFont.
Older assets still have the font stored in this field. Calling GetFont() will move the font to the currently used MotionDesignFontObject property
deprecated: MotionDesignFontObject is the property currently handling the font.

<a id="unreal.AvaFont.current_font"></a>

#### current_font

```python
@current_font.setter
def current_font(value: Font) -> None
```

<a id="unreal.AvalancheFont"></a>