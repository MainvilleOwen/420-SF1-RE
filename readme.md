# Tactical Grid Engine

## Description

This project is a **turn-based tactical grid engine** written in Python using **Pygame**. It is inspired by games such as *Final Fantasy Tactics* and focuses on grid-based movement, tile interaction, and clean separation between game systems (tiles, units, rendering, and input).

The engine features an **isometric tilemap renderer** with layered draw order to ensure tiles and units are drawn correctly in 3D space. Tiles can have different properties (walkable, unwalkable, special visuals), and units can occupy tiles both logically and visually.

Units move using flood-fill pathfinding to determine reachable tiles, then follow a reconstructed path with **smooth, frame-based interpolation** rather than snapping tile-to-tile. Units also rotate and face correct directions based on their movement vector, and use simple sprite-based animations while moving.

The engine supports:
- Isometric tilemaps with height layers (z-axis)
- Correct tile and unit draw ordering
- Tile highlighting (hovered, selectable, movement range, attack range)
- Click-to-select and click-to-move controls
- Unit movement with animation and facing logic
- A structure designed for easy extension (combat, AI, abilities, turn systems)

This project is intended as a **foundation system** rather than a complete game, allowing additional mechanics to be built on top of it.

---

## How to Run the Program

1. Make sure **Python 3** is installed on your system.
2. Install the required dependency:
   ```bash
   pip install pygame-ce
   ```
3. Ensure all project files and asset folders remain in the same directory structure.
4. Run the program by executing:
   ```bash
   python main.py
   ```

All initialization (screen setup, asset loading, tilemap creation, and unit spawning) is handled automatically when the program starts.

---

## Controls

- **Mouse Hover**
  - Hovering over a tile highlights it:
    - White if it is walkable
    - Red if it is unwalkable

- **Unit Interaction**
  - Hovering over a unit displays:
    - Blue tiles: movement range (based on speed)
    - Red tiles: attack range (based on reach)
  - Tiles that are both attackable and walkable appear blue

- **Mouse Click (Left Click)**
  - Click a unit to select it
  - Click a blue tile to move the selected unit to that tile

- **Keyboard Controls**
  - `Up Arrow`: Rotate the tilemap 90° clockwise
  - `Down Arrow`: Rotate the tilemap 90° counter-clockwise
  - `Esc`: Lift tiles off the screen and exit the program

---

## Tilemap System Overview

- Tilemaps are defined as **3D nested lists** (x, y, z) inside `TileMaps.py`.
- Each tile stores:
  - Its sprite
  - Whether it is walkable
  - Which unit (if any) occupies it
- Tiles never permanently change their sprite; instead, **conversion dictionaries** are used at draw time to display selected, blocked, or highlighted versions.

Tile occupancy supports:
- Logical occupancy (game logic)
- Visual occupancy (draw ordering)
- Combined occupancy helpers for convenience

Draw order is dynamically calculated to ensure correct rendering of tiles and units in isometric space.

---

## Unit System Overview

- Units store their current tile, facing direction, animation state, and stats
- Movement range is calculated using flood-fill
- Paths are reconstructed and followed using smooth pixel-based motion
- Units animate while moving and return to an idle sprite when finished
- Facing direction updates automatically based on movement direction

Units are designed to be easily extended with:
- Combat logic
- Abilities
- Turn-based systems
- AI behaviors

---

## Project Purpose

This engine was created as a **technical foundation** for a tactical RPG-style project. The focus is on clean structure, readable logic, and extensibility rather than polished gameplay. It demonstrates understanding of game loops, rendering order, state management, and object-oriented design in Python.

