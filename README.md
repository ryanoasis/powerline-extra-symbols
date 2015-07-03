# Powerline Extra Symbols

Extra glyphs for your powerline separators (work in progress)

![preview](preview.png)

_NOTE: This repo will soon probably just hold the glyphs. The patched fonts will eventually be available in [ryanoasis/font-nerd-icons](https://github.com/ryanoasis/font-nerd-icons)_

Vim preview also showing column number glyph:

![preview](preview-3.png)

This prompt is on fiiire (flaming shell), just having some fun:

![preview](preview-4.png)

![font forge](fontforge.png)

# Sample Configurations

Example configuration I have for [milkbikis powerline-shell](https://github.com/milkbikis/powerline-shell)

```py
        # original
        'patched': {
                'lock': u'\uE0A2',
                'network': u'\uE0A2',
                'separator': u'\uE0B0',
                'separator_thin': u'\uE0B1'
        },
        # angly 1
        'patched': {
                'lock': u'\uE0A2',
                'network': u'\uE0A2',
                'separator': u'\uE0B8',
                'separator_thin': u'\uE0B9'
        },
        # angly 2
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0BC',
        	'separator_thin': u'\uE0BD'
        },
        # curvy
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0B4',
        	'separator_thin': u'\uE0B5'
        },
        # flames (flamey)
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0C0',
        	'separator_thin': u'\uE0C1'
        },
        # lego (blocky)
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0CE',
        	'separator_thin': u'\uE0CF'
        },
        # pixelated blocks 2 (large) random fade (pixey)
        'patched': {
        	'lock': u'\uE0A2',
        	'network': u'\uE0A2',
        	'separator': u'\uE0C6',
        	'separator_thin': u'\uE0C6'
        }
```

## TODO

* [ ] Add more triangles
* [ ] Add more other type glyphs
* [ ] Create Powerline symbol only font for `fontconfig`
* [ ] Add to more fonts (just testing the included [Droid font](/patched-fonts) for now)
* [ ] Add glyph set to patcher and fonts in [ryanoasis/font-nerd-icons](https://github.com/ryanoasis/font-nerd-icons)
