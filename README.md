# XilliaArchipelago
This is a custom world integration for [Archipelago](https://archipelago.gg/) randomizer using **Tales of Xillia (BLUS31006)** on RPCS3.
By:SchitzoAce
Contributers:

---

## 📌 Current Progress

- ✅ Basic world folder structure in place (`XilliaWorld.py`, `Items.py`, `Locations.py`, etc.)
- ✅ Items and locations defined (3 total for now)
- ✅ Region definitions initialized
- ✅ Game is detected by Archipelago as `xillia`
- 🔁 Currently troubleshooting seed generation issues

---

## 🧪 Known Issues

- ⚠️ `KeyError: 'Ramsgate Shop'`  
  └ Location isn't pre-registered before being used. Fixed by ensuring all locations are pre-populated during `create_locations()`.

- ⚠️ `IndentationError` in `XilliaWorld.py`  
  └ Caused by missing indents under function definitions. Resolved by proper formatting.

---

## 🛠️ Planned Features

- Add more locations and items
- Implement proper rules and item progression
- Add victory condition and hint system
- Integration with Tales of Xillia RPCS3 memory state (future)

---


